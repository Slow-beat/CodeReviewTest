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

## 项目结构

- `app.py`: Flask 应用入口
- `src/routes/tasks.py`: 任务相关路由
- `src/services/task_service.py`: 任务服务
- `src/storage.py`: 内存数据
- `src/utils/validators.py`: 参数校验
- `docs/legacy-notes.md`: 旧文档，后续演练会删除
