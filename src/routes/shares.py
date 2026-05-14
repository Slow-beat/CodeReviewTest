from flask import Blueprint, jsonify, request

from src.services.share_service import share_task
from src.services.task_service import get_task


shares_bp = Blueprint("shares", __name__)


@shares_bp.post("/<int:task_id>/share")
def create_share(task_id: int):
    payload = request.get_json(silent=True) or {}
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "task not found"}), 404

    actor_id = payload.get("actor_id", "")
    if not actor_id:
        return jsonify({"error": "actor_id is required"}), 400

    target_user_ids = payload.get("target_user_ids", [])
    if not isinstance(target_user_ids, list) or not target_user_ids:
        return jsonify({"error": "target_user_ids must be a non-empty list"}), 400

    if task["owner_id"] != actor_id:
        return jsonify({"error": "only task owner can share task"}), 403

    try:
        result = share_task(
            task_id=task_id,
            actor_id=actor_id,
            target_user_ids=target_user_ids,
            message=payload.get("message", ""),
        )
        return jsonify(result), 200
    except Exception:
        return jsonify({"error": "share failed"}), 500
