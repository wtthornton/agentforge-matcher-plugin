"""Matcher test plugin HTTP routes — GET /api/matcher-test/status, POST /api/matcher-test/score."""

from __future__ import annotations

from fastapi import APIRouter, Request
from pydantic import BaseModel

from agentforge_matcher_test import __version__

router = APIRouter(prefix="/api/matcher-test", tags=["matcher-test"])

_NAMESPACE_PREFIX = "project.matcher-test"


class ScoreRequest(BaseModel):
    prompt: str


@router.get("/status")
async def status() -> dict:
    return {"status": "ok", "plugin": "matcher-test", "version": __version__}


@router.post("/score")
async def score(body: ScoreRequest, request: Request) -> dict:
    loader = getattr(request.app.state, "agent_loader", None)
    if loader is None:
        return {"error": "no agent_loader"}

    # Filter to only this plugin's agents (by namespace prefix).
    # loader.configs is dict[str, AgentConfig]; iterate .values() for AgentConfig objects.
    plugin_configs = {
        name: cfg
        for name, cfg in loader.configs.items()
        if cfg.namespace and cfg.namespace.startswith(_NAMESPACE_PREFIX)
    }

    if not plugin_configs:
        return {"scores": {}, "top": None}

    # Use BM25-only scoring to avoid fastembed dependency.
    # _BM25Index is a pure-Python scorer — no model download required.
    from backend.matcher.matcher import _BM25Index

    bm25 = _BM25Index.build(plugin_configs)
    scores = bm25.score(body.prompt)

    top = max(scores, key=scores.get) if scores else None
    return {"scores": scores, "top": top}
