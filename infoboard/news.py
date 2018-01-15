#!/usr/bin/env python
"""
New module takes the new information in a news feed provider
and displays the top 3 stories.
"""
import logging
from infoboard.providers.yahoo_news import YahooNews

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class News(object):
    """
    The News class handles getting the news from a provider,
    processing and outputting stories
    """
    def __init__(self, limit=3):
        self._limit = limit
        self._feed = YahooNews(limit)
        self._index = 0

    def _process_story(self, story):
        processed = {}
        processed['Title'] = story['title']
        processed['Summary'] = story['summary']
        processed['Image'] = story['media_content'][0]
        processed['Source'] = story['source']
        processed['PublishedDate'] = story['published']
        processed['Link'] = story['link']
        return processed

    @property
    def stories(self):
        """
        Returns all the stories recieved in raw output
        """
        return self._feed

    def __iter__(self):
        return self

    def __next__(self):
        story = None

        if self._index < self._limit:
            raw_story = self._feed.__next__()
            story = self._process_story(raw_story)
            self._index += 1
        else:
            raise StopIteration

        return story
