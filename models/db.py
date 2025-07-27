from .models import Sheep

class FakeDB:
    def __init__(self):
        self.data = {
            1: Sheep(id=1, name="Spice", breed="Gotland", sex="Female")
        }
        self.next_id = 2

    def get_sheep(self, sheep_id: int):
        return self.data.get(sheep_id)

    def add_sheep(self, sheep: Sheep):
        self.data[sheep.id] = sheep

    def delete_sheep(self, sheep_id: int):
        return self.data.pop(sheep_id, None)

    def update_sheep(self, sheep_id: int, sheep: Sheep):
        if sheep_id in self.data:
            self.data[sheep_id] = sheep
            return sheep
        return None

    def get_all_sheep(self):
        return list(self.data.values())

db = FakeDB() 