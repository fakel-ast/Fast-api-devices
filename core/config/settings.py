import dotenv
import os

PROJECT_NAME = "Devices"

# Secret key
SECRET_KEY = b"9zMdOG@3Qiasdas~mFMQ1x}GW123123MT~sf@A6Gj3qnFasdas{21321312}wetF~5PDSqOfdafaJtupKqsfsw}PD1SM"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# load env
dotenv.load_dotenv(os.path.join(BASE_DIR, '..', '.env'))

API_V1_STR = "/api/v1"

DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:5432/' \
               f'{os.environ.get("POSTGRES_DB")}'

APPS_MODELS = [
    "core.apps.api.models",
    "aerich.models",
]