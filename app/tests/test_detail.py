import pytest
import requests
from pytest_mock import MockerFixture

from app.models import get_movie_detail, get_tv_detail, Credit
from app.models.movie_detail import MovieDetail
from app.models.tv_detail import TVDetail


@pytest.fixture
def movie_detail_mock_data():
    return {
        "adult": False,
        "backdrop_path": "/rLb2cwF3Pazuxaj0sRXQ037tGI1.jpg",
        "belongs_to_collection": None,
        "budget": 100000000,
        "genres": [{"id": 18, "name": "Drama"}, {"id": 36, "name": "History"}],
        "homepage": "http://www.oppenheimermovie.com",
        "id": 872585,
        "imdb_id": "tt15398776",
        "original_language": "en",
        "original_title": "Oppenheimer",
        "overview": "The story of J. Robert Oppenheimer's role in the "
                    "development of the atomic bomb during World War II.",
        "popularity": 1766.305,
        "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "production_companies": [
            {
                "id": 9996,
                "logo_path": "/3tvBqYsBhxWeHlu62SIJ1el93O7.png",
                "name": "Syncopy",
                "origin_country": "GB",
                },
            {
                "id": 33,
                "logo_path": "/8lvHyhjr8oUKOOy2dKXoALWKdp0.png",
                "name": "Universal Pictures",
                "origin_country": "US",
                },
            {
                "id": 507,
                "logo_path": "/aRmHe6GWxYMRCQljF75rn2B9Gv8.png",
                "name": "Atlas Entertainment",
                "origin_country": "US",
                },
            ],
        "production_countries": [
            {"iso_3166_1": "GB", "name": "United Kingdom"},
            {"iso_3166_1": "US", "name": "United States of America"},
            ],
        "release_date": "2023-07-19",
        "revenue": 950200000,
        "runtime": 181,
        "spoken_languages": [
            {"english_name": "Dutch", "iso_639_1": "nl", "name": "Nederlands"},
            {"english_name": "English", "iso_639_1": "en", "name": "English"},
            ],
        "status": "Released",
        "tagline": "The world forever changes.",
        "title": "Oppenheimer",
        "video": False,
        "vote_average": 8.16,
        "vote_count": 4918,
        }


@pytest.fixture
def movie_credits_mock_data():
    return {
        "id": 872585,
        "cast": [
            {
                "adult": False,
                "gender": 2,
                "id": 2037,
                "known_for_department": "Acting",
                "name": "Cillian Murphy",
                "original_name": "Cillian Murphy",
                "popularity": 68.756,
                "profile_path": "/dm6V24NjjvjMiCtbMkc8Y2WPm2e.jpg",
                "cast_id": 3,
                "character": "J. Robert Oppenheimer",
                "credit_id": "613a940d9653f60043e380df",
                "order": 0
                },
            {
                "adult": False,
                "gender": 1,
                "id": 5081,
                "known_for_department": "Acting",
                "name": "Emily Blunt",
                "original_name": "Emily Blunt",
                "popularity": 53.751,
                "profile_path": "/xDc01ud6ZtaJFQWg8YfffFlUBdY.jpg",
                "cast_id": 161,
                "character": "Kitty Oppenheimer",
                "credit_id": "6328c918524978007e9f1a7f",
                "order": 1
                },
            {
                "adult": False,
                "gender": 2,
                "id": 1892,
                "known_for_department": "Acting",
                "name": "Matt Damon",
                "original_name": "Matt Damon",
                "popularity": 86.407,
                "profile_path": "/At3JgvaNeEN4Z4ESKlhhes85Xo3.jpg",
                "cast_id": 108,
                "character": "Leslie Groves",
                "credit_id": "6328ad9843250f00830efdca",
                "order": 2
                }],
        "crew": [
            {
                "adult": False,
                "gender": 2,
                "id": 282,
                "known_for_department": "Production",
                "name": "Charles Roven",
                "original_name": "Charles Roven",
                "popularity": 4.834,
                "profile_path": "/4uJLoVstC1CBcArXFOe53N2fDr1.jpg",
                "credit_id": "6162d88a18b75100298fcb24",
                "department": "Production",
                "job": "Producer"
                },
            {
                "adult": False,
                "gender": 2,
                "id": 525,
                "known_for_department": "Directing",
                "name": "Christopher Nolan",
                "original_name": "Christopher Nolan",
                "popularity": 28.205,
                "profile_path": "/xuAIuYSmsUzKlUMBFGVZaWsY3DZ.jpg",
                "credit_id": "613a93cbd38b58005f6a1964",
                "department": "Directing",
                "job": "Director"
                },
            {
                "adult": False,
                "gender": 2,
                "id": 525,
                "known_for_department": "Directing",
                "name": "Christopher Nolan",
                "original_name": "Christopher Nolan",
                "popularity": 28.205,
                "profile_path": "/xuAIuYSmsUzKlUMBFGVZaWsY3DZ.jpg",
                "credit_id": "6140dd58aaf89700421a6dd1",
                "department": "Production",
                "job": "Producer"
                }]
            
        }


@pytest.fixture
def tv_detail_mock_data():
    return {
        "adult": False,
        "backdrop_path": "/2meX1nMdScFOoV4370rqHWKmXhY.jpg",
        "created_by": [
            {
                "id": 1294471,
                "credit_id": "61235265886348007e36f84c",
                "name": "Hwang Dong-hyuk",
                "gender": 2,
                "profile_path": "/xyr3b04ayyJtA5ZN3L0Af10WKIR.jpg",
                }
            ],
        "episode_run_time": [],
        "first_air_date": "2021-09-17",
        "genres": [
            {"id": 10759, "name": "Action & Adventure"},
            {"id": 9648, "name": "Mystery"},
            {"id": 18, "name": "Drama"},
            ],
        "homepage": "https://www.netflix.com/title/81040344",
        "id": 93405,
        "in_production": False,
        "languages": ["en", "ko", "ur"],
        "last_air_date": "2021-09-17",
        "last_episode_to_air": {
            "id": 3222798,
            "name": "One Lucky Day",
            "overview": "The final round presents another cruel test — but "
                        "this time, how it ends depends on just one player. "
                        "The game's creator steps out of the shadows.",
            "vote_average": 7.6,
            "vote_count": 81,
            "air_date": "2021-09-17",
            "episode_number": 9,
            "episode_type": "finale",
            "production_code": "",
            "runtime": 56,
            "season_number": 1,
            "show_id": 93405,
            "still_path": "/sKeQbHeEUQLyoSdopa0QXm604cz.jpg",
            },
        "name": "Squid Game",
        "next_episode_to_air": None,
        "networks": [
            {
                "id": 213,
                "logo_path": "/wwemzKWzjKYJFfCeiB57q3r4Bcm.png",
                "name": "Netflix",
                "origin_country": "",
                }
            ],
        "number_of_episodes": 9,
        "number_of_seasons": 2,
        "origin_country": ["KR"],
        "original_language": "ko",
        "original_name": "오징어 게임",
        "overview": "Hundreds of cash-strapped players accept a strange "
                    "invitation to compete in children's games—with high "
                    "stakes. But, a tempting prize awaits the victor.",
        "popularity": 342.186,
        "poster_path": "/dDlEmu3EZ0Pgg93K2SVNLCjCSvE.jpg",
        "production_companies": [
            {
                "id": 112647,
                "logo_path": None,
                "name": "Siren Pictures",
                "origin_country": "KR",
                },
            {
                "id": 203249,
                "logo_path": None,
                "name": "Firstman Studio",
                "origin_country": "KR",
                },
            ],
        "production_countries": [{"iso_3166_1": "KR", "name": "South Korea"}],
        "seasons": [
            {
                "air_date": "2021-09-17",
                "episode_count": 9,
                "id": 131977,
                "name": "Season 1",
                "overview": "",
                "poster_path": "/jlbrV1Kl4Y8pWXu12SppebRs7On.jpg",
                "season_number": 1,
                "vote_average": 8.2,
                },
            {
                "air_date": None,
                "episode_count": 0,
                "id": 287516,
                "name": "Season 2",
                "overview": "",
                "poster_path": "/yt02fUla8WSJj4FZAeZssZemxlW.jpg",
                "season_number": 2,
                "vote_average": 0,
                },
            ],
        "spoken_languages": [
            {"english_name": "English", "iso_639_1": "en", "name": "English"},
            {"english_name": "Korean", "iso_639_1": "ko", "name": "한국어/조선말"},
            {"english_name": "Urdu", "iso_639_1": "ur", "name": "اردو"},
            ],
        "status": "Returning Series",
        "tagline": "45.6 billion won is child's play",
        "type": "Scripted",
        "vote_average": 7.832,
        "vote_count": 13205,
        }


