"""
API about genre
"""
from .request import get
from ..common.types import MediaType

GENRE_URL = "/genre"


def get_genre(
    media_type: MediaType = MediaType.MOVIE,
):
    url = f"{GENRE_URL}/{media_type.value}/list"
    return get(url)
