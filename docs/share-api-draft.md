# Share API Draft

该文档用于记录共享接口的草稿设计，当前仅供内部讨论：

- 路径：`POST /api/tasks/<task_id>/share`
- 角色：任务拥有者可以把任务共享给其他用户
- 参数：
  - `actor_id`
  - `target_user_ids`
  - `message`

待补充：

- 权限边界
- 错误码约定
- 返回字段收敛
