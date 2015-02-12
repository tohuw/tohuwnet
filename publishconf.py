#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://tohuw.net'
LOCALE = ( 'en_US.utf8', )
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = True
PIWIK_URL = 'tohuw.net/stats'
PIWIK_SSL_URL = 'tohuw.net/stats'
PIWIK_SITE_ID = 1
ISSO_URL = '{SITEURL}/comments'
