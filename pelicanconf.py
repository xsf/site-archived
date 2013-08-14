#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR   = u'XMPP Members'
SITENAME = u'XMPP Standards Foundation'
SITEURL  = 'http://xmpp.org'
TIMEZONE = 'Europe/London'

DELETE_OUTPUT_DIRECTORY = True
TYPOGRIFY               = True
DISPLAY_PAGES_ON_MENU   = False
DEFAULT_LANG            = u'en'
DEFAULT_PAGINATION      = 20
DEFAULT_CATEGORY        = 'post'
# GOOGLE_ANALYTICS        = ''

ARTICLE_URL     = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FEED_DOMAIN   = 'http://xmpp.org/feed'
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS  = 'rss.xml'

STATIC_PATHS  = ['images', 'js', 'css']
FILES_TO_COPY = (('robots.txt', 'robots.txt'),
                )
THEME         = 'themes/xsf'
MARKUP        = (('md',
                  'rst')
                )
# Blogroll
LINKS         =  (('XMPP Wiki', 'http://wiki.xmpp.org/'),
                 )

# Social widget
SOCIAL        = (
                )

