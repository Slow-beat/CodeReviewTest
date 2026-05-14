import src.storage as storage


def share_task(task_id: int, actor_id: str, target_user_ids, message: str):
    task = storage.TASKS[task_id]
    share_targets = list(target_user_ids or [])

    history = task.setdefault("share_history", [])
    history.append(
        {
            "actor_id": actor_id,
            "targets": share_targets,
            "message": message,
        }
    )

    task["shared_with"] = share_targets
    task["last_share_message"] = message

    return {
        "task": {
            "id": task["id"],
            "title": task["title"],
            "shared_with": task.get("shared_with", []),
            "last_share_message": task.get("last_share_message", ""),
        },
        "share_count": len(history),
        "shared_by": actor_id,
    }
