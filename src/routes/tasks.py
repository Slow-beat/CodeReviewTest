from flask import Blueprint, jsonify, request

from src.services.task_service import create_task, list_tasks
from src.utils.validators import validate_task_payload


tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("")
def get_tasks():
    return jsonify({"items": list_tasks()})


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
