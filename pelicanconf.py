#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mansi Sharma'
SITENAME = 'Coderita: Let\'s Code Clear, not Clever..'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Objecting To Objects: Main Article', 'https://www.usenix.org/legacy/publications/library/proceedings/sf94/full_papers/johnson.html'),
         ('Execution in the Kingdom of Nouns', 'http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html'),
         ('Understanding Chess', 'http://www.chesscorner.com/index.html'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/mansi-sharma-617521191/'),
        ('Twitter', 'https://twitter.com/mansi035?s=09'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelicanenv/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATHS = ['../pelicanenv/pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites']

I18N_TEMPLATES_LANG = 'en'
