from __future__ import annotations

from fastapi import APIRouter, Query

from db import ensure_view, get_video_list, query_boxes, query_next_hit, query_prev_hit, query_timeline
from templates import render_index

router = APIRouter()


@router.get("/")
def index():
    return render_index()


@router.get("/api/videos")
def api_videos():
    return get_video_list()


@router.get("/api/videos/{video_id}/boxes")
def api_boxes(video_id: str, frame: int = Query(..., ge=0)):
    view = ensure_view(video_id)
    return query_boxes(view, frame)


@router.get("/api/videos/{video_id}/timeline")
def api_timeline(video_id: str, bin_sec: int = Query(1, ge=1, le=60)):
    view = ensure_view(video_id)
    counts = query_timeline(view, bin_sec)
    return {"bin_sec": bin_sec, "counts": counts}


@router.get("/api/videos/{video_id}/next_hit")
def api_next_hit(video_id: str, frame: int = Query(..., ge=0)):
    view = ensure_view(video_id)
    next_frame = query_next_hit(view, frame)
    return {"frame": next_frame}


@router.get("/api/videos/{video_id}/prev_hit")
def api_prev_hit(video_id: str, frame: int = Query(..., ge=0)):
    view = ensure_view(video_id)
    prev_frame = query_prev_hit(view, frame)
    return {"frame": prev_frame}
