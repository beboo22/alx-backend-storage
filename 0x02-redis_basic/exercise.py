#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
