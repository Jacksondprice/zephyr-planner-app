"""Webhooks helpers for internal support ticket triage."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def webhooks_step_0(records: list[dict], limit: int = 135) -> list[dict]:
    """Apply webhooks rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_1(records: list[dict], limit: int = 382) -> list[dict]:
    """Apply webhooks rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_2(records: list[dict], limit: int = 90) -> list[dict]:
    """Apply webhooks rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_3(records: list[dict], limit: int = 267) -> list[dict]:
    """Apply webhooks rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_4(records: list[dict], limit: int = 384) -> list[dict]:
    """Apply webhooks rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_5(records: list[dict], limit: int = 457) -> list[dict]:
    """Apply webhooks rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_6(records: list[dict], limit: int = 91) -> list[dict]:
    """Apply webhooks rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_7(records: list[dict], limit: int = 344) -> list[dict]:
    """Apply webhooks rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_8(records: list[dict], limit: int = 248) -> list[dict]:
    """Apply webhooks rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_9(records: list[dict], limit: int = 309) -> list[dict]:
    """Apply webhooks rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_10(records: list[dict], limit: int = 39) -> list[dict]:
    """Apply webhooks rule 10 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 10 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
