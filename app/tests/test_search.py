import pytest
import requests
from pytest_mock import MockerFixture

from app.models import get_search_list, Movie


@pytest.fixture
def mock_data():
    return {
        "page": 1,
        "results": [
            {
                "adult": False,
                "backdrop_path": "/mQZ0jXbTfY4RAfPPp3iuH6vtKcX.jpg",
                "genre_ids": [10770, 28, 53],
                "id": 47369,
                "original_language": "en",
                "original_title": "Avenger",
                "overview": "After his own daughter was killed in Panama in "
                            "1994, former CIA agent Calvin Dexter became a "
                            "private 'specialist' in cases which wouldn't "
                            "reach "
                            "justice trough the regular legal channels. Two "
                            "years later he accepts to find Richard 'Ricky' "
                            "Edmunds for his pa, influential rich businessman "
                            "Stephen Edmonds. Ricky for a private Canadian "
                            "war "
                            "victims charity in Bosnia and went missing. "
                            "Dexter "
                            "discovers Ricky was beaten to pulp and drowned "
                            "for "
                            "no other crime then helping street boys from the "
                            "other side by Zoran Zilic and his Serbian "
                            "paramilitary 'order'. He offers Steven to "
                            "'finish "
                            "the job' as such war criminals don't go to "
                            "trial. "
                            "But deputy CIA director Paul Devereaux cares "
                            "only "
                            "for a nuclear arms project he wants to use Zilic "
                            "for. So CIA troubleshooter Frank McBride is "
                            "ordered "
                            "to protect him and handle Dexter.",
                "popularity": 4.768,
                "poster_path": "/cEI5aazuAVJ3PcWeNM8gxYiNjmq.jpg",
                "release_date": "2006-04-09",
                "title": "Avenger",
                "video": False,
                "vote_average": 5.741,
                "vote_count": 29,
                },
            {
                "adult": False,
                "backdrop_path": "/mDfJG3LC3Dqb67AZ52x3Z0jU0uB.jpg",
                "genre_ids": [12, 28, 878],
                "id": 299536,
                "original_language": "en",
                "original_title": "Avengers: Infinity War",
                "overview": "As the Avengers and their allies have continued "
                            "to "
                            "protect the world from threats too large for any "
                            "one hero to handle, a new danger has emerged "
                            "from "
                            "the cosmic shadows: Thanos. A despot of "
                            "intergalactic infamy, his goal is to collect all "
                            "six Infinity Stones, artifacts of unimaginable "
                            "power, and use them to inflict his twisted will "
                            "on "
                            "all of reality. Everything the Avengers have "
                            "fought "
                            "for has led up to this moment - the fate of "
                            "Earth "
                            "and existence itself has never been more "
                            "uncertain.",
                "popularity": 301.947,
                "poster_path": "/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
                "release_date": "2018-04-25",
                "title": "Avengers: Infinity War",
                "video": False,
                "vote_average": 8.252,
                "vote_count": 28019,
                },
            ],
        "total_pages": 9,
        "total_results": 175,
        }


@pytest.fixture
def search(mocker: MockerFixture, mock_data):
    mocker.patch("app.models.get_search", return_value=mock_data)
    return get_search_list('avenger')


def test_fetch_list(search):
    assert len(search) == 2


def test_fetch_movie(search):
    assert type(search[0]) is Movie


def test_search_connection_error(mocker: MockerFixture):
    mocker.patch('requests.get',
                 side_effect=requests.exceptions.ConnectionError())
    res = get_search_list('avenger')
    assert res == []


def test_search_bad_status_code(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 500
    res = get_search_list('avenger')
    assert res == []


def test_search_bad_status(mocker: MockerFixture):
    m = mocker.patch('requests.get')
    m.return_value.status_code = 200
    m.return_value.json.return_value = {
        'status': 'error',
        'message': 'some errors'
        }
    res = get_search_list('avenger')
    assert res == []
