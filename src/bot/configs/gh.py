from github import Github
from github.Auth import Token

from bot.configs.env import GITHUB_WEBHOOK_URL

WEBHOOK_NAME = "web"
WEBHOOK_CONFIG = {
    "url": GITHUB_WEBHOOK_URL,
    "content_type": "json",
    # "secret": "your_secret",
    # 1 - not use SSL
    "insecure_ssl": 1,
}
WEBHOOK_EVENTS = ['pull_request']


def _get_auth(access_token: str):
    auth = Token(access_token)
    return auth


def get_user_github(access_token: str):
    auth = _get_auth(access_token)
    gh = Github(auth=auth)
    return gh


def get_user_repos_list(gh: Github):
    repos_list = [repo.full_name for repo in gh.get_user().get_repos()]
    return repos_list


def get_repo_by_name(gh: Github, repo_name: str):
    repo = gh.get_user().get_repo(repo_name)
    return repo


def get_repo_hook_by_name(gh: Github, selected_repo: str):
    repo = gh.get_repo(full_name_or_id=selected_repo)
    hooks_list = repo.get_hooks()
    for hook in hooks_list:
        webhook_url = hook.config['url']
        if webhook_url.lower() == GITHUB_WEBHOOK_URL.lower():
            return hook


def create_repo_hook(gh: Github, selected_repo: str):
    repo = gh.get_repo(full_name_or_id=selected_repo)
    hook = repo.create_hook(
        name=WEBHOOK_NAME,
        config=WEBHOOK_CONFIG,
        events=WEBHOOK_EVENTS,
        active=True,
    )
    return hook
