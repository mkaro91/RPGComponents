class Quest:
    """ Represents a quest that can be completed by a player"""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.objectives = []
    
    def __str__(self):
        label = "[ ]" if not self.is_completed else "[X]"

        lines = [
            f"{label} {self.title}",
            self.description,
            "\nObjectives:"
        ]

        for objective in self.objectives:
            lines.append(str(objective))
        
        lines.append("\n")

        return "\n".join(lines)

    @property
    def is_completed(self):
        if not self.objectives: return False
        return all(objective.is_completed for objective in self.objectives)
    
    def add_objective(self, objective):
        """ Adds an objective object """
        self.objectives.append(objective)