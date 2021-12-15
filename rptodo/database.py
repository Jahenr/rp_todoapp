'''This module provides the RP To-DO database functionality.'''
# rptodo/database.py

import configparser
from pathlib import Path

from rptodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

