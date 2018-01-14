#!/usr/bin/env python
"""
yahoo_news module
This module processes news rss feed from yahoo.
It uses thethe free rss feed
"""

import feedparser
from unidecode import unidecode

class YahooNews(object):  # added object base class for python2 compatibility.
    """
    The Yahoo_news class handles getting and processing the news feeed
    """
    __YAHOO_NEWS_URL = 'https://uk.news.yahoo.com/rss'

    def __init__(self, limit = None):
        self._feed = None
        self._iterator = None
        self._index = 1
        self.update()
        if limit:
            self._limit = limit
        else:
            self._limit = max(self._feed)

    def update(self):
        self._feed = feedparser.parse(self.__YAHOO_NEWS_URL)
        self._iterator = iter(self._feed['entries'])

    def news(self):
        return self._feed

    def __iter__(self):
        return self

    def __next__(self):
        story = None

        if self._index <= self._limit:
            story = self._iterator.__next__()
            self._index += 1
        else:
            raise StopIteration
        return story

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    news_feed = YahooNews(3)
    feed = news_feed.news()
    # for key in feed["entries"]:
    #         print(unidecode(key["title"]))

    for news_item in news_feed:
        print(news_item['title'])

if __name__ == "__main__":
    main()
