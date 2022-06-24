

from .constants.google_play import Sort  # noqa: F401
from .features.app import app  # noqa: F401
from .features.permissions import permissions  # noqa: F401
from .features.reviews import reviews, reviews_all  # noqa: F401
from .features.search import search  # noqa: F401
from .features.data_safety import data_safty  # noqa: F401
from .features.collection import collection  # noqa: F401
from .features.developer import developer  # noqa: F401

VERSION = __version__ = "1.1.0"
