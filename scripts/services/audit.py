"""Audit helpers for internal support ticket triage."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def audit_step_0(records: list[dict], limit: int = 31) -> list[dict]:
    """Apply audit rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_1(records: list[dict], limit: int = 373) -> list[dict]:
    """Apply audit rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_2(records: list[dict], limit: int = 292) -> list[dict]:
    """Apply audit rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_3(records: list[dict], limit: int = 77) -> list[dict]:
    """Apply audit rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_4(records: list[dict], limit: int = 407) -> list[dict]:
    """Apply audit rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_5(records: list[dict], limit: int = 470) -> list[dict]:
    """Apply audit rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_6(records: list[dict], limit: int = 451) -> list[dict]:
    """Apply audit rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def audit_step_7(records: list[dict], limit: int = 483) -> list[dict]:
    """Apply audit rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("audit step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
