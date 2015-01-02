import uuid
import jwt
from datetime import datetime
from calendar import timegm

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from rest_framework_jwt.settings import api_settings
from django_gravatar.helpers import get_gravatar_url


from ..utils.jwt_handlers import jwt_payload_handler, jwt_encode_handler
from .managers import AccountManager, ActiveAccountManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    gravatar_url = models.URLField(blank=True)

    university = models.ForeignKey('universities.University')
    department = models.ForeignKey('departments.Department')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(
        default=False)
    is_active = models.BooleanField(default=True)

    token_version = models.CharField(
        max_length=36, default=str(uuid.uuid4()), unique=True, db_index=True)

    objects = AccountManager()
    active = ActiveAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

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
        return full_name.strip() or self.username

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name or self.email

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

        # TODO: send notification email - not sure if needed

    def reset_token_version(self):
        """
        Resets the user's token_version.
        """
        self.token_version = str(uuid.uuid4())

    def send_password_reset_email(self):
        self.email_user(
            "Reset Password",
            "robot@bookshub.com"
        )
