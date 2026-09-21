from __future__ import annotations

from functools import lru_cache

from redis import Redis

from app.config import get_settings


@lru_cache(maxsize=1)
def get_redis_client() -> Redis:
    """创建 Redis 客户端单例。

    当前阶段 Redis 主要承担会话缓存与后续对话状态缓存的职责。
    这里提前把常用连接参数收口，后面业务层直接复用这个客户端即可。
    """

    settings = get_settings()
    # protocol=2（RESP2）：兼容老版本 Redis（< 6.0 不支持 HELLO/RESP3）。
    # 本机原生 Redis 较旧，redis-py 8.x 默认走 RESP3 会报 unknown command 'HELLO'。
    return Redis.from_url(
        settings.redis_url,
        decode_responses=True,
        protocol=2,
        socket_connect_timeout=5,
        socket_timeout=5,
        health_check_interval=30,
        retry_on_timeout=True,
    )
