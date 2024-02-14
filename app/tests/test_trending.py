import pytest
import requests.exceptions
from pytest_mock import MockerFixture

from app.api.const import POSTER_BASE_URL
from app.models import get_trending_list, Movie, TV


@pytest.fixture
def mock_data():
    return {
        "page": 1,
        "results": [
            {
                "adult": False,
                "backdrop_path": "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
                "id": 872585,
                "title": "Oppenheimer",
                "original_language": "en",
                "original_title": "Oppenheimer",
                "overview": "The story of J. Robert Oppenheimer's role in the "
                            "development of the atomic bomb during World War "
                            "II.",
                "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
                "media_type": "movie",
                "genre_ids": [18, 36],
                "popularity": 1563.034,
                "release_date": "2023-07-19",
                "video": False,
                "vote_average": 8.166,
                "vote_count": 4843,
                },
            {
                "adult": False,
                "backdrop_path": "/9PqD3wSIjntyJDBzMNuxuKHwpUD.jpg",
                "id": 1075794,
                "title": "Leo",
                "original_language": "en",
                "original_title": "Leo",
                "overview": "Jaded 74-year-old lizard Leo has been stuck in "
                            "the "
                            "same Florida classroom for decades with his "
                            "terrarium-mate turtle. When he learns he only "
                            "has "
                            "one year left to live, he plans to escape to "
                            "experience life on the outside but instead gets "
                            "caught up in the problems of his anxious "
                            "students — "
                            "including an impossibly mean substitute teacher.",
                "poster_path": "",
                "media_type": "movie",
                "genre_ids": [16, 35, 10751],
                "popularity": 461.8,
                "release_date": "2023-11-11",
                "video": False,
                "vote_average": 7.836,
                "vote_count": 119,
                },
            {
                "adult": False,
                "backdrop_path": "/zHiDNFogo4l2Zod5SZigf4tuuPg.jpg",
                "id": 204082,
                "name": "Squid Game: The Challenge",
                "original_language": "en",
                "original_name": "Squid Game: The Challenge",
                "overview": 'Immersed in the world of "Squid Game," 456 real '
                            'players put their skills — and character — to '
                            'the '
                            'ultimate test for a life-changing $4.56 million '
                            'prize.',
                "poster_path": "/eAjXAgdjPMZH9Ugub7XYPowFoS1.jpg",
                "media_type": "tv",
                "genre_ids": [10764],
                "popularity": 395.165,
                "first_air_date": "2023-11-22",
                "vote_average": 5.735,
                "vote_count": 34,
                "origin_country": ["GB"],
                },
            ],
        "total_pages": 1000,
        "total_results": 20000,
        }


@pytest.fixture
def trend(mocker: MockerFixture, mock_data):
    mocker.patch("app.models.get_trending", return_value=mock_data)
    return get_trending_list()


def test_fetch_list(trend):
    assert len(trend) == 3


def test_fetch_movie(trend):
    assert type(trend[0]) is Movie


def test_fetch_tv(trend):
    assert type(trend[2]) is TV


def test_poster_path(trend, mock_data):
    assert trend[0].poster_path == POSTER_BASE_URL + mock_data['results'][0][
        'poster_path']


def test_invalid_poster_path(trend):
    assert trend[1].poster_path == "../static/img/no-poster-available.jpg"


def test_fetch_genre_list(trend):
    assert type(trend[0].genre_list[0]) is str


def test_trend_connection_error(mocker: MockerFixture):
    mocker.patch('requests.get',
                 side_effect=requests.exceptions.ConnectionError())
    res = get_trending_list()
    assert res == []


def test_trend_bad_status_code(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 500
    res = get_trending_list()
    assert res == []


def test_trend_bad_status(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 200
    m.return_value.json.return_value = {
        'status': 'error',
        'message': 'some errors'
        }
    res = get_trending_list()
    assert res == []
