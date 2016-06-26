#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'itech001'
AUTHORS = u'itech001'
SITENAME = u'ciandcd'
SITEURL = 'http://ciandcd.github.io/ciandcd-web'
#SITESUBTITLE = 'continuous integration and continuous delivery'
SITESUBTITLE = '软件持续集成和持续发布 QQ群：172758282<a target="_blank" href="http://shang.qq.com/wpa/qunwpa?idkey=d15cb26237b499f41b21a6e95ddc436766a383a725106a92bd69cdf860a64d34"><img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="ciandcd.com" title="ciandcd.com"></a><a href="https://travis-ci.org/ciandcd/ciandcd-web/"><img src="https://camo.githubusercontent.com/bba1a9ccd5663588705b6df1b02e3a7dad66a36c/68747470733a2f2f7472617669732d63692e6f72672f6369616e6463642f6369616e6463642d7765622e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/ciandcd/ciandcd-web.svg?branch=master" style="max-width:100%;"></a>'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
DEFAULT_PAGINATION = 20
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_MAX_LENGTH = 0
TYPOGRIFY = False
CACHE_CONTENT = True
CACHE_PATH = 'cache'
PDF_GENERATOR = False
#READERS = {'html': None}
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra/robots.txt',]
# path-specific metadata
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'},
    }

#theme
#https://github.com/getpelican/pelican-themes/tree/master/gum
THEME = "themes/bootstrap-spacelab"

#disqus
DISQUS_SITENAME = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ATOM = None
FEED_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('itech', 'http://www.cnblogs.com/itech/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/ciandcd'),
          )
#GITHUB_URL = 'https://github.com/ciandcd'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#google analytices
GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITENAME = ''
GOOGLE_ANALYTICS_UNIVERSAL = ''


PLUGIN_PATH = ["plugins"]
PLUGINS = ["tag_cloud", "tipue_search"]

#tag_cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
