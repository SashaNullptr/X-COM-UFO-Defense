import os

ROOT_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIR = os.path.join( ROOT_DIR, 'config_files' )
DB_CONFIG = os.path.join( CONFIG_DIR, 'database.ini' )
