import os

from dotenv import load_dotenv

load_dotenv()

DB_CON_STR = os.getenv('DB_CON_STR')

GITHUB_OAUTH_CLIENT_ID = os.getenv('GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_CLIENT_SECRET = os.getenv('GITHUB_OAUTH_CLIENT_SECRET')
GITHUB_OAUTH_REDIRECT_URI = os.getenv('GITHUB_OAUTH_REDIRECT_URI')

BOT_URL = os.getenv('BOT_URL')
