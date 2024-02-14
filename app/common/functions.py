"""
Common functions
"""


from functools import cache

from app.api.genre import get_genre
from app.common.types import MediaType
from app.models.genre import Genre


@cache
def get_genre_list(media_type: MediaType):
    """
    Get movie or TV show genre list
    """
    return [
        Genre(media_type=media_type, id=genre["id"], name=genre["name"])
        for genre in get_genre(media_type)["genres"]
    ]

