from typing import List

import redis


class Basket:
    def __init__(self, redis) -> None:
        self.redis = redis
        self.basket_name = "basket"

    def add(self, key, value) -> bool:
        redis_key = self.basket_name + ":" + str(key)
        return self.redis.sadd(redis_key, value)

    def delete(self, key, value) -> None:
        redis_key = self.basket_name + ":" + str(key)
        self.redis.srem(redis_key, value)

    def is_member(self, key, value) -> bool:
        redis_key = self.basket_name + ":" + str(key)
        return self.redis.sismember(redis_key, value)

    def __getitem__(self, key) -> List:
        redis_key = self.basket_name + ":" + str(key)
        return [int(i.decode()) for i in self.redis.smembers(redis_key)]


class SeenBasket(Basket):
    def __init__(self, redis) -> None:
        super().__init__(redis)
        self.basket_name = "seen"


class CompareBasket(Basket):
    def __init__(self, redis) -> None:
        super().__init__(redis)
        self.basket_name = "compare"


class CartBasket(Basket):
    def __init__(self, redis) -> None:
        super().__init__(redis)
        self.basket_name = "cart"
