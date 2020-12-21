# -*- coding: utf-8 -*-


"""
The Rest7 API interface.
"""


from contextlib import closing
from json import loads
from urllib.parse import quote_plus
from urllib.request import urlopen


class Rest7API:
    """
    The Rest7 API.
    """

    def __init__(self):
        self.logger = None
        self._base_url = 'http://api.rest7.com/v1/movie_info.php'

    def search(self, title, year):
        """
        Search for a movie : http://api.rest7.com/v1/movie_info.php?title=oblivion

        :param title: Movie title
        :type title: unicode
        :param year: Year of release
        :type year: int
        :return: IMDB identifier
        :rtype: unicode
        """



        self.logger.debug('Looking for {0} ({1})'.format(title, year))

        # url = u'{0}/?t={1}&y={2}'.format(self._base_url, quote_plus(title), year)
        url = '{0}?title={1}'.format(self._base_url, quote_plus(title))
        with closing(urlopen(url)) as f:
            response = loads(f.read())
            # response=f.read()

        # response is a list of films, we have to filter by date
        # print 'DEBUGGGING'
        print(response)
        print(response['success'])

        # if not response.get('Response', u'False') == u'True':
        if not response['success'] :
            self.logger.warn('No match found for {0} ({1})'.format(title, year))
            return None

        match = None
        for mv in response['movies'] : 
            if mv['year'] == year : 
                match=mv
                break
        print(match)

        imdb_id = match['imdb']
        # print imdb_id
        self.logger.debug('IMDB identifier {2} found for {0} ({1})'.format(title, year, imdb_id))

        return imdb_id
