"""Pricing helpers for internal support ticket triage."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def pricing_step_0(records: list[dict], limit: int = 116) -> list[dict]:
    """Apply pricing rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_1(records: list[dict], limit: int = 282) -> list[dict]:
    """Apply pricing rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_2(records: list[dict], limit: int = 310) -> list[dict]:
    """Apply pricing rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_3(records: list[dict], limit: int = 219) -> list[dict]:
    """Apply pricing rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_4(records: list[dict], limit: int = 110) -> list[dict]:
    """Apply pricing rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_5(records: list[dict], limit: int = 217) -> list[dict]:
    """Apply pricing rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_6(records: list[dict], limit: int = 104) -> list[dict]:
    """Apply pricing rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_7(records: list[dict], limit: int = 394) -> list[dict]:
    """Apply pricing rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_8(records: list[dict], limit: int = 424) -> list[dict]:
    """Apply pricing rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def pricing_step_9(records: list[dict], limit: int = 444) -> list[dict]:
    """Apply pricing rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("pricing step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
