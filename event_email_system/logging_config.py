import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = os.environ.get('LOG_DIR', os.path.join(BASE_DIR, "logs"))

os.makedirs(LOG_DIR, exist_ok=True)
LOGGING_FILE = os.environ.get('LOGGING_PATH', os.path.join(LOG_DIR, "application.log"))

service_name = 'event_email_system'
role_name = 'event'


class CustomLogRecord(logging.LogRecord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.do_service = service_name
        self.role = role_name


def record_factory(*args, **kwargs):
    """"
    Added service name to logging
    """
    return CustomLogRecord(*args, **kwargs)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
        "simple": {
            "format": "%(levelname)s %(asctime)s %(module)s <PID #%(process)d> <Thread #%(thread)d> %(message)s"
        },
    },
    "handlers": {
        "django_application_file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGING_FILE,
            "maxBytes": 1024 * 1024 * 100,  # 100 MB
            "backupCount": 50,
            "formatter": "json",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "django_application_file",
                "console",
            ],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}

if hasattr(logging, "setLogRecordFactory"):
    logging.setLogRecordFactory(record_factory)
else:
    logging.log(
        logging.WARNING,
        "Failed to set custom log record factory. Using default factory.",
    )

logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s %(asctime)s %(module)s %(message)s"
)
