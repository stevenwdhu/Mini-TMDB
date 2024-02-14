"""
API about media details
"""


from .request import get
from ..common.types import MediaType

MOVIE_DETAIL_URL = "/movie"
TV_DETAIL_URL = "/tv"
PERSON_DETAIL_URL = "/person"


def get_detail(media_type: MediaType, media_id):
    """
    Get media details
    """
    url = ""
    if media_type == MediaType.MOVIE:
        url = f"{MOVIE_DETAIL_URL}/{media_id}"
    elif media_type == MediaType.TV:
        url = f"{TV_DETAIL_URL}/{media_id}"

    return get(url)


def get_credit(media_type: MediaType, media_id):
    """
    Get media credits
    """
    url = ""
    if media_type == MediaType.MOVIE:
        url = f"{MOVIE_DETAIL_URL}/{media_id}/credits"
    elif media_type == MediaType.TV:
        url = f"{TV_DETAIL_URL}/{media_id}/credits"

    return get(url)
