from typing import List


class Basket:
    def __init__(self) -> None:
        self.storage = {}

    def add(self, key, value) -> None:
        if key not in self.storage:
            self.storage[key] = set()
        self.storage[key].add(value)

    def delete(self, key, value) -> None:
        if key not in self.storage or value not in self.storage[key]:
            return
        self.storage[key].remove(value)

    def __getitem__(self, key) -> List:
        if key not in self.storage:
            return
        return list(self.storage[key])

    def __contains__(self, key) -> bool:
        return key in self.storage


class SeenBasket(Basket):
    def __init__(self) -> None:
        super().__init__()


class CompareBasket(Basket):
    def __init__(self) -> None:
        super().__init__()


class CartBasket(Basket):
    def __init__(self) -> None:
        super().__init__()
