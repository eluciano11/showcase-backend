import uuid
import jwt
from datetime import datetime
from calendar import timegm

from django.db import models
from django.conf import settings
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser
from rest_framework_jwt.settings import api_settings
from django_gravatar.helpers import get_gravatar_url
from autoslug import AutoSlugField


from ..utils.jwt_handlers import jwt_payload_handler, jwt_encode_handler
from ..utils.mixins import ModelDiffMixin
from .managers import AccountManager, ActiveAccountManager


def populate_user_slug(instance):
    return instance.get_full_name()


class User(AbstractBaseUser, ModelDiffMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    gravatar_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from=populate_user_slug, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(
        default=False)
    is_active = models.BooleanField(default=True)

    token_version = models.CharField(
        max_length=36, default=str(uuid.uuid4()), unique=True, db_index=True)

    objects = AccountManager()
    active = ActiveAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def is_admin(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        if not self.pk or self.has_field_changed('email'):
            self.gravatar_url = get_gravatar_url(self.email, size=150)

        return super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        """
        Returns True if user is an active superuser.
        """
        if self.is_active and self.is_superuser:
            return True

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms
        for this object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if user is an active superuser.
        """
        if self.is_active and self.is_superuser:
            return True

    @property
    def token(self):
        """
        Returns a JSON Web Token used for Authentication.
        """
        payload = jwt_payload_handler(self)
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )
        return jwt_encode_handler(payload)

    @property
    def password_reset_token(self):
        """
        Returns a JSON Web Token used for Password Reset
        """
        payload = {
            'type': 'PasswordReset',
            'id': self.pk,
            'token_version': self.token_version,
        }

        jwt_token = jwt.encode(payload, settings.SECRET_KEY)

        return jwt_token.decode('utf-8')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name or self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def set_password(self, raw_password):
        """
        Sets the user's password and changes token_version.
        """
        super(User, self).set_password(raw_password)
        self.reset_token_version()

    def change_password(self, raw_password):
        """
        Sets the user's password, changes token_version, and notifies user.
        """
        self.set_password(raw_password)
        self.reset_token_version()
        self.save()

    def reset_token_version(self):
        """
        Resets the user's token_version.
        """
        self.token_version = str(uuid.uuid4())

    def get_email_context(self):
        print self.password_reset_token
        return {
            "domain": settings.DOMAIN,
            "site_name": settings.SITE_NAME,
            "token": self.password_reset_token,
            "protocol": settings.PROTOCOL,
            "url": settings.PASSWORD_RESET_CONFIRM_URL
        }

    def send_password_reset_email(self):
        self.email_user(
            subject="Reset Password",
            message=loader.render_to_string(
                "email/password_reset_email_body.txt",
                self.get_email_context())
        )
