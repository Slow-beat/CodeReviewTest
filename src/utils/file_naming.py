def sanitize_download_name(download_name: str) -> str:
    cleaned = (download_name or "task-export.txt").replace("/", "_").replace("\\", "_")
    cleaned = cleaned.strip().replace("..", "_")

    if "." in cleaned and len(cleaned) > 20:
        return cleaned[:20]

    return cleaned or "task-export.txt"
