"""
Common types
"""

from enum import Enum, StrEnum
from typing import TypedDict


class CustomEnum(StrEnum):
    """
    A customized enum class
    """
    @property
    def value(self):
        """
        Return lower case of value
        """
        return self.lower()

    def __str__(self):
        return self._value_

    @classmethod
    def get(cls, val, default=None):
        """
        Convert string to enum
        """
        for item in cls._member_map_.values():
            if val == item.value.lower():
                return item
        return default


class MediaType(CustomEnum):
    MOVIE = "Movie"
    TV = "TV"


class TrendingMediaType(CustomEnum):
    MOVIE = "Movie"
    TV = "TV"
    PERSON = "Person"
    ALL = "All"


class TrendingTimeWindow(Enum):
    DAY = "day"
    WEEK = "week"


class Company(TypedDict):
    id: int
    logo_path: str
    name: str
    origin_country: str


class Country(TypedDict):
    iso_3166_1: str
    name: str


class SpokenLanguage(TypedDict):
    english_name: str
    iso_639_1: str
    name: str


class Episode(TypedDict):
    id: int
    name: str
    overview: str
    vote_average: float
    vote_count: int
    air_date: str
    episode_number: int
    production_code: str
    runtime: int
    season_number: int
    show_id: int
    still_path: str


class Network(TypedDict):
    id: int
    logo_path: str
    name: str
    origin_country: str


class Person(TypedDict):
    id: int
    credit_id: str
    name: str
    gender: int
    profile_path: str



