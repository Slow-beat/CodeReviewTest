from flask import Blueprint, jsonify, request

from src.services.share_service import share_task


shares_bp = Blueprint("shares", __name__)


@shares_bp.post("/<int:task_id>/share")
def create_share(task_id: int):
    payload = request.get_json(silent=True) or {}

    try:
        result = share_task(
            task_id=task_id,
            actor_id=payload.get("actor_id", ""),
            target_user_ids=payload.get("target_user_ids", []),
            message=payload.get("message", ""),
        )
        return jsonify(result), 200
    except Exception:
        return jsonify({"error": "share failed"}), 500
