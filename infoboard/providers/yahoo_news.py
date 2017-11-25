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

    def __init__(self):
        self._feed = None
        self.update()

    def update(self):
        self._feed = feedparser.parse(self.__YAHOO_NEWS_URL)
        for key in self._feed["entries"]:
            print(unidecode(key["title"]))

    def news(self):
        return self._feed

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    news_feed = YahooNews()

if __name__ == "__main__":
    main()
