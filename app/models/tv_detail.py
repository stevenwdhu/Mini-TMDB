"""
TV detail model
"""

from dataclasses import dataclass, field
from typing import TypedDict

from app.api.const import POSTER_BASE_URL
from app.common.types import Person, Episode, Network, MediaType
from app.models.media_detail import MediaDetail
from app.models.tv import TV


class TGenre(TypedDict):
    id: int
    name: str


@dataclass
class Season:
    """
    Season class
    """
    air_date: str
    episode_count: int
    id: int
    name: str
    overview: str
    poster_path: str
    season_number: int
    vote_average: int
    
    def __post_init__(self):
        if self.poster_path:
            self.poster_path = POSTER_BASE_URL + self.poster_path
        else:
            self.poster_path = "../static/img/no-poster-available.jpg"


@dataclass
class TVDetail(MediaDetail, TV):
    """
    TV detail class
    """
    created_by: list[Person] = field(default_factory=list)
    episode_run_time: list[int] = field(default_factory=list)
    in_production: bool = False
    languages: list[str] = field(default_factory=list)
    last_air_date: str = ''
    last_episode_to_air: Episode = field(default_factory=dict)
    next_episode_to_air: str = ''
    networks: list[Network] = field(default_factory=list)
    number_of_episodes: int = 0
    number_of_seasons: int = 0
    seasons: list[Season] = field(default_factory=list)
    type: str = ''
    media_type = MediaType.TV
