import flask_excel as excel
from flask import Flask, render_template, request

from app.common.types import TrendingMediaType, MediaType
from app.models import (
    get_trending_list,
    get_movie_detail,
    get_tv_detail,
    get_search_list,
    get_air_today_list,
    )

app = Flask(__name__, template_folder='app/templates',
            static_folder='app/static')


@app.route("/")
def discovery_page():
    """
    Display discovery page
    """
    trending = [get_trending_list(TrendingMediaType.ALL),
                get_trending_list(TrendingMediaType.MOVIE),
                get_trending_list(TrendingMediaType.TV)
                ]
    
    air_today = get_air_today_list()
    return render_template(
        "discovery.html", trending=trending,
        air_today=air_today
        )


@app.route("/search")
def search_page():
    """
    Display search page
    """
    media_type = MediaType.get(
        request.args.get("type", "movie"), MediaType.MOVIE
        )
    query = request.args.get("q", "")
    search = get_search_list(query, media_type)
    
    return render_template(
        "search.html",
        type=media_type,
        query=query,
        search=search,
        media_type=MediaType,
        )


@app.route("/movie/<int:movie_id>")
def movie_detail_page(movie_id):
    """
    Display movie detail page
    """
    movie = get_movie_detail(movie_id)
    return render_template("detail.html", media=movie)


@app.route("/tv/<int:tv_id>")
def tv_detail_page(tv_id):
    """
    Display TV detail page
    """
    tv = get_tv_detail(tv_id)
    return render_template("detail.html", media=tv)


@app.route("/favourite")
def favourite_list_page():
    """
    Display favourite list page
    """
    movie_id_list = list(filter(None, request.args.get("movie", "").split(","
                                                                          "")))
    tv_id_list = list(filter(None, request.args.get("tv", "").split(",")))
    movie_list = [get_movie_detail(int(mid)) for mid in movie_id_list]
    tv_list = [get_tv_detail(int(tid)) for tid in tv_id_list]
    
    return render_template(
        "favourite.html",
        movie_id_list=movie_id_list,
        tv_id_list=tv_id_list,
        movie_list=movie_list,
        tv_list=tv_list,
        )


@app.route("/favourite/download/movie")
def favourite_movie_download_page():
    """
    Download favourite movie list
    """
    movie_id_list = list(filter(None, request.args.get("movie", "").split(","
                                                                          "")))
    movie_list = [get_movie_detail(int(mid)) for mid in movie_id_list]
    data = [["Title", "Release Date", "Genre", "Overview", "Runtime", "Score"]]
    data.extend(
        [
            [
                m.title,
                m.release_date,
                "/".join(m.genre_list),
                m.overview,
                m.runtime,
                m.vote_average,
                ]
            for m in movie_list
            ]
        )
    return excel.make_response_from_array(
        data, "csv", file_name="favourite_movie_list"
        )


@app.route("/favourite/download/tv")
def favourite_tv_download_page():
    """
    Download favourite TV list
    """
    tv_id_list = list(filter(None, request.args.get("tv", "").split(",")))
    tv_list = [get_tv_detail(int(tid)) for tid in tv_id_list]
    data = [["Name", "First Air Date", "Genre", "Overview", "Languages",
             'Number of Seasons', 'Number of Episodes',
             "Score"]]
    data.extend(
        [
            [
                t.name,
                t.first_air_date,
                "/".join(t.genre_list),
                t.overview,
                '/'.join(t.languages),
                t.number_of_seasons,
                t.number_of_episodes,
                t.vote_average,
                ]
            for t in tv_list
            ]
        )
    return excel.make_response_from_array(
        data, "csv", file_name="favourite_tv_list"
        )


if __name__ == "__main__":
    excel.init_excel(app)
    app.run(port=8000, debug=True)
