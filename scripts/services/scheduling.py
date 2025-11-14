"""Scheduling helpers for internal support ticket triage."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def scheduling_step_0(records: list[dict], limit: int = 146) -> list[dict]:
    """Apply scheduling rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_1(records: list[dict], limit: int = 86) -> list[dict]:
    """Apply scheduling rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_2(records: list[dict], limit: int = 61) -> list[dict]:
    """Apply scheduling rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_3(records: list[dict], limit: int = 267) -> list[dict]:
    """Apply scheduling rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_4(records: list[dict], limit: int = 468) -> list[dict]:
    """Apply scheduling rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_5(records: list[dict], limit: int = 53) -> list[dict]:
    """Apply scheduling rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_6(records: list[dict], limit: int = 142) -> list[dict]:
    """Apply scheduling rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_7(records: list[dict], limit: int = 433) -> list[dict]:
    """Apply scheduling rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def scheduling_step_8(records: list[dict], limit: int = 45) -> list[dict]:
    """Apply scheduling rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("scheduling step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
