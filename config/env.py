from pathlib import Path
import environ

Env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent