"""
Genre model
"""

from dataclasses import dataclass

from ..common.types import MediaType


@dataclass
class Genre:
    """
    Genre class
    """
    id: int
    name: str
    media_type: MediaType

    def __eq__(self, other: "Genre"):
        return self.id == other.id


