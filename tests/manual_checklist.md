# Manual Checklist

最终合并前，请按以下步骤手工验证：

1. 安装依赖：`pip3 install -r requirements.txt`
2. 启动服务：`python3 app.py`
3. 访问 `GET /health`，确认返回 `{"status": "ok"}`
4. 访问 `GET /api/tasks/1`，确认能看到任务详情和 `share`/`export` 链接
5. 调用 `POST /api/tasks/1/share`，传入 owner `u100` 和非空 `target_user_ids`，确认返回 200
6. 调用 `POST /api/tasks/1/share`，传入空 `target_user_ids`，确认返回 400
7. 调用 `POST /api/tasks/1/share`，传入非 owner `actor_id`，确认返回 403
8. 调用 `GET /api/tasks/1/export?actor_id=u100&download_name=very-long-file-name.csv`，确认返回 200，且 `download_name` 保留 `.csv`
9. 调用 `GET /api/tasks/1/export?actor_id=u999&download_name=task.txt`，确认返回 403
