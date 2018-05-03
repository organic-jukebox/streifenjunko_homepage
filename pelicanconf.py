#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'me'
SITENAME = 'Streifenjunko'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['concerts']

# DEFAULT_LANG = 'English'
DEFAULT_LANG = 'en'
THEME = 'theme'
HIDE_SIDEBAR = True
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
LOAD_CONTENT_CACHE = False

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False

DIRECT_TEMPLATES = ['index', 'archive']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
