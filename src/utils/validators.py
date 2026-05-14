def validate_task_payload(payload):
    if not payload.get("title"):
        return "title is required"

    if not payload.get("owner_id"):
        return "owner_id is required"

    return None


def validate_export_query(query_args):
    if not query_args.get("actor_id"):
        return "actor_id is required"

    if not query_args.get("download_name"):
        return "download_name is required"

    return None
