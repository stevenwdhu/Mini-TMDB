"""
API about trending
"""

from typing import Literal
import requests as req
from .const import HEADERS
from .request import get
from ..common.types import TrendingMediaType, TrendingTimeWindow

TRENDING_URL = "/trending"


def get_trending(
    media_type: TrendingMediaType = TrendingMediaType.ALL,
    time_window: TrendingTimeWindow = TrendingTimeWindow.DAY,
    page: int = 1,
):
    """
    Get trending list
    """
    url = f"{TRENDING_URL}/{media_type.value}/{time_window.value}"
    query = {"page": page}
    return get(url, query)
