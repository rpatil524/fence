"""
Do not run this during normal application run-time. This is a distinct
application meant to run _before_ the app loads so that migrations can be done
safely while the app is offline.
"""
import json

from fence.models import migrate
from fence.config import config
from userdatamodel.driver import SQLAlchemyDriver
from fence import app_init, app
from cdislogging import get_logger

logger = get_logger(__name__, log_level="debug")


def run_migrations():
    app_init(app)

    if config["ENABLE_DB_MIGRATION"]:
        logger.info("Running database migration...")
        migrate(app.db)
        logger.info("Done running database migration.")
    else:
        logger.info("NOT running database migration.")
