import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__name__).parent
FILES_DIR = Path(BASE_DIR, 'app', 'files')
FILES_DIR.mkdir(exist_ok=True, parents=True)


load_dotenv(Path(BASE_DIR, 'env'))


class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    ELASTIC_URL = os.environ.get('ELASTIC_URL')
