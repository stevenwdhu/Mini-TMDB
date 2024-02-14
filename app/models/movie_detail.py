"""
Movie detail model
"""
from dataclasses import dataclass

from app.common.types import MediaType
from app.models.media_detail import MediaDetail
from app.models.movie import Movie


@dataclass
class MovieDetail(MediaDetail, Movie):
    """
    Movie detail class
    """
    belongs_to_collection: str = ''
    budget: int = 0
    imdb_id: str = ''
    revenue: int = 0
    runtime: int = 0
    media_type = MediaType.MOVIE

