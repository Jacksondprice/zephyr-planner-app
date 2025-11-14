"""Reminders helpers for internal support ticket triage."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def reminders_step_0(records: list[dict], limit: int = 290) -> list[dict]:
    """Apply reminders rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def reminders_step_1(records: list[dict], limit: int = 37) -> list[dict]:
    """Apply reminders rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def reminders_step_2(records: list[dict], limit: int = 19) -> list[dict]:
    """Apply reminders rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def reminders_step_3(records: list[dict], limit: int = 395) -> list[dict]:
    """Apply reminders rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def reminders_step_4(records: list[dict], limit: int = 49) -> list[dict]:
    """Apply reminders rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def reminders_step_5(records: list[dict], limit: int = 261) -> list[dict]:
    """Apply reminders rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("reminders step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
