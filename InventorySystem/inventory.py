from item import Item

from typing import List

class Inventory:
    def __init__(self):
        self.items: List[Item] = []
    
    def __str__(self) -> str:
        lines = [
            "Inventory",
            "",            
        ]

        for item in self.items:
            lines.append(str(item))
        
        return "\n".join(lines)
    
    def has_item(self, item_name: str) -> bool:
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return True
        return False
    
    def get_item(self, item_name: str) -> Item | None:
        """ Find an Item in inventory by name or return None """
        return next((item for item in self.items if item.name.lower() == item_name.lower()), None)
    
    def add_item(self, item: Item) -> None:
        """ Add an item to inventory """
        # Check if item exists already
        existing_item = self.get_item(item.name)

        # If existing item add to quantity
        # Else add new item to inventory
        if existing_item:
            existing_item.add(item.quantity)
        else:
            self.items.append(item)
    
    def remove_item(self, item_name: str, amount: int = 1) -> None:
        """ Remove an amount of an item from inventory """
        # Check if item in inventory
        if not self.has_item(item_name): raise ValueError(f"{item_name.title()} not found in inventory.")

        # Get Item by Name
        item = self.get_item(item_name)

        # Remove amount from item quantity
        item.remove(amount)
        
        # Remove item from inventory if quantity is 0
        if item.quantity == 0:
            self.items.remove(item)