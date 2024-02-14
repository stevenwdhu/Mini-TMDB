"""
API about search
"""

from typing import Literal
import requests as req
from .const import HEADERS
from .request import get
from ..common.types import MediaType

SEARCH_URL = "/search"


def get_search(
    query: str,
    media_type: MediaType = MediaType.MOVIE,
    page: int = 1,
):
    """
    Get a list of movie or TV shows by keyword
    """
    url = f"{SEARCH_URL}/{media_type.value}"
    params = {"page": page, "query": query}
    return get(url, params)
