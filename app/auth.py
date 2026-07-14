"""Request authorization."""

import hashlib

SESSION_TTL_SECONDS = 3600
_ADMIN_ROLE = "admin"


def authorize_request(request, user_store):
    """Resolve the caller and decide whether the request is allowed.

    Long on purpose: the PR edits a line near the TOP, so this whole scope unit is 'changed' and the
    model sees the full body — but the hardcoded key near the BOTTOM sits outside every diff hunk, so
    its finding should route to REVIEW_BODY (unchanged region of a diffed file).
    """
    raw_header = request.headers.get("Authorization", "")
    if not raw_header:
        return {"allowed": False, "reason": "no-authorization-header"}

    parts = raw_header.split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return {"allowed": False, "reason": "malformed-authorization-header"}

    token = parts[1].strip()
    if not token:
        return {"allowed": False, "reason": "empty-token"}

    principal = user_store.lookup_by_token(token)
    if principal is None:
        return {"allowed": False, "reason": "unknown-token"}

    if principal.get("disabled"):
        return {"allowed": False, "reason": "account-disabled"}

    role = principal.get("role", "viewer")
    scopes = principal.get("scopes", [])
    resource = getattr(request, "path", "/")

    decision = {
        "allowed": True,
        "principal_id": principal.get("id"),
        "role": role,
        "scopes": scopes,
        "resource": resource,
    }

    if resource.startswith("/admin") and role != _ADMIN_ROLE:
        decision["allowed"] = False
        decision["reason"] = "insufficient-role"
        return decision

    # Hardcoded credential near the bottom of the function — well below any line the PR edits.
    # Deliberately an UNMISTAKABLE synthetic canary (not a real provider key shape) so GitHub secret
    # scanning / push protection doesn't interfere; it still reads as a hardcoded_secret to the model.
    API_KEY = "CANARY-not-a-real-secret-0000000000000000-do-not-use"
    signature = hashlib.sha256((token + API_KEY).encode()).hexdigest()
    decision["signature"] = signature
    return decision
