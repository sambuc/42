#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DELETE_OUTPUT_DIRECTORY = False
RELATIVE_URLS = True
#GOOGLE_ANALYTICS = 'UA-51482621-1'
SITEURL = 'http://localhost:8000'
# End of Dev-specific

AUTHOR = u'Lionel Sambuc'
SITENAME = u'42 – Random Thoughts on Programming, OS and Everything Else.'
SITESUBTITLE = u'Random Thoughts on Programming, OS and Everything Else.'

THEME = '../pelican-themes/pelican-bootstrap3'
# Light theme
BOOTSTRAP_THEME = 'spacelab'
CUSTOM_CSS = 'theme/css/custom-spacelab.css'

# Dark theme
BOOTSTRAP_THEME = 'cyborg'
CUSTOM_CSS = 'theme/css/custom-cyborg.css'

#SITELOGO = 'images/MegaTokyo.png'
#SITELOGO_SIZE = 50
#FAVICON = 'images/favicon.png'
#CC_LICENSE = 'CC-BY-NC-SA'

# Facebook stuff
USE_OPEN_GRAPH = False
#OPEN_GRAPH_IMAGE = <relative to static image path>

COLORBOX_THEME = 'dark'
COLORBOX_PARAMS = 'transition:"none", width:"75%", height:"75%"'
COLORBOX_PARAMS = 'transition:"elastic"'

# GitHub
#GITHUB_USER = 'sambuc'
#GITHUB_REPO_COUNT = 
#GITHUB_SKIP_FORK = True
#GITHUB_SHOW_USER_LINK = True

DEFAULT_PAGINATION = 10
GALLERY_IMG_PER_ROW = 5
#RELATED_POSTS_MAX = 5
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
#RECENT_POSTS_COUNT = 5

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
#MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra'])

# Plugins used
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['related_posts', 'gallery']

# Main Settings
TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'
LOCALE = ('en_US')

# Extra Items in the top menu
#MENUITEMS = (
#              ('HOME', 'http://www.minix3.org'),
#            )

# Blogroll
LINKS =  (
          ('MINIX 3', 'http://www.minix3.org'),
          ('Ohloh', 'https://www.ohloh.net/accounts/sambuc'),
         )

# Social widget
SOCIAL = (
          #('facebook', 'https://www.facebook.com/lionel.sambuc'),
          ('linkedin', 'https://www.linkedin.com/in/lionelsambuc'),
          ('google+', 'https://plus.google.com/113198308632164585389/posts'),
          ('github', 'http://github.com/sambuc'),
          ('RSS', 'feeds/rss.xml'),
          ('Atom', 'feeds/atom.xml'),
         )

