from typing import Iterable


class DataBase:
    storage = {}

    def create(self, name: str, value: dict) -> None:
        self.storage[name] = value

    def get(self, name: str) -> dict:
        if name in self.storage:
            return self.storage[name]

        raise ValueError("Ключа %s нет базе данных")

    def all(self) -> Iterable[dict]:
        for key, value in self.storage.items():
            yield value

    def filter(self, **search_parameters) -> dict:
        for key, data in self.storage.items():
            for parameter, value in search_parameters.items():
                if parameter in self.storage and self.storage[parameter] == value:
                    yield data




def get_db() -> DataBase:
    db = DataBase()
    yield db