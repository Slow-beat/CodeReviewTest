from flask import Blueprint, jsonify, request

from src.services.export_service import export_task
from src.utils.validators import validate_export_query


exports_bp = Blueprint("exports", __name__)


@exports_bp.get("/<int:task_id>/export")
def export_task_file(task_id: int):
    error = validate_export_query(request.args)
    if error:
        return jsonify({"message": error}), 400

    try:
        result = export_task(
            task_id=task_id,
            actor_id=request.args["actor_id"],
            download_name=request.args["download_name"],
        )
        return jsonify(result), 200
    except PermissionError:
        return jsonify({"error": "forbidden"}), 403
    except ValueError:
        return jsonify({"error": "export failed"}), 404
    except Exception:
        return jsonify({"error": "export failed"}), 500
