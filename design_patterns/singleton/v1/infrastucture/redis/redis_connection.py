import redis


class Cache:
    _instance = None

    def __init__(self, connection):
        self.connection = redis.Redis.from_url(connection)

    @classmethod
    def get_instance(cls, connection):
        if cls._instance is None:
            cls._instance = cls(connection)
        return cls._instance

    def get(self, key: str) -> str or None:
        try:
            if key is None:
                return key
            redis_key = self.connection.get(key)
            return redis_key.decode('utf-8') if redis_key is not None else None
        except Exception:
            return None

    def set(self, key: str, value: str, time: int) -> None:
        try:
            self.connection.set(key, value, ex=time)
        except Exception:
            pass
