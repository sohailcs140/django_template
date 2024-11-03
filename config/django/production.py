from .base import *
from config.env import Env

DEBUG=Env.bool("DEBUG", default=False)
ALLOWED_HOSTS = Env.list("ALLOWED_HOSTS", default=[])