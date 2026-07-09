class Stat:
    def __init__(self, name: str, value: int):
        if not name.strip(): raise ValueError("Stat name cannot be blank.")
        if value < 0: raise ValueError("Stat value cannot be less than zero.")

        self.__name = name.title()
        self.__value = value
    
    def __str__(self) -> str:
        return f"{self.name}: {self.value}"

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def value(self) -> int:
        return self.__value
    
    def _validate_amount(self, amount: int) -> None:
        """ Validates change amount is above zero """
        if amount < 1: 
            raise ValueError("Change amount must be at least one.")
    
    def _validate_sufficient_value(self, amount: int) -> None:
        if self.value < amount: 
            raise ValueError("Stat value cannot go negative.")
    
    def increase(self, amount: int = 1) -> None:
        """ Increase stat value """
        self._validate_amount(amount)
        self.__value += amount
    
    def decrease(self, amount: int = 1) -> None:
        """ Decrease stat value """
        self._validate_amount(amount)
        self._validate_sufficient_value(amount)

        self.__value -= amount
