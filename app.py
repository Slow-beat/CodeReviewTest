from flask import Flask, jsonify

from src.routes.shares import shares_bp
from src.routes.tasks import tasks_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")
    app.register_blueprint(shares_bp, url_prefix="/api/tasks")

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok"})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
