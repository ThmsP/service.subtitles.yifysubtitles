# -*- coding: utf-8 -*-


"""
The OMDb API interface.
"""


from contextlib import closing
from json import loads

import sys

try: #python3
    from urllib.request import urlopen, Request
    from urllib.parse import quote_plus
except:
    from urllib import quote_plus
    from urllib2 import urlopen, Request


class OMDbAPI:
    """
    The OMDb API.
    """

    def __init__(self, apikey):
        self.logger = None
        self.apikey = apikey
        self._base_url = "http://www.omdbapi.com/?apikey={0}".format(self.apikey)

    def search(self, title, year):
        """
        Search for a movie.

        :param title: Movie title
        :type title: unicode
        :param year: Year of release
        :type year: int
        :return: IMDB identifier
        :rtype: unicode
        """

        self.logger.debug("Looking for {0} ({1})".format(title, year))

        url = "{0}&t={1}&y={2}".format(self._base_url, quote_plus(title), year)
        req = Request(url)
        req.add_header(
            "User-Agent",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        )
        with closing(urlopen(req)) as f:
            response = loads(f.read())

        if not response.get("Response", "False") == "True":
            self.logger.debug("No match found for {0} ({1})".format(title, year))
            return None

        imdb_id = response["imdbID"]
        self.logger.debug(
            "IMDB identifier {2} found for {0} ({1})".format(title, year, imdb_id)
        )

        return imdb_id
