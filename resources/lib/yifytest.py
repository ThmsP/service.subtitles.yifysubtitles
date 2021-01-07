# -*- coding: utf-8 -*-


from shutil import rmtree
from tempfile import mkdtemp
from .omdbapi import OMDbAPI
from .omdbapikey import apikey # This is personal, get one : http://www.omdbapi.com/
# from rest7api import Rest7API
from .yifysubtitles import YifySubtitles
from .yifysubtitles import YifySubtitlesListener
from .yifysubtitles import YifySubtitlesLogger


class TestService(YifySubtitlesListener, YifySubtitlesLogger):
    def __init__(self):
        super(TestService, self).__init__()

        self._omdbapi = OMDbAPI(apikey)
        # self._omdbapi = Rest7API()
        self._omdbapi.logger = self

        self._yifysubtitles = YifySubtitles()
        self._yifysubtitles.listener = self
        self._yifysubtitles.logger = self
        self._yifysubtitles.workdir = mkdtemp()

        self._num_subtitles_downloaded = 0
        self._num_subtitles_found = 0

    def cleanup(self):
        rmtree(self._yifysubtitles.workdir)

    def lookup(self, title, year):
        return self._omdbapi.search(title, year)

    def download(self, url, filename):
        self._num_subtitles_downloaded = 0
        self._yifysubtitles.download(url, filename)
        self.info('{0} subtitles downloaded'.format(self._num_subtitles_downloaded))

    def search(self, imdb_id, languages):
        self._num_subtitles_found = 0
        self._yifysubtitles.search(imdb_id, languages)
        self.info('{0} subtitles found'.format(self._num_subtitles_found))

    def on_subtitle_found(self, subtitle):
        self._num_subtitles_found += 1
        self.info('Found {0} subtitle {1}'.format(subtitle['language'], subtitle['filename']))
        for key in subtitle:
            self.debug('  {0}: {1}'.format(key, subtitle[key]))

    def on_subtitle_downloaded(self, path):
        self._num_subtitles_downloaded += 1
        self.info('Subtitle {0} downloaded'.format(path))

    def debug(self, message):
        print('DEBUG: {0}'.format(message))

    def info(self, message):
        print('INFO: {0}'.format(message))

    def warn(self, message):
        print('WARN: {0}'.format(message))

    def error(self, message):
        print('ERROR: {0}'.format(message))
