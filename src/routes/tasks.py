from flask import Blueprint, jsonify, request

from src.services.task_service import create_task, get_task, list_tasks
from src.utils.validators import validate_task_payload


tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("")
def get_tasks():
    return jsonify({"items": list_tasks()})


@tasks_bp.get("/<int:task_id>")
def get_task_detail(task_id: int):
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "task not found"}), 404

    return jsonify(
        {
            "item": task,
            "links": {
                "share": f"/api/tasks/{task_id}/share",
                "export": f"/api/tasks/{task_id}/export",
            },
        }
    )


@tasks_bp.post("")
def add_task():
    payload = request.get_json(silent=True) or {}
    error = validate_task_payload(payload)
    if error:
        return jsonify({"error": error}), 400

    task = create_task(
        title=payload["title"],
        description=payload.get("description", ""),
        owner_id=payload["owner_id"],
    )
    return jsonify(task), 201
