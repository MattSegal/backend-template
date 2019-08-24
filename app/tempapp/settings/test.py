import fakeredis

from . import *

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True
SECRET_KEY = "test-secret-key"
ALLOWED_HOSTS = ["*"]
CACHES["default"]["OPTIONS"]["REDIS_CLIENT_CLASS"] = "fakeredis.FakeStrictRedis"
DATABASES["default"]["name"] = "test"
MEDIA_ROOT = os.path.join(BASE_DIR, "test_media")
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
