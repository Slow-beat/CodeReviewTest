from pathlib import Path

from src.services.task_service import get_task


EXPORT_DIR = Path("/tmp/task-exports")


def export_task(task_id: int, actor_id: str, download_name: str):
    task = get_task(task_id)
    if not task:
        raise ValueError("task not found")

    export_path = EXPORT_DIR / download_name
    export_path.parent.mkdir(parents=True, exist_ok=True)

    content = (
        f"id={task['id']}\n"
        f"title={task['title']}\n"
        f"owner_id={task['owner_id']}\n"
        f"requested_by={actor_id}\n"
    )
    export_path.write_text(content, encoding="utf-8")

    return {
        "path": str(export_path),
        "task": task,
        "requested_by": actor_id,
    }
