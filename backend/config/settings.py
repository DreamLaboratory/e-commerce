import logging.config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ithz@*q#q7z*h1x#0)ia5hc9km1*t1p^lrvffnzr3k8z-knvpl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

ALLOWED_HOSTS = ["*"]


# Application definition

THIRD_APPS = [
    # admin_interface
    # colorfield
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    # TODO install Admin Honeypot
    # TODO install django-admin-honeypot
    # django-ckeditor
    # django-crispy-forms
    "rosetta",  # https://django-rosetta.readthedocs.io/en/latest/installation.html
    "import_export",  # https://django-import-export.readthedocs.io/en/latest/installation.html
    "django_extensions",  # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
    "debug_toolbar",  # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    "mathfilters",  # https://django-mathfilters.readthedocs.io/en/latest/installation.html
    "smart_selects",  # https://django-smart-selects.readthedocs.io/en/latest/installation.html
    "modeltranslation",  # https://django-modeltranslation.readthedocs.io/en/latest/installation.html
]

LOCAL_APPS = [
    "src.apps.accounts",
    "src.apps.common",
    "src.apps.store",
    "src.apps.cart",
    "src.apps.order",
]

INSTALLED_APPS = THIRD_APPS + LOCAL_APPS


AUTH_USER_MODEL = "accounts.Account"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "src.apps.store.category_processors.all_categories",
                "src.apps.cart.item_counter.counter",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ("en", _("English")),
    ("uz", _("Uzbek")),
)

MODELTRANSLATION_TRANSLATION_FILES = [
    "src.apps.store.translation",
]

MODELTRANSLATION_LANGUAGES = ("uz", "en")

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "uz"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [BASE_DIR / "static"]
LOCALE_PATHS = [
    BASE_DIR / "locale/",
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email configuration
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "fayzulloh00010003@gmail.com"
EMAIL_HOST_PASSWORD = "yauwzixxyhcylioi"
EMAIL_USE_TLS = True


# log file
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        },
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "errors.log",
            },
        },
        "loggers": {
            "": {"level": "ERROR", "handlers": ["file"]},
            "django.request": {"level": "INFO", "handlers": ["file"]},
        },
    }
)

# SET session expire time
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 days

# TTL for cache
CACHE_TTL = 60 * 60 * 24 * 7  # 7 days

# JQUERY_URL = True

# Login url
LOGIN_URL = "/login/"
