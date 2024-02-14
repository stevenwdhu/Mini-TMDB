"""
Model generators
"""

from app.api.air_today import get_air_today
from app.api.detail import get_detail, get_credit
from app.api.search import get_search
from app.api.trending import get_trending
from app.common.types import TrendingMediaType, TrendingTimeWindow, MediaType
from .credit import Credit, Cast, Crew
from .media import Media
from .movie import Movie
from .movie_detail import MovieDetail
from .tv import TV
from .tv_detail import TVDetail, Season


def get_trending_list(
        media_type: TrendingMediaType = TrendingMediaType.ALL,
        time_window: TrendingTimeWindow = TrendingTimeWindow.DAY,
        ) -> list[Media]:
    """
    Get a list of trending media
    """
    return [
        Movie(**media)
        if media["media_type"] == MediaType.MOVIE.value
        else TV(**media)
        for media in get_trending(media_type, time_window).get("results", [])
        ]


def get_air_today_list() -> list[TV]:
    """
    Get a list of tv shows that air today
    """
    return [
        TV(**tv, media_type=MediaType.TV)
        for tv in get_air_today().get("results", [])
        ]


def get_movie_detail(movie_id: int):
    """
    Get detail information of a movie by id
    """
    detail_res = get_detail(MediaType.MOVIE, movie_id)
    credit_res = get_credit(MediaType.MOVIE, movie_id)
    if detail_res:
        return MovieDetail(
            **detail_res,
            media_type=MediaType.MOVIE,
            credits=Credit(
                id=movie_id,
                cast=[Cast(**c) for c in credit_res.get("cast", [])],
                crew=[Crew(**c) for c in credit_res.get("crew", [])],
                )
            )


def get_tv_detail(tv_id: int):
    """
    Get detail information of a tv show by id
    """
    detail_res = get_detail(MediaType.TV, tv_id)
    credit_res = get_credit(MediaType.TV, tv_id)
    if detail_res:
        detail_res['seasons'] = [Season(**s) for s in
                                 detail_res.get('seasons', [])]
        return TVDetail(
            **detail_res,
            media_type=MediaType.TV,
            credits=Credit(
                id=tv_id,
                cast=[Cast(**c) for c in credit_res.get("cast", [])],
                crew=[Crew(**c) for c in credit_res.get("crew", [])],
                )
            )


def get_search_list(query: str, media_type: MediaType = MediaType.MOVIE):
    """
    Get a list of search result by query
    """
    if len(query) > 0:
        if media_type == MediaType.MOVIE:
            return [
                Movie(**movie, media_type=MediaType.MOVIE)
                for movie in get_search(query, media_type).get("results", [])
                ]
        if media_type == MediaType.TV:
            return [
                TV(**tv, media_type=MediaType.TV)
                for tv in get_search(query, media_type).get("results", [])
                ]
    return []
