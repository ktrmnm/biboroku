#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kentaro Minami'
SITENAME = 'StatsBiboroku'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Japan'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Githubリポジトリ', 'https://github.com/ktrmnm/biboroku'),
    ('Kentaro Minami (HP)', 'https://sites.google.com/site/ktrmnm1991/home'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/ktrmnm'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = False
#DEFAULT_CATEGORY = 'stats'
#DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

#THEME = './themes/bootstrap'
THEME = './themes/foundation-default-colours'
#THEME = './themes/gum'
#THEME = './themes/pelican-bootstrap3'

# foundation-default-colours
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = True
FOUNDATION_ALTERNATE_FONTS = True
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = True
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>'
FOUNDATION_PYGMENT_THEME = 'monokai'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# gum
GITHUB_URL = ''
#GITHUB_URL = 'http://github.com/ktrmnm/'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''
