"""
API about air today
"""

from .request import get

AIR_TODAY_URL = "/tv/airing_today"


def get_air_today(
    page: int = 1,
):
    """
    Get air today data
    """
    url = f"{AIR_TODAY_URL}"
    query = {"page": page}
    return get(url, query)
