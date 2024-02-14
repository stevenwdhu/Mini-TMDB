import pytest

from app.api.const import POSTER_BASE_URL
from app.common.types import MediaType
from app.models import Movie, TV


@pytest.fixture
def movie_mock_data():
    return {
        "adult": False,
        "backdrop_path": "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
        "id": 872585,
        "title": "Oppenheimer",
        "original_language": "en",
        "original_title": "Oppenheimer",
        "overview": "The story of J. Robert Oppenheimer's role in the "
                    "development of the atomic bomb during World War II.",
        "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "media_type": "movie",
        "genre_ids": [18, 36],
        "popularity": 1563.034,
        "release_date": "2023-07-19",
        "video": False,
        "vote_average": 8.166,
        "vote_count": 4843,
        }


@pytest.fixture
def tv_mock_data():
    return {
        "adult": False,
        "backdrop_path": "/zHiDNFogo4l2Zod5SZigf4tuuPg.jpg",
        "id": 204082,
        "name": "Squid Game: The Challenge",
        "original_language": "en",
        "original_name": "Squid Game: The Challenge",
        "overview": 'Immersed in the world of "Squid Game," 456 real players '
                    'put their skills — and character — to the ultimate test '
                    'for a life-changing $4.56 million prize.',
        "poster_path": "/eAjXAgdjPMZH9Ugub7XYPowFoS1.jpg",
        "media_type": "tv",
        "genre_ids": [10764],
        "popularity": 395.165,
        "first_air_date": "2023-11-22",
        "vote_average": 5.735,
        "vote_count": 34,
        "origin_country": ["GB"],
        }


@pytest.fixture
def media_movie(movie_mock_data):
    return Movie(**movie_mock_data)


@pytest.fixture
def media_tv(tv_mock_data):
    return TV(**tv_mock_data)


def test_id(media_movie, movie_mock_data):
    assert media_movie.id == movie_mock_data["id"]


def test_movie_title(media_movie, movie_mock_data):
    assert media_movie.title == movie_mock_data["title"]


def test_overview(media_movie, movie_mock_data):
    assert media_movie.overview == movie_mock_data["overview"]


def test_poster_path(media_movie, movie_mock_data):
    assert (
            media_movie.poster_path
            == POSTER_BASE_URL + movie_mock_data["poster_path"]
    )


def test_media_type_movie(media_movie, movie_mock_data):
    assert media_movie.media_type == MediaType.MOVIE


def test_genre_ids(media_movie, movie_mock_data):
    assert media_movie.genre_ids == movie_mock_data["genre_ids"]


def test_release_date(media_movie, movie_mock_data):
    assert media_movie.release_date == movie_mock_data["release_date"]


def test_vote_average(media_movie, movie_mock_data):
    assert media_movie.vote_average == movie_mock_data["vote_average"]


def test_vote_count(media_movie, movie_mock_data):
    assert media_movie.vote_count == movie_mock_data["vote_count"]


def test_media_type_tv(media_tv, tv_mock_data):
    assert media_tv.media_type == MediaType.TV


def test_tv_title(media_tv, tv_mock_data):
    assert media_tv.name == tv_mock_data["name"]
