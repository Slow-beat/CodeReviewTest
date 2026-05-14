# Task Review Demo

一个用于模拟 PR、代码审查和多轮修复的小型 Flask API 项目。

## 启动方式

```bash
pip install -r requirements.txt
python app.py
```

服务默认监听 `http://127.0.0.1:5000`。

## 基础接口

- `GET /health` 健康检查
- `GET /api/tasks` 获取任务列表
- `POST /api/tasks` 创建任务
- `POST /api/tasks/<task_id>/share` 共享任务给其他用户

共享接口请求体示例：

```json
{
  "actor_id": "u100",
  "target_user_ids": ["u200", "u201"],
  "message": "请一起处理这个任务"
}
```

## 项目结构

- `app.py`: Flask 应用入口
- `src/routes/shares.py`: 任务共享路由
- `src/routes/tasks.py`: 任务相关路由
- `src/services/share_service.py`: 任务共享服务
- `src/services/task_service.py`: 任务服务
- `src/storage.py`: 内存数据
- `src/utils/validators.py`: 参数校验
- `docs/share-api-draft.md`: 共享接口草稿文档
