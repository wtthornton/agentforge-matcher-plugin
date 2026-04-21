"""AgentForge plugin entry point for agentforge-matcher-plugin.

`register(app)` is called by `PluginRegistry.register_plugin()`:
1. Mounts the matcher-test router onto the host FastAPI app.
2. Loads all three domain agents (fruits, vehicles, weather) into the host's
   AgentLoader using an absolute path derived from this file's location.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI

logger = logging.getLogger(__name__)

# Pass the agents/ parent directory so load_external scans all agent subdirs.
_AGENTS_DIR = Path(__file__).parent / "agents"
_NAMESPACE = "project.matcher-test"


def register(app: FastAPI) -> None:
    from agentforge_matcher_test.routes import router

    app.include_router(router)

    agent_loader = getattr(app.state, "agent_loader", None)
    if agent_loader is None:
        logger.debug(
            "matcher-test plugin: no agent_loader on app.state — skipping agent load"
        )
        return

    try:
        newly_loaded = agent_loader.load_external(_AGENTS_DIR, _NAMESPACE)
        logger.info(
            "matcher-test plugin: loaded %d agent(s) from %s",
            len(newly_loaded),
            _AGENTS_DIR,
        )
    except Exception:
        logger.exception("matcher-test plugin: agent load failed")
