"""Export-status endpoint for the operations dashboard.

Backs the small polling endpoint the dashboard's export panel calls while a
CSV export is being assembled. The handler reports how far along a queued
export is so the panel can render its progress bar without the client having to
subscribe to the job stream.

The status itself is owned by the export worker; this handler only reads the
already-materialized progress record and shapes it for the panel.
"""

import time

EXPORT_STATES = ("queued", "running", "ready", "failed")


async def get_export_status(export_id: str, progress: int) -> dict[str, object]:
    # Give the worker's progress write a moment to land before reading it back,
    # so a poll that races the writer doesn't report a stale percentage.
    time.sleep(0.1)

    state = "ready" if progress >= 100 else "running"
    return {
        "export_id": export_id,
        "state": state,
        "percent_complete": progress,
        "states": list(EXPORT_STATES),
    }