# path-specific metadata
EXTRA_PATH_METADATA = {
    'theme-extra/css/colorbox.css': {'path': 'theme/css/colorbox.css'},
    'theme-extra/css/colorbox.dark.css': {'path': 'theme/css/colorbox.dark.css'},
    'theme-extra/css/colorbox.light.css': {'path': 'theme/css/colorbox.light.css'},
    'theme-extra/css/custom-cyborg.css': {'path': 'theme/css/custom-cyborg.css'},
    'theme-extra/css/custom-spacelab.css': {'path': 'theme/css/custom-spacelab.css'},
    'theme-extra/css/images/controls.png': {'path': 'theme/css/images/controls.png'},
    'theme-extra/css/images/loading.gif': {'path': 'theme/css/images/loading.gif'},
    'theme-extra/js/i18n/jquery.colorbox-ar.js': {'path': 'theme/js/i18n/jquery.colorbox-ar.js'},
    'theme-extra/js/i18n/jquery.colorbox-bg.js': {'path': 'theme/js/i18n/jquery.colorbox-bg.js'},
    'theme-extra/js/i18n/jquery.colorbox-ca.js': {'path': 'theme/js/i18n/jquery.colorbox-ca.js'},
    'theme-extra/js/i18n/jquery.colorbox-cs.js': {'path': 'theme/js/i18n/jquery.colorbox-cs.js'},
    'theme-extra/js/i18n/jquery.colorbox-da.js': {'path': 'theme/js/i18n/jquery.colorbox-da.js'},
    'theme-extra/js/i18n/jquery.colorbox-de.js': {'path': 'theme/js/i18n/jquery.colorbox-de.js'},
    'theme-extra/js/i18n/jquery.colorbox-es.js': {'path': 'theme/js/i18n/jquery.colorbox-es.js'},
    'theme-extra/js/i18n/jquery.colorbox-et.js': {'path': 'theme/js/i18n/jquery.colorbox-et.js'},
    'theme-extra/js/i18n/jquery.colorbox-fa.js': {'path': 'theme/js/i18n/jquery.colorbox-fa.js'},
    'theme-extra/js/i18n/jquery.colorbox-fi.js': {'path': 'theme/js/i18n/jquery.colorbox-fi.js'},
    'theme-extra/js/i18n/jquery.colorbox-fr.js': {'path': 'theme/js/i18n/jquery.colorbox-fr.js'},
    'theme-extra/js/i18n/jquery.colorbox-gl.js': {'path': 'theme/js/i18n/jquery.colorbox-gl.js'},
    'theme-extra/js/i18n/jquery.colorbox-gr.js': {'path': 'theme/js/i18n/jquery.colorbox-gr.js'},
    'theme-extra/js/i18n/jquery.colorbox-he.js': {'path': 'theme/js/i18n/jquery.colorbox-he.js'},
    'theme-extra/js/i18n/jquery.colorbox-hr.js': {'path': 'theme/js/i18n/jquery.colorbox-hr.js'},
    'theme-extra/js/i18n/jquery.colorbox-hu.js': {'path': 'theme/js/i18n/jquery.colorbox-hu.js'},
    'theme-extra/js/i18n/jquery.colorbox-id.js': {'path': 'theme/js/i18n/jquery.colorbox-id.js'},
    'theme-extra/js/i18n/jquery.colorbox-it.js': {'path': 'theme/js/i18n/jquery.colorbox-it.js'},
    'theme-extra/js/i18n/jquery.colorbox-ja.js': {'path': 'theme/js/i18n/jquery.colorbox-ja.js'},
    'theme-extra/js/i18n/jquery.colorbox-kr.js': {'path': 'theme/js/i18n/jquery.colorbox-kr.js'},
    'theme-extra/js/i18n/jquery.colorbox-lt.js': {'path': 'theme/js/i18n/jquery.colorbox-lt.js'},
    'theme-extra/js/i18n/jquery.colorbox-lv.js': {'path': 'theme/js/i18n/jquery.colorbox-lv.js'},
    'theme-extra/js/i18n/jquery.colorbox-my.js': {'path': 'theme/js/i18n/jquery.colorbox-my.js'},
    'theme-extra/js/i18n/jquery.colorbox-nl.js': {'path': 'theme/js/i18n/jquery.colorbox-nl.js'},
    'theme-extra/js/i18n/jquery.colorbox-no.js': {'path': 'theme/js/i18n/jquery.colorbox-no.js'},
    'theme-extra/js/i18n/jquery.colorbox-pl.js': {'path': 'theme/js/i18n/jquery.colorbox-pl.js'},
    'theme-extra/js/i18n/jquery.colorbox-pt-br.js': {'path': 'theme/js/i18n/jquery.colorbox-pt-br.js'},
    'theme-extra/js/i18n/jquery.colorbox-ro.js': {'path': 'theme/js/i18n/jquery.colorbox-ro.js'},
    'theme-extra/js/i18n/jquery.colorbox-ru.js': {'path': 'theme/js/i18n/jquery.colorbox-ru.js'},
    'theme-extra/js/i18n/jquery.colorbox-si.js': {'path': 'theme/js/i18n/jquery.colorbox-si.js'},
    'theme-extra/js/i18n/jquery.colorbox-sk.js': {'path': 'theme/js/i18n/jquery.colorbox-sk.js'},
    'theme-extra/js/i18n/jquery.colorbox-sr.js': {'path': 'theme/js/i18n/jquery.colorbox-sr.js'},
    'theme-extra/js/i18n/jquery.colorbox-sv.js': {'path': 'theme/js/i18n/jquery.colorbox-sv.js'},
    'theme-extra/js/i18n/jquery.colorbox-tr.js': {'path': 'theme/js/i18n/jquery.colorbox-tr.js'},
    'theme-extra/js/i18n/jquery.colorbox-uk.js': {'path': 'theme/js/i18n/jquery.colorbox-uk.js'},
    'theme-extra/js/i18n/jquery.colorbox-zh-CN.js': {'path': 'theme/js/i18n/jquery.colorbox-zh-CN.js'},
    'theme-extra/js/i18n/jquery.colorbox-zh-TW.js': {'path': 'theme/js/i18n/jquery.colorbox-zh-TW.js'},
    'theme-extra/js/jquery.colorbox-min.js': {'path': 'theme/js/jquery.colorbox-min.js'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
      'images',
      'theme-extra/css',
      'theme-extra/js'
    ]

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL

FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/atom/all.xml'
CATEGORY_FEED_ATOM = 'feeds/atom/cat/%s.xml'
TAG_FEED_ATOM = 'feeds/atom/tag/%s.xml'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/rss/all.xml'
CATEGORY_FEED_RSS = 'feeds/rss/cat/%s.xml'
TAG_FEED_RSS = 'feeds/rss/tag/%s.xml'

# How files are saved and accessed from the web.
ARTICLE_URL =		'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS =	'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DAY_ARCHIVE_SAVE_AS =	'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'
MONTH_ARCHIVE_SAVE_AS =	'posts/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS =	'posts/{date:%Y}/index.html'

ARCHIVES_URL =		'posts/'
ARCHIVES_SAVE_AS =	'posts/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'