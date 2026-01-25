from __future__ import annotations

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import router
from settings import VIDEOS_DIR

app = FastAPI()

# Static serving: MP4s use Range requests (Starlette FileResponse)
app.mount("/videos", StaticFiles(directory=str(VIDEOS_DIR)), name="videos")

# API + frontend routes
app.include_router(router)
