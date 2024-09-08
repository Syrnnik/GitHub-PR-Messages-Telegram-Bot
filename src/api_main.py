import uvicorn
from fastapi import FastAPI

from api.controller import pull_request_webhook, oauth_callback

app = FastAPI()

app.include_router(pull_request_webhook.router, prefix="/pull_request_webhook", tags=["PR Webhook"])
app.include_router(oauth_callback.router, prefix="/oauth_callback", tags=["OAuth Callback"])

if __name__ == "__main__":
    uvicorn.run("api_main:app", host="0.0.0.0", port=8080, reload=True)
