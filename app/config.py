import os
import pathlib
import sys
from configparser import ConfigParser

from dotenv import load_dotenv
from loguru import logger

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
load_dotenv()

_config = ConfigParser()

_config["GLOBAL"] = os.environ
_config = _config["GLOBAL"]

PORT = _config.getint("PORT")
HOST = _config["HOST"]
RELOAD = _config.getboolean("RELOAD")

logger.remove()
# logging.disable()
LOGGING_FORMAT = (
    "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> "
    "<level>{level}</level>: "
    "<level>{name}</level> - "
    "<level>{message}</level>"
)

logger.add(
    ROOT_FOLDER / "logs" / "log_{time:YYYY-MM-DD}.log",
    format=LOGGING_FORMAT,
    level="DEBUG",
    mode="a",
    retention="5 days",
)
logger.add(sys.stdout, format=LOGGING_FORMAT)
