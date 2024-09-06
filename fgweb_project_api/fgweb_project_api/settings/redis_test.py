# 单独测试redis数据库连接状态
import redis
from decouple import config
# 创建 Redis 连接
r = redis.Redis(
    host = config('REDIS_HOST'),
    port = config('REDIS_PORT'),
    password = config('REDIS_PASSWORD')
)

# 测试连接
try:
    # Ping Redis 服务器以确认连接
    r.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")