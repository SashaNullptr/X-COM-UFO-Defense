import os

ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR, 'config_files')
DB_CONFIG = os.path.join(CONFIG_DIR, 'database.ini')

from .db_config import config
from .db_query import send_query_fetchone_no_results, send_query_fetchone
from .counter import count_rows_in_table
from .fleet_composition import unique_ship_shapes
from .evacuation_priorities import evac_priorties