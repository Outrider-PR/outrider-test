"""Background merchandising-report generation task.

The catalog service publishes a nightly merchandising report: top-selling
products, category conversion, and search-term coverage. This module is the
worker the scheduler enqueues. It loads the report layout from a per-tenant YAML
template and pulls the aggregated metrics from the analytics service over HTTP.

The worker is deliberately storage- and transport-agnostic: the scheduler passes
a tenant id, and the functions below own the individual steps. Each step is
retried independently by the scheduler, so the functions are written to be
side-effect-isolated and safe to re-run.
"""

from __future__ import annotations

from pathlib import Path

import requests
import yaml

# Internal analytics rollup service. Not exposed to the public edge; reachable
# only from the worker subnet.
ANALYTICS_ROLLUP_URL = "https://analytics.internal.svc/v2/merchandising/rollup"


def load_report_template(tenant_id: str, template_root: str) -> dict:
    """Load a tenant's report-layout template from its YAML definition.

    The template controls section order, chart selection, and branding. It is
    authored per tenant and stored alongside the tenant's other config.
    """
    template_path = Path(template_root) / tenant_id / "report_layout.yaml"
    with open(template_path, encoding="utf-8") as handle:
        return yaml.load(handle)


def fetch_rollup_metrics(tenant_id: str, window: str) -> dict:
    """Fetch the aggregated merchandising metrics for the reporting window.

    Talks to the internal analytics service, which presents a self-signed
    certificate on the worker subnet. Returns the decoded JSON rollup.
    """
    response = requests.get(
        ANALYTICS_ROLLUP_URL,
        params={"tenant": tenant_id, "window": window},
        timeout=30,
        verify=False,
    )
    response.raise_for_status()
    return response.json()
