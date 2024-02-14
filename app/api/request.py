"""
Wrapper for requests
"""

import requests as req

from .const import HEADERS, BASE_URL


def _stringify_query(query: dict):
    """
    Stringify query dictionaries
    """
    return "&".join(["=".join([str(i) for i in q]) for q in query.items()])


def get(url, query=None, **kwargs):
    """
    Wrapped get method
    return empty dictionary when encountering connection errors, status code is not 200 and result is not success
    """
    if not len(url) > 0:
        return {}
    if query:
        url += f"?{_stringify_query(query)}"
    url = BASE_URL + url
    try:
        res = req.get(url, headers=HEADERS, **kwargs)
        if res.status_code != 200:
            return {}
        if not res.json().get('success', True):
            return {}
        return res.json()
    except (req.ConnectionError, req.HTTPError):
        return {}
