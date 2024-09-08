import requests
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from api.config.env import GITHUB_OAUTH_CLIENT_ID, GITHUB_OAUTH_CLIENT_SECRET, GITHUB_OAUTH_REDIRECT_URI, BOT_URL
from api.repository.user import get_user_by_tg_id, create_user, update_user
from api.scheme.user import User

router = APIRouter()

TOKEN_URL = "https://github.com/login/oauth/access_token"


@router.get("")
async def oauth_callback(
    code: str,
    # State is user tg id
    state: int,
):
    token_data = {
        "client_id": GITHUB_OAUTH_CLIENT_ID,
        "client_secret": GITHUB_OAUTH_CLIENT_SECRET,
        "code": code,
        "redirect_uri": GITHUB_OAUTH_REDIRECT_URI,
        "state": state
    }
    headers = {
        "Accept": "application/json",
    }

    response = requests.post(
        url=TOKEN_URL,
        data=token_data,
        headers=headers,
    )
    response_json = response.json()

    if "access_token" in response_json:
        access_token = response_json['access_token']

        user = get_user_by_tg_id(state)
        if not user:
            user = User(
                telegram_id=state,
                github_access_token=access_token,
            )
            create_user(user)
        else:
            user.github_access_token = access_token
            update_user(user)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Authorization failed.",
        )

    return RedirectResponse(
        url=BOT_URL,
    )
