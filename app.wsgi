#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/UNT-Hack/mason/StatTrack")

from src import app as application
application.secret_key = '12345'