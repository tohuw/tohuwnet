#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = 'http://tohuwnet.local'
SITENAME = u'Tohuw.Net'

DEFAULT_LANG = u'en'
# LOCALE = ( 'en_US', )
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# DATE_FORMATS = { 'en': '%a, %d %b %Y', }
TIMEZONE = 'America/New_York'
DEFAULT_DATE = None

PATH = 'content'
THEME = 'themes/qalal'
# JINJA_EXTENSIONS = []
# JINJA_FILTERS = {}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
# PYGMENTS_RST_OPTIONS = []
TYPOGRIFY = True

OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False
WRITE_SELECTED = []
# OUTPUT_RETENTION = ( ".git", )
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
IGNORE_FILES = ['.*', '*.cod']
# LOG_FILTER = [(logging.WARN, 'Feeds generated without SITEURL set properly may not be valid')]

CACHE_PATH = 'cache'
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = True
AUTORELOAD_IGNORE_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'
GZIP_CACHE = True

TITLE = 'Tohuw.Net'
AUTHOR = u'Ron Scott-Adams'
SITESUBTITLE = 'tohuw {to’-hoo}: formlessness, confusion, unreality, emptiness; nothingness, place of chaos; vanity'
# DEFAULT_METADATA = ()

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))
# PAGINATED_DIRECT_TEMPLATES = ('index',)
# TEMPLATE_PAGES = {'extras/search.html': 'search.html'}
EXTRA_TEMPLATES_PATHS = []
ARTICLE_EXCLUDES = ['extras']
PAGE_EXCLUDES = ['extras']
STATIC_PATHS = [
        'extras',
        'images',
]
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
EXTRA_PATH_METADATA = { 'extras/robots.txt': {'path': 'robots.txt'}, }
SLUGIFY_SOURCE = 'title'

# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
RELATIVE_URLS = False

# MENUITEMS = ( ('Archive','/archives.html'), ('Search', '/search.html') ,)
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

SUMMARY_MAX_LENGTH = 50

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

SLUG_SUBSTITUTIONS = [('and', '')]

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = ''
NEWEST_FIRST_ARCHIVES = True

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
WITH_FUTURE_DATES = False

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_SAVE_AS = 'topics.html'
CATEGORY_URL = 'topic/{slug}.html'
CATEGORY_SAVE_AS = 'topic/{slug}.html'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
REVERSE_CATEGORY_ORDER = False

TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 100

AUTHORS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

## Comments
DISQUS_SITENAME = 'tohuw'

## Analytics
#GOOGLE_ANALYTICS =
#GOSQUARED_SITENAME =
# PIWIK_URL = 'tohuw.net/stats'
# PIWIK_SSL_URL = 'tohuw.net/stats'
# PIWIK_SITE_ID = 1

LINKS = (('HighExecutive', 'http://highexecutive.net'),
         ('Uber Marianne', 'http://ubermarianne.net'),)

SOCIAL = (('@Tohuw', 'https://twitter.com/tohuw'),
          ('LinkedIn', 'https://linkedin.com/in/tohuw'),
          ('GitHub', 'https://github.com/tohuw'))
GITHUB_URL = "https://github.com/tohuw"

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3
# PAGINATION_PATTERNS = (
#         (1, '{base_name}/', '{base_name}/index.html'),
#         (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

## Qalal-Specific Settings
ALLARTICLES_TITLE = False
ARTICLE_SHOW_MODDATE = True
ARTICLE_SHOW_SHARE = True
PAGE_SHOW_MODDATE = True
TWITTER_USERNAME = 'tohuw'
TWITTER_FEED = True
CREDITS_SHOW = True
TIPUE_SEARCH = 'tipue_search' in PLUGINS
ISSO_ENABLED = False
