"""
TV model
"""

from dataclasses import dataclass, field

from app.models.media import Media


@dataclass
class TV(Media):
    """
    TV class
    """
    name: str = ""
    original_name: str = ""
    first_air_date: str = ""
    origin_country: list[str] = field(default_factory=list)
