from . import *

DEBUG = True
SECRET_KEY = "dev-secret-key"

# Static files
STATIC_URL = "/static/"

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS = True

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = "tempapp-bot-test"
AWS_S3_CUSTOM_DOMAIN = None

LOGIN_REDIRECT_URL = "http://localhost:3000/"
LOGOUT_REDIRECT_URL = "http://localhost:3000/"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "handlers": {"console": {"level": "INFO", "class": "logging.StreamHandler"}},
    "loggers": {
        "tempapp": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "django": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "django.db.backends": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
