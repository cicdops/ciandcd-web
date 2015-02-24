#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'itech001'
AUTHORS = u'itech001'
SITENAME = u'ciandcd'
SITEURL = 'http://www.ciandcd.com'
SITESUBTITLE = 'continuous integration and continuous delivery'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
READERS = {'html': None}
STATIC_PATHS = ['images', 'extra/CNAME']
# path-specific metadata
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
    }

#theme
#https://github.com/getpelican/pelican-themes/tree/master/gum
THEME = "themes/bootstrap-ciandcd"

#disqus
DISQUS_SITENAME = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('GITHUB', 'https://github.com/ciandcd'),
          )
GITHUB_URL = 'https://github.com/ciandcd'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#google analytices
GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITENAME = ''
GOOGLE_ANALYTICS_UNIVERSAL = ''
