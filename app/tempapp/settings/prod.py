from . import *

DEBUG = False
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = [
    "tempapp.com.au",
    "api.tempapp.com.au",
    "167.99.78.141",
    "127.0.0.1",
    "localhost",
]

SESSION_COOKIE_DOMAIN = ".tempapp.com.au"
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_DOMAIN = ".tempapp.com.au"
CSRF_TRUSTED_ORIGINS = [".tempapp.com.au"]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    r"^(https?://)?(\w*-*\w*\.+)*tempapp\.com.au$",
    r"^(https?://)?(localhost|127\.0\.0\.1|0\.0\.0\.0)(:\d{4})?$",
)

# Get DRF to use HTTPS in links.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = "tempapp-bot"
AWS_S3_CUSTOM_DOMAIN = "media.tempapp.com.au"

LOGIN_REDIRECT_URL = "https://tempapp.com.au/"
LOGOUT_REDIRECT_URL = "https://tempapp.com.au/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console", "sentry"]},
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler"},
        "sentry": {
            "level": "ERROR",
            "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "raven": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "sentry.errors": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
    },
}

RAVEN_CONFIG = {"dsn": os.environ.get("TEMPAPP_RAVEN_DSN")}
