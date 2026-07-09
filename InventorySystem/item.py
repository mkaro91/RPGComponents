class Item:
    def __init__(self, name: str, quantity: int = 1):
        if quantity < 1: 
            raise ValueError("Item quantity must be at least one.")

        self.__name = name.title()
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    
    @property
    def quantity(self):
        return self.__quantity
    
    def _validate_sufficient_quantity(self, amount: int):
        """ Validates enough quantity of an item exists for removal """
        if self.quantity < amount:
            raise ValueError("Insufficient item quantity.")
    
    def _validate_amount(self, amount: int):
        """ Validates given amount before operations """
        if amount < 1:
            raise ValueError("Change amount must be at least one.")

    def add(self, amount: int = 1):
        """ Add to quantity """
        self._validate_amount(amount)

        self.__quantity += amount
    
    def remove(self, amount: int = 1):
        """ Reduce quantity """
        self._validate_amount(amount)
        self._validate_sufficient_quantity(amount)
        
        self.__quantity -= amount
    
