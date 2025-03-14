import os

from .base import UdalMap

REQUESTS_TIMEOUT = os.environ.get("UDALMAP_REQUESTS_TIMEOUT", 5)