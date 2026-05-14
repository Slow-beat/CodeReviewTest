# Export API Draft

该文档用于记录导出接口的草稿设计，当前仅供内部讨论：

- 路径：`GET /api/tasks/<task_id>/export`
- 参数：
  - `actor_id`
  - `download_name`
- 输出：
  - 导出文件路径
  - 任务信息

待补充：

- 文件名安全策略
- 权限校验规则
- 导出格式统一约定
