import src.storage as storage


def list_tasks():
    return list(storage.TASKS.values())


def create_task(title: str, description: str, owner_id: str):
    task = {
        "id": storage.NEXT_TASK_ID,
        "title": title,
        "description": description,
        "owner_id": owner_id,
        "status": "open",
    }
    storage.TASKS[storage.NEXT_TASK_ID] = task
    storage.NEXT_TASK_ID += 1
    return task


def get_task(task_id: int):
    return storage.TASKS.get(task_id)
