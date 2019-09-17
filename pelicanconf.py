#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Conner Swann'
SITENAME = 'Conner Swann'
SITESUBTITLE = u'Reliability Engineer'
#SITEURL = 'https://connerswann.me'
STATIC_PATHS = ['images']

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Coda Protocol', 'https://codaprotocol.org'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/yourbuddyconner'),
          ('github', 'https://github.com/yourbuddyconner'),
          ('linkedin', 'https://www.linkedin.com/in/connerswann/'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme Settings

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

THEME = "attila"
HOME_COVER = 'https://connerswann.me/images/blog-cover.jpg'
COLOR_SCHEME_CSS = 'monokai.css'
AUTHORS_BIO = {
  "conner swann": {
    "name": "Conner Swann",
    "image": "https://connerswann.me/images/conner-profile-picture.png",
    "cover": "https://connerswann.me/images/blog-cover.jpg",
    "website": "https://connerswann.me",
    "github": "yourbuddyconner",
    "twitter": "yourbuddyconner",
    "linkedin": "connerswann",
    "location": "San Francisco",
    "bio": "Software Engineer, Infrastructure Magician, Architecture Nerd </br> Core Maintainer @ Coda Protocol"
  }
}