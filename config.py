import os
import logging

# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'SlackV3'

BOT_IDENTITY = {
    'token': os.environ['SLACK_TOKEN'],
}

BOT_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
BOT_EXTRA_PLUGIN_DIR = os.path.join(os.path.dirname(__file__), "plugins")

BOT_LOG_FILE = os.path.join(os.path.dirname(__file__), "errbot.log")
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = (f"@{os.getenv('ADMIN', 'yuri')}", )
