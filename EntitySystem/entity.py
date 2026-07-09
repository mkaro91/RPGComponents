from uuid import uuid4

class Entity:
    def __init__(self, name: str, entity_type: str):
        if not name.strip(): raise ValueError("Entity name cannot be blank.")
        if not entity_type.strip(): raise ValueError("Entity type cannot be blank.")

        self.__id = str(uuid4())
        self.__name = name.title()
        self.__entity_type = entity_type.title()
    
    def __str__(self) -> str:
        lines = [
            f"\nEntity ID: {self.id}",
            f"Name: {self.name}",
            f"Type: {self.entity_type}"
        ]

        return "\n".join(lines)
        
    @property
    def id(self) -> str:
        return self.__id 
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def entity_type(self) -> str:
        return self.__entity_type