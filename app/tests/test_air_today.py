import pytest
import requests.exceptions
from pytest_mock import MockerFixture

from app.models import TV, get_air_today_list


@pytest.fixture
def mock_data():
    return {
        "page": 1,
        "results": [
            {
                "adult": False,
                "backdrop_path": "/jWXrQstj7p3Wl5MfYWY6IHqRpDb.jpg",
                "genre_ids": [
                    10763
                    ],
                "id": 94722,
                "origin_country": [
                    "DE"
                    ],
                "original_language": "de",
                "original_name": "Tagesschau",
                "overview": "German daily news program, the oldest still "
                            "existing program on German television.",
                "popularity": 3422.186,
                "poster_path": "/7dFZJ2ZJJdcmkp05B9NWlqTJ5tq.jpg",
                "first_air_date": "1952-12-26",
                "name": "Tagesschau",
                "vote_average": 7.02,
                "vote_count": 179
                },
            {
                "adult": False,
                "backdrop_path": "/218ZehBKlH8efPRRccmB7bu0oLQ.jpg",
                "genre_ids": [
                    35,
                    9648,
                    10766,
                    18
                    ],
                "id": 219109,
                "origin_country": [
                    "BR"
                    ],
                "original_language": "pt",
                "original_name": "Elas por Elas",
                "overview": "Seven friends who met in their youth at an "
                            "English "
                            "course meet again 25 years later; Lara, Taís, "
                            "Helena, Adriana, Renée, Natália and Carol, "
                            "each of "
                            "them has a different personality and origin, "
                            "but they share a deep affection.",
                "popularity": 3203.847,
                "poster_path": "/m0cvvnhnRXdQhLARx7qt9lz7hTE.jpg",
                "first_air_date": "2023-09-25",
                "name": "Elas por Elas",
                "vote_average": 6.19,
                "vote_count": 21
                },
            {
                "adult": False,
                "backdrop_path": "/aWPhMZ0P2DyfWB7k5NXhGHSZHGC.jpg",
                "genre_ids": [
                    18,
                    80,
                    10766
                    ],
                "id": 209265,
                "origin_country": [
                    "BR"
                    ],
                "original_language": "pt",
                "original_name": "Terra e Paixão",
                "overview": "When her husband is killed in a land grabbing "
                            "attempt, Aline takes charge of cultivating his "
                            "land "
                            "and protecting his family. Facing the powerful "
                            "Antonio La Selva, responsible for the death of "
                            "her "
                            "husband and the largest landowner in the region, "
                            "Aline is determined to keep possession of her "
                            "land "
                            "and invest in its production. However, "
                            "she didn't "
                            "expect that she would fall in love with Daniel, "
                            "son of her rival, who is at odds with his "
                            "rebellious half-brother, Caio, who, in turn, "
                            "also falls in love with the girl. In the "
                            "interior "
                            "of Brazil, Aline will have to fight two battles: "
                            "the dispute for her lands and for her heart.",
                "popularity": 2181.77,
                "poster_path": "/33HrrOZQKRp7W3dNXPmKB0udA2m.jpg",
                "first_air_date": "2023-05-08",
                "name": "Land of Desire",
                "vote_average": 6.606,
                "vote_count": 126
                },
            ],
        "total_pages": 11,
        "total_results": 202
        }


@pytest.fixture
def air_today(mocker: MockerFixture, mock_data):
    mocker.patch("app.models.get_air_today", return_value=mock_data)
    return get_air_today_list()


def test_fetch_list(air_today):
    assert len(air_today) == 3


def test_fetch_tv(air_today):
    assert type(air_today[0]) is TV


def test_air_today_connection_error(mocker: MockerFixture):
    mocker.patch('requests.get',
                 side_effect=requests.exceptions.ConnectionError())
    res = get_air_today_list()
    assert res == []


def test_air_today_bad_status_code(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 500
    res = get_air_today_list()
    assert res == []


def test_air_today_bad_status(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 200
    m.return_value.json.return_value = {
        'status': 'error',
        'message': 'some errors'
        }
    res = get_air_today_list()
    assert res == []
