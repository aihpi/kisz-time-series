import sys
from pathlib import Path

sys.path.append("..")


BASE_DIR = Path(__file__).parent
ARTIFACTS_PATH = BASE_DIR.parent / "artifacts"
DATA_PATH = BASE_DIR.parent / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
EXTERNAL_DATA_PATH = DATA_PATH / "external"
INTERIM_DATA_PATH = DATA_PATH / "interim"
PROCESSED_DATA_PATH = DATA_PATH / "processed"
