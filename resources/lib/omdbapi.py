# -*- coding: utf-8 -*-


"""
The OMDb API interface.
"""


from contextlib import closing
from json import loads
from urllib import quote_plus
from urllib2 import urlopen


class OMDbAPI:
    """
    The OMDb API.
    """

    def __init__(self, apikey):
        self.logger = None
        self.apikey = apikey
        self._base_url = u'http://www.omdbapi.com/?apikey={0}'.format(self.apikey)


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

        self.logger.debug(u'Looking for {0} ({1})'.format(title, year))

        url = u'{0}&t={1}&y={2}'.format(self._base_url, quote_plus(title), year)
        with closing(urlopen(url)) as f:
            response = loads(f.read())

        if not response.get('Response', u'False') == u'True':
            self.logger.warn(u'No match found for {0} ({1})'.format(title, year))
            return None

        print("response : {0}".format(response))
        imdb_id = response['imdbID']
        self.logger.debug(u'IMDB identifier {2} found for {0} ({1})'.format(title, year, imdb_id))

        return imdb_id