@pytest.fixture
def tv_credits_mock_data():
    return {
        "cast": [
            {
                "adult": False,
                "gender": 2,
                "id": 73249,
                "known_for_department": "Acting",
                "name": "Lee Jung-jae",
                "original_name": "Lee Jung-jae",
                "popularity": 17.601,
                "profile_path": "/3h5Cfm0X8ohWn7psZkqdNWqXAHH.jpg",
                "character": "Seong Gi-hun / 'No. 456'",
                "credit_id": "5e691b882f3b1700113ec6a7",
                "order": 0
                },
            {
                "adult": False,
                "gender": 2,
                "id": 1593672,
                "known_for_department": "Acting",
                "name": "Park Hae-soo",
                "original_name": "Park Hae-soo",
                "popularity": 13.779,
                "profile_path": "/hfejrQ8gjRWCheiKpJANajXT0xi.jpg",
                "character": "Cho Sang-woo / 'No. 218'",
                "credit_id": "5dcf6e70255dba0012da4822",
                "order": 4
                },
            {
                "adult": False,
                "gender": 1,
                "id": 3194501,
                "known_for_department": "Acting",
                "name": "Jung Ho-yeon",
                "original_name": "Jung Ho-yeon",
                "popularity": 18.731,
                "profile_path": "/5340wMwuy4mz0s0Gc6012ReldRi.jpg",
                "character": "Kang Sae-byeok / 'No. 067'",
                "credit_id": "6113c0575c56340028bc05fd",
                "order": 7
                },
            ],
        "crew": [
            {
                "adult": False,
                "gender": 2,
                "id": 2127965,
                "known_for_department": "Sound",
                "name": "Jung Jae-il",
                "original_name": "Jung Jae-il",
                "popularity": 5.166,
                "profile_path": "/a1q0hsgTTUJwaq0T3W02mi1b6Q6.jpg",
                "credit_id": "614435a7ed28b9008e9ede3f",
                "department": "Sound",
                "job": "Original Music Composer"
                },
            {
                "adult": False,
                "gender": 0,
                "id": 1294476,
                "known_for_department": "Production",
                "name": "Han Heung-seok",
                "original_name": "Han Heung-seok",
                "popularity": 1.4,
                "profile_path": '',
                "credit_id": "614ae43f2dffd80045cfebf3",
                "department": "Production",
                "job": "Producer"
                },
            {
                "adult": False,
                "gender": 0,
                "id": 1294128,
                "known_for_department": "Camera",
                "name": "Lee Hyung-deok",
                "original_name": "Lee Hyung-deok",
                "popularity": 2.159,
                "profile_path": '',
                "credit_id": "614ae45a4a4bfc0044bdc9c9",
                "department": "Camera",
                "job": "Director of Photography"
                },
            
            ],
        "id": 93405
        }


@pytest.fixture
def movie_detail(mocker: MockerFixture, movie_detail_mock_data,
                 movie_credits_mock_data):
    mocker.patch("app.models.get_detail", return_value=movie_detail_mock_data)
    mocker.patch("app.models.get_credit", return_value=movie_credits_mock_data)
    return get_movie_detail(872585)


@pytest.fixture
def tv_detail(mocker: MockerFixture, tv_detail_mock_data,
              tv_credits_mock_data):
    mocker.patch("app.models.get_detail",
                 return_value=tv_detail_mock_data)
    mocker.patch("app.models.get_credit",
                 return_value=tv_credits_mock_data)
    return get_tv_detail(94722)


def test_movie_type(movie_detail):
    assert type(movie_detail) is MovieDetail


def test_tv_type(tv_detail):
    assert type(tv_detail) is TVDetail


def test_movie_id(movie_detail, movie_detail_mock_data):
    assert movie_detail.id == movie_detail_mock_data['id']


def test_tv_id(tv_detail, tv_detail_mock_data):
    assert tv_detail.id == tv_detail_mock_data['id']


def test_movie_name(movie_detail, movie_detail_mock_data):
    assert movie_detail.title == movie_detail_mock_data['title']


def test_tv_name(tv_detail, tv_detail_mock_data):
    assert tv_detail.name == tv_detail_mock_data['name']


def test_movie_connection_error(mocker: MockerFixture):
    mocker.patch('requests.get',
                 side_effect=requests.exceptions.ConnectionError())
    res = get_movie_detail(872585)
    assert res is None


def test_movie_bad_status_code(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 500
    res = get_movie_detail(872585)
    assert res is None


def test_movie_bad_status(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 200
    m.return_value.json.return_value = {
        'status': 'error',
        'message': 'some errors'
        }
    res = get_movie_detail(872585)
    assert res is None


def test_tv_connection_error(mocker: MockerFixture):
    mocker.patch('requests.get',
                 side_effect=requests.exceptions.ConnectionError())
    res = get_tv_detail(94722)
    assert res is None


def test_tv_bad_status_code(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 500
    res = get_tv_detail(94722)
    assert res is None


def test_tv_bad_status(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 200
    m.return_value.json.return_value = {
        'status': 'error',
        'message': 'some errors'
        }
    res = get_tv_detail(94722)
    assert res is None


def test_movie_invalid_credits(mocker: MockerFixture, movie_detail_mock_data):
    mocker.patch("app.models.get_detail", return_value=movie_detail_mock_data)
    mocker.patch('app.models.get_credit', return_value={})
    res = get_movie_detail(872585)
    assert res.credits == Credit(id=872585, cast=[], crew=[])


def test_tv_invalid_credits(mocker: MockerFixture, tv_detail_mock_data):
    mocker.patch("app.models.get_detail", return_value=tv_detail_mock_data)
    mocker.patch('app.models.get_credit', return_value={})
    res = get_tv_detail(94722)
    assert res.credits == Credit(id=94722, cast=[], crew=[])
