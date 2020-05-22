#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jesse'
SITENAME = 'Coffee With Code'
SITEURL = ''

PATH = 'content'
THEME = 'theme/coffee'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About the author', 'https://jldohmann.netlify.app/about.html'),
         ('Blog home', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/fourierfiend'),
          ('LinkedIn', 'https://linkedin.com/in/jldohmann'),
          ('GitHub', 'https://github.com/jldohmann'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True