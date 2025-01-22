import os

DEPLOY = os.getenv("DEPLOY", "dev")
PROJECT_NAME = os.getenv("PROJECT_NAME", "tutorial")
PROJECT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

DEFAULT_LOG_DIR = os.path.join(PROJECT_DIR, "logs")
LOG_DIR = os.getenv("LOG_DIR", DEFAULT_LOG_DIR)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "unfazed.log")


# SECRET
# This is a secret key that will be used to sign cookies and other sensitive data.
DEFAULT_SECRET = "7e89ebff5e7048998e0866199644be6c929dad55b375408e91c885faea28ffcb"
SECRET = os.getenv("SECRET", DEFAULT_SECRET)

UNFAZED_SETTINGS = {
    "DEBUG": True if DEPLOY != "prod" else False,
    "DEPLOY": DEPLOY,
    "PROJECT_NAME": PROJECT_NAME,
    "ROOT_URLCONF": "entry.routes",
    "INSTALLED_APPS": ["enroll"],
    "DATABASE": {
        "CONNECTIONS": {
            "default": {
                "ENGINE": "tortoise.backends.sqlite",
                "CREDENTIALS": {
                    "FILE_PATH": os.path.join(PROJECT_DIR, "db.sqlite3"),
                },
            }
        }
    },
    # "CACHE": {
    #     "default": {
    #         "BACKEND": "unfazed.cache.backends.locmem.LocMemCache",
    #         "LOCATION": PROJECT_NAME,
    #     },
    # },
    "MIDDLEWARE": ["unfazed.middleware.internal.common.CommonMiddleware"],
    "LOGGING": {
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "standard",
                "class": "unfazed.logging.handlers.UnfazedRotatingFileHandler",
                "filename": LOG_FILE,
            },
        },
        "loggers": {
            "common": {
                "handlers": ["default"],
                "level": "INFO",
            },
        },
    },
    "OPENAPI": {
        "servers": [{"url": "http://127.0.0.1:9527", "description": "Local dev"}],
        "info": {
            "title": PROJECT_NAME,
            "version": "1.0.0",
            "description": f"API for {PROJECT_NAME}",
        },
    },
}
