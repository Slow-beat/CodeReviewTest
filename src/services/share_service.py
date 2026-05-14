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
        "task": task,
        "share_count": len(history),
        "internal_debug": {
            "actor_id": actor_id,
            "task_owner": task["owner_id"],
        },
    }
