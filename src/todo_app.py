# [Task]: T007, T008, T009
# [From]: speckit.plan / Phase 2: Foundational
# [Spec]: speckit.specify / FR-006, FR-007, FR-008, Key Entities

class Task:
    """
    Represents a single to-do item.
    [Spec]: Key Entities
    """
    def __init__(self, id: int, description: str, status: str = "Pending"):
        self.id = id
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', status='{self.status}')"

class TodoManager:
    """
    Manages the in-memory storage and operations for tasks.
    [Spec]: FR-006
    """
    def __init__(self):
        self._tasks = []  # In-memory storage for Task objects
        self._next_id = 1 # Mechanism to generate unique integer IDs for new tasks
        # [Spec]: FR-007

    def _generate_id(self) -> int:
        """
        Generates a unique ID for a new task.
        """
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def add_task(self, description: str) -> Task:
        """
        Adds a new task with the given description to the in-memory storage.
        [Spec]: User Story 1 / FR-001, FR-009
        """
        if not description:
            raise ValueError("Task description cannot be empty")

        task_id = self._generate_id()
        new_task = Task(id=task_id, description=description)
        self._tasks.append(new_task)
        return new_task

    def get_formatted_task_list(self) -> str:
        """
        Retrieves all tasks and formats them for display.
        [Spec]: User Story 2 / FR-002
        """
        if not self._tasks:
            return "No tasks yet!"
        
        formatted_tasks = []
        for task in self._tasks:
            formatted_tasks.append(f"{task.id}. [{task.status}] {task.description}")
        return "\n".join(formatted_tasks)

    def mark_task_complete(self, task_id: int) -> None:
        """
        Marks a task as complete given its ID.
        [Spec]: User Story 3 / FR-003, FR-009
        """
        found_task = None
        for task in self._tasks:
            if task.id == task_id:
                found_task = task
                break
        
        if found_task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        
        if found_task.status == "Complete":
            raise ValueError(f"Task with ID {task_id} is already complete.")
        
        found_task.status = "Complete"

    def update_task(self, task_id: int, new_description: str) -> None:
        """
        Updates the description of a task given its ID.
        [Spec]: User Story 4 / FR-004, FR-009
        """
        if not new_description:
            raise ValueError("Task description cannot be empty")

        found_task = None
        for task in self._tasks:
            if task.id == task_id:
                found_task = task
                break
        
        if found_task is None:
            raise ValueError(f"Task with ID {task_id} not found.")
        
        found_task.description = new_description

    def delete_task(self, task_id: int) -> None:
        """
        Deletes a task given its ID.
        [Spec]: User Story 5 / FR-005, FR-009
        """
        initial_task_count = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        
        if len(self._tasks) == initial_task_count:
            raise ValueError(f"Task with ID {task_id} not found.")




