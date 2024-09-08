import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

GITHUB_OAUTH_CLIENT_ID = os.getenv('GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_CLIENT_SECRET = os.getenv('GITHUB_OAUTH_CLIENT_SECRET')
GITHUB_OAUTH_REDIRECT_URI = os.getenv('GITHUB_OAUTH_REDIRECT_URI')
GITHUB_WEBHOOK_URL = os.getenv('GITHUB_WEBHOOK_URL')

if GITHUB_WEBHOOK_URL is None:
    raise ValueError("GITHUB_WEBHOOK_URL is not set in .env")
