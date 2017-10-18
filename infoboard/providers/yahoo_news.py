"""
yahoo_news module
This module processes news rss feed from yahoo.
It uses thethe free rss feed
"""

import feedparser
from unidecode import unidecode

class Yahoo_news(object):  # added object base class for python2 compatibility.
    """
    The Yahoo_news class handles getting and processing the news feeed
    """
    __YAHOO_NEWS_URL = 'https://uk.news.yahoo.com/rss'

    def __init__(self):
        feed = feedparser.parse(self.__YAHOO_NEWS_URL)
        for key in feed["entries"]:
            print(unidecode(key["title"]))

    def __iter__(self):
        return self

    def __next__(self):

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    news_feed = Yahoo_news()

if __name__ == "__main__":
    main()