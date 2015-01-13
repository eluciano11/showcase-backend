"""
Django settings for showcase_backend project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import datetime

from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    ENVIRONMENT = values.Value(environ_prefix=None)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',

        # Third party
        'django_extensions',
        'rest_framework',
        'django_gravatar',
        'corsheaders',
        'ember_drf',

        # Apps
        'showcase_backend.universities',
        'showcase_backend.departments',
        'showcase_backend.users',
        'showcase_backend.projects',
    )

    MIDDLEWARE_CLASSES = (
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'showcase_backend.urls'

    WSGI_APPLICATION = 'showcase_backend.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    STATIC_URL = '/static/'

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    MEDIA_ROOT = 'media'

    MEDIA_URL = '/media/'

    REST_FRAMEWORK = {
        'PAGINATE_BY': 10,
        'PAGINATE_BY_PARAM': 'page_size',
        'MAX_PAGINATE_BY': 100,
        'DEFAULT_RENDERER_CLASSES': (
            'ember_drf.renderers.EmberJSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'ember_drf.parsers.EmberJSONParser',
            'rest_framework.parsers.MultiPartParser',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'showcase_backend.users.authentication.JSONWebTokenAuthentication',
            'showcase_backend.users.authentication.SessionAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': (
            'rest_framework.filters.DjangoFilterBackend',
            'ember_drf.filters.CoallesceIDsFilterBackend'
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
        'PAGINATE_BY': 30,
        'PAGINATE_BY_PARAM': 'page_size',
        'MAX_PAGINATE_BY': 100
    }

    JWT_AUTH = {
        'JWT_PAYLOAD_HANDLER':
        'showcase_backend.utils.jwt_handlers.jwt_payload_handler',
        'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=8)
    }

    AUTH_USER_MODEL = 'users.User'

    LOGIN_REDIRECT_URL = '/api/users/me'

    DOMAIN = values.Value(environ_prefix=None)

    SITE_NAME = values.Value(environ_prefix=None)

    ACTIVATION_URL = values.Value(environ_prefix=None)

    PASSWORD_RESET_CONFIRM_URL = values.Value(environ_prefix=None)

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    DEFAULT_FROM_EMAIL = values.Value()
    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.IntegerValue()
    EMAIL_USE_TLS = values.BooleanValue(False)

    #CORS
    #It's true just for development purposes. we can create the whitelist later
    CORS_ORIGIN_ALLOW_ALL = True

    APPEND_SLASH = False


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'debug_toolbar',
    )

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    PROTOCOL = 'http'


class Staging(Common):
    """
    The in-staging settings.
    """
    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'djangosecure',
    )

    PROTOCOL = 'https'

    # django-secure
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )


class Production(Staging):
    """
    The in-production settings.
    """
    pass
