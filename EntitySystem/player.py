from entity import Entity

class Player(Entity):
    def __init__(self, name: str):
        super().__init__(name, entity_type="player")