from entity import Entity

class NPC(Entity):
    def __init__(self, name: str):
        super().__init__(name, entity_type="Npc")