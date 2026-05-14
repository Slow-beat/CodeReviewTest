def validate_task_payload(payload):
    if not payload.get("title"):
        return "title is required"

    if not payload.get("owner_id"):
        return "owner_id is required"

    return None
