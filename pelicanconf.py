#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###############################################################################
## Site
SITEURL = 'http://localhost:8000'
SITENAME = u'Tohuw.Net'
TITLE = 'Tohuw.Net'
AUTHOR = u'Ron Scott-Adams'
SITESUBTITLE = 'Elucidating Systems Architecture, Operations, & Yak Shaving'
###############################################################################
## Logging
# LOG_FILTER = [
#               (logging.WARN, 'Feeds generated without SITEURL set properly may not be valid')
#              ]
###############################################################################
## Caching
CACHE_PATH = 'cache'
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = False
AUTORELOAD_IGNORE_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'
GZIP_CACHE = True
###############################################################################
## Locale
DEFAULT_LANG = u'en'
LOCALE = ( 'en_US', )
DEFAULT_DATE_FORMAT = '%B %d, %Y'
# DATE_FORMATS = { 'en': '%a, %d %b %Y', }
TIMEZONE = 'America/New_York'
DEFAULT_DATE = None
###############################################################################
## Paths
PATH = 'content'
THEME = 'themes/qalal'
# JINJA_EXTENSIONS = []
# JINJA_FILTERS = { 'urlencode': urlencode_filter }
THEME_STATIC_DIR = ''
THEME_STATIC_PATHS = [ 'static' ]
CSS_FILE = 'main.css'

OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False
WRITE_SELECTED = []
# OUTPUT_RETENTION = ( ".git", )
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
IGNORE_FILES = [ '.*' ]

DIRECT_TEMPLATES = ((
                        'index',
                        'tags',
                        'categories',
                        'archives',
                        'authors',
                        'search'
                    ))
# TEMPLATE_PAGES = {
#                       'src/books.html': 'dest/books.html',
#                       'src/resume.html': 'dest/resume.html',
#                       'src/contact.html': 'dest/contact.html'
#                   }
# EXTRA_TEMPLATES_PATHS = []
ARTICLE_EXCLUDES = [ 'extras' ]
PAGE_EXCLUDES = [ 'extras' ]
STATIC_PATHS = [
                    'extras',
                    'images',
                    'comments'
               ]
# STATIC_EXCLUDES = []
STATIC_EXCLUDE_SOURCES = True
# READERS = { 'html': None }

SLUGIFY_SOURCE = 'title'
SLUG_SUBSTITUTIONS = [('and', '')]

ARTICLE_URL = '/articles/{slug}'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
ARTICLE_ORDER_BY = 'slug'

INDEX_SAVE_AS = 'articles.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = ''
NEWEST_FIRST_ARCHIVES = True

DRAFT_URL = '/drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = '{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = '{slug}-{lang}.html'
WITH_FUTURE_DATES = False

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_ORDER_BY = 'basename'

CATEGORIES_SAVE_AS = 'topics/index.html'
CATEGORY_URL = '/topics/{slug}'
CATEGORY_SAVE_AS = 'topics/{slug}.html'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
REVERSE_CATEGORY_ORDER = False

TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = '/tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 100

AUTHORS_SAVE_AS = 'authors.html'
AUTHOR_URL = '/author/{slug}'
AUTHOR_SAVE_AS = '/author/{slug}.html'
###############################################################################
## Metadata
# DEFAULT_METADATA = ()
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
# PATH_METADATA = ''
EXTRA_PATH_METADATA = { 'extras/robots.txt': {'path': 'robots.txt'}, }
SUMMARY_MAX_LENGTH = 50
###############################################################################
## Menu
MENUITEMS = (
                ('Topics', '/topics/'),
                ('Archives','/archives/'),
                ('Ron Scott-Adams', '/ron-scott-adams'),
            )
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
###############################################################################
## Links
LINKS = (
            ('<span class="links-name">HighExecutive</span> (Ruminations of my illustrious wife)', 'http://highexecutive.net'),
            ('<span class="links-name">UberMarianne</span> (My sister-in-law introspects)', 'http://ubermarianne.net'),
            ('<span class="links-name">Dadhacker</span> (An old and new school cantankerous coder)', 'http://dadhacker.com')
        )
TWITTER_USERNAME = 'tohuw'
GITHUB_URL = "https://github.com/tohuw"
SOCIAL = (
            ('<span class="fa-twitter"></span>', 'https://twitter.com/' + TWITTER_USERNAME),
            ('<span class="fa-linkedin"></span>', 'https://linkedin.com/in/tohuw'),
            ('<span class="fa-github"></span>', GITHUB_URL)
        )
###############################################################################
## Linkification
RELATIVE_URLS = False
# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
###############################################################################
## Pagination
DEFAULT_PAGINATION = False
# PAGINATED_DIRECT_TEMPLATES = ( 'index', )
DEFAULT_ORPHANS = 3
# PAGINATION_PATTERNS = (
#                           (1, '{base_name}/', '{base_name}/index'),
#                           (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index'),
#                       )
###############################################################################
## Feeds
FEED_DOMAIN = SITEURL
#FEED_MAX_ITEMS =

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = None
FEED_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_RSS = None
###############################################################################
## Plugins/Extensions
PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = [
            'tipue_search',
            'better_figures_and_images'
          ]
TYPOGRIFY = True
# TYPOGRIFY_IGNORE_TAGS = []
MD_EXTENSIONS = [
                   'codehilite(css_class=highlight)',
                   'extra',
                   'admonition',
                 ]
# DOCUTILS_SETTINGS = {}
# PYGMENTS_RST_OPTIONS = []
RESPONSIVE_IMAGES = True
###############################################################################
## Comments
# DISQUS_SITENAME = 'tohuw'

ISSO_ENABLED = True
ISSO_URL = 'localhost:8001'
# ISSO_LANG =
ISSO_DEFAULT_STYLE = False
ISSO_REPLY_TO_SELF = True
ISSO_MAX_COMMENTS_TOP = 'inf'
ISSO_MAX_COMMENTS_NESTED = 'inf'
ISSO_REVEAL_ON_CLICK = 'inf'
ISSO_AVATARS = True
# ISSO_AVATAR_BG =
# ISSO_AVATAR_FG =
ISSO_VOTING = True
###############################################################################
## Analytics
#GOOGLE_ANALYTICS =
#GOSQUARED_SITENAME =
# PIWIK_URL =
# PIWIK_SSL_URL =
# PIWIK_SITE_ID =
###############################################################################
## Qalal-Specific Settings
ARTICLES_RECENT_TITLE = 'More, Here'
ARTICLES_SHOW_RECENT = True
ARTICLE_SHOW_DATE = True
ARTICLE_SHOW_EDITINFO = True
ARTICLE_SHOW_AUTHORS = True
ARTICLE_SHOW_CATEGORY = True
ARTICLE_SHOW_TAGS = True
ARTICLE_SHOW_SHARE = False
PAGE_SHOW_EDITINFO = True
CUSTOM_AUTHOR_URL = '/ron-scott-adams'
LINKS_TITLE = 'More, Elsewhere'
SOCIAL_TITLE = False
FEED_TITLE = '<span class="fa-rss"></span>'
TIPUE_SEARCH_ENABLED = 'tipue_search' in PLUGINS
