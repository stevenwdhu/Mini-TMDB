"""
Credit model
"""

from dataclasses import dataclass

from app.api.const import POSTER_BASE_URL


@dataclass
class Cast:
    """
    Cast class
    """
    adult: bool
    gender: int
    id: int
    known_for_department: str
    name: str
    original_name: str
    popularity: float
    profile_path: str
    character: str
    credit_id: str
    order: int
    cast_id: int = 0

    def __post_init__(self):
        if self.profile_path:
            self.profile_path = POSTER_BASE_URL + self.profile_path
        else:
            self.profile_path = f"../static/img/portrait-{'female' if self.gender == 1 else 'male'}.png"


@dataclass
class Crew:
    """
    Crew class
    """
    adult: bool
    gender: int
    id: int
    known_for_department: str
    name: str
    original_name: str
    popularity: float
    profile_path: str
    credit_id: str
    department: str
    job: str

    def __post_init__(self):
        if self.profile_path:
            self.profile_path = POSTER_BASE_URL + self.profile_path
        else:
            self.profile_path = f"../static/img/portrait-{'female' if self.gender == 1 else 'male'}.png"


@dataclass
class Credit:
    """
    Credit class
    """
    id: int
    cast: list[Cast]
    crew: list[Crew]
