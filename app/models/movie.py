"""
Movie model
"""

from dataclasses import dataclass

from app.models.media import Media


@dataclass
class Movie(Media):
    """
    Movie class
    """
    original_title: str = ''
    release_date: str = ''
    video: bool = False
    title: str = ''
