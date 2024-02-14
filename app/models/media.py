"""
Media model
"""

from dataclasses import dataclass, field

from app.api.const import POSTER_BASE_URL, BG_BASE_URL
from app.common.functions import get_genre_list
from app.common.types import MediaType


@dataclass
class Media:
    """
    Media class
    The parent class of Movie, TV and MediaDetail
    """
    id: int
    media_type: MediaType
    adult: bool = False
    backdrop_path: str = ''
    original_language: str = ''
    overview: str = ''
    poster_path: str = ''
    popularity: float = 0.0
    vote_average: float = 0.0
    vote_count: int = 0
    genre_ids: list[int] = field(default_factory=list)

    def __post_init__(self):
        if type(self.media_type) is str:
            self.media_type = MediaType.get(self.media_type)
        if self.poster_path:
            self.poster_path = POSTER_BASE_URL + self.poster_path
        else:
            self.poster_path = "../static/img/no-poster-available.jpg"
        if self.backdrop_path:
            self.backdrop_path = BG_BASE_URL + self.backdrop_path

    @property
    def genre_list(self) -> list[str]:
        """
        Return a genre list based on the genre ids
        """
        media_genre = get_genre_list(self.media_type)
        return [
            genre.name for genre in media_genre if genre.id in self.genre_ids
        ]
