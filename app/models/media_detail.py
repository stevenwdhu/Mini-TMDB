"""
Media detail model
"""

from dataclasses import dataclass, field
from typing import TypedDict

from app.common.types import Company, Country, SpokenLanguage
from app.models.credit import Credit
from app.models.media import Media


class TGenre(TypedDict):
    id: int
    name: str


@dataclass
class MediaDetail(Media):
    """
    Media detail class
    The parent class of MovieDetail and TVDetail
    """
    genres: list[TGenre] = field(default_factory=list)
    homepage: str = ''
    production_companies: list[Company] = field(default_factory=list)
    production_countries: list[Country] = field(default_factory=list)
    spoken_languages: list[SpokenLanguage] = field(default_factory=list)
    status: str = ''
    tagline: str = ''
    credits: Credit = field(default_factory=Credit)
    
    @property
    def genre_list(self) -> list[str]:
        """
        Return a genre list based on genres
        """
        return [genre["name"] for genre in self.genres]
