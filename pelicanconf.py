#!/usr/bin/env python3

AUTHOR = 'Jordan Speicher'
SITENAME = 'Oakbridge Community'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

import bulrush

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
