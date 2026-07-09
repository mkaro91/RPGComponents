from statClass import Stat
from typing import Dict

class Stats:
    def __init__(self):
        self.stats: Dict[str, Stat] = {}
    
    def __str__(self) -> str:
        lines = [str(stat) for stat in self.stats.values()]
        return "\n".join(lines)
    
    def _validate_stat_exists(self, stat) -> None:
        if stat is None:
            raise ValueError(f"Stat does not exist in stat list.")

    def has_stat(self, stat_name: str) -> bool:
        return stat_name.lower() in self.stats
    
    def get_stat(self, stat_name: str) -> Stat | None:
        return self.stats.get(stat_name.lower())
    
    def add_stat(self, stat: Stat) -> None:
        if self.has_stat(stat.name): raise ValueError(f"{stat.name} already exists in stat list.")
        self.stats[stat.name.lower()] = stat
    
    def increase_stat(self, stat_name: str, amount: int = 1) -> None:
        stat = self.get_stat(stat_name)
        self._validate_stat_exists(stat)
        stat.increase(amount)
        
    def decrease_stat(self, stat_name: str, amount: int = 1) -> None:
        stat = self.get_stat(stat_name)
        self._validate_stat_exists(stat)
        stat.decrease(amount)