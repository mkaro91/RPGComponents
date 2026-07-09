from entity import Entity

from typing import Dict

class EntityRegistry:
    def __init__(self):
        self.entities: Dict[str, Entity] = {}
    
    def __str__(self) -> str:
        lines = ["Entities", ""]

        for entity in self.entities.values():
            lines.append(str(entity))
        
        return "\n".join(lines)
    
    def _validate_entity_type(self, entity: Entity) -> None:
        """ Validates a given entity is of type Entity """
        if not isinstance(entity, Entity): 
            raise TypeError("Invalid entity type.")
    
    def _validate_new_entity(self, entity_id: str) -> None:
        """ Validates a given entity doesn't already exist in registry """
        if self.has_entity(entity_id):
            raise ValueError(f"{entity_id} already exists.")
    
    def _validate_existing_entity(self, entity_id: str) -> None:
        """ Validates a given entity is found in the registry """
        if not self.has_entity(entity_id):
            raise ValueError("Unknown entity.")
    
    def has_entity(self, entity_id: str) -> bool:
        """ Returns True if a given name is in registry else False """
        return entity_id in self.entities
    
    def get(self, entity_id: str) -> Entity | None:
        """ Returns an entity with matching name or None """
        return self.entities.get(entity_id, None)

    def add(self, entity: Entity) -> None:
        """ Adds an entity to the registry """
        self._validate_entity_type(entity)
        self._validate_new_entity(entity.id)

        self.entities[entity.id] = entity
    
    def remove(self, entity_id: str) -> None:
        """ Removes an entity from registry if they exist """
        self._validate_existing_entity(entity_id)
        del self.entities[entity_id]
        