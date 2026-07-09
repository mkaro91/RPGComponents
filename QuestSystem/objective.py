class Objective:
    def __init__(self, description: str, required_progress: int = 1):
        if required_progress < 1: raise ValueError("Required objective progress must be at least one.")

        self.description = description
        self.current_progress = 0
        self.required_progress = required_progress
    
    def __str__(self):
        if self.is_completed:
            label = "[X]"
        else:
            if self.required_progress == 1:
                label = "[ ]"
            else:
                label = f"[{self.current_progress}/{self.required_progress}]"

        return f"{label} {self.description}"

    @property
    def is_completed(self):
        return self.current_progress == self.required_progress
    
    # Increases progress
    # Never exceeds required progress
    # Automatically marks object as complete when required progress is met
    def add_progress(self, amount: int = 1):
        """ Increases progress """
        if self.is_completed: 
            return
        
        self.current_progress = min(self.required_progress, self.current_progress + amount)