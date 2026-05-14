def sanitize_download_name(download_name: str) -> str:
    max_length = 20
    cleaned = (download_name or "task-export.txt").replace("/", "_").replace("\\", "_")
    cleaned = cleaned.strip().replace("..", "_")
    cleaned = cleaned or "task-export.txt"

    if len(cleaned) <= max_length:
        return cleaned

    name, dot, extension = cleaned.rpartition(".")
    if not dot:
        return cleaned[:max_length]

    suffix = f".{extension}"
    base_limit = max_length - len(suffix)
    if base_limit <= 0:
        return cleaned[:max_length]

    return f"{name[:base_limit]}{suffix}"
