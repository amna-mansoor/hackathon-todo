# [Task]: T010, T011
# [From]: speckit.plan / Phase 3: User Story 1 - Add Task / Tests
# [Spec]: speckit.specify / User Story 1, FR-001, FR-009

from src.todo_app import TodoManager, Task
import pytest

@pytest.fixture
def todo_manager():
    """Provides a fresh TodoManager instance for each test."""
    return TodoManager()

def test_add_task_with_valid_description(todo_manager):
    """
    Test that a task with a valid description can be added.
    [Spec]: User Story 1 / Acceptance Scenarios 1, FR-001
    """
    description = "Buy groceries"
    task = todo_manager.add_task(description) # This function doesn't exist yet, so it will fail

    assert task.description == description
    assert task.status == "Pending"
    assert task.id is not None
    assert len(todo_manager._tasks) == 1
    assert todo_manager._tasks[0] == task

def test_add_task_with_empty_description(todo_manager):
    """
    Test that adding a task with an empty description raises an error.
    [Spec]: User Story 1 / Acceptance Scenarios 2, FR-009
    """
    with pytest.raises(ValueError, match="Task description cannot be empty"):
        todo_manager.add_task("") # This function doesn't exist yet, so it will fail
    
    assert len(todo_manager._tasks) == 0


# [Task]: T015, T016
# [From]: speckit.plan / Phase 4: User Story 2 - View Task List / Tests
# [Spec]: speckit.specify / User Story 2, FR-002

def test_view_empty_task_list(todo_manager):
    """
    Test that viewing an empty task list returns an appropriate message.
    [Spec]: User Story 2 / Acceptance Scenarios 2
    """
    assert todo_manager.get_formatted_task_list() == "No tasks yet!"


def test_view_task_list_with_multiple_tasks(todo_manager):
    """
    Test that viewing a task list with multiple tasks (pending and complete)
    returns all tasks with correct formatting.
    [Spec]: User Story 2 / Acceptance Scenarios 1
    """
    task1 = todo_manager.add_task("Buy groceries")
    task2 = todo_manager.add_task("Walk the dog")
    task3 = todo_manager.add_task("Do laundry")
    
    # Manually change status for testing purposes as mark_task_complete is not yet implemented
    task2.status = "Complete"

    expected_list = [
        f"{task1.id}. [Pending] Buy groceries",
        f"{task2.id}. [Complete] Walk the dog",
        f"{task3.id}. [Pending] Do laundry"
    ]
    assert todo_manager.get_formatted_task_list() == "\n".join(expected_list)


# [Task]: T020, T021, T022
# [From]: speckit.plan / Phase 5: User Story 3 - Mark Task as Complete / Tests
# [Spec]: speckit.specify / User Story 3, FR-003, FR-009

def test_mark_existing_task_as_complete(todo_manager):
    """
    Test that an existing pending task can be marked as complete.
    [Spec]: User Story 3 / Acceptance Scenarios 1
    """
    task = todo_manager.add_task("Call mom")
    todo_manager.mark_task_complete(task.id) # This function doesn't exist yet, so it will fail
    
    found_task = next((t for t in todo_manager._tasks if t.id == task.id), None)
    assert found_task is not None
    assert found_task.status == "Complete"

def test_mark_non_existent_task_as_complete(todo_manager):
    """
    Test that attempting to mark a non-existent task as complete raises an error.
    [Spec]: User Story 3 / Acceptance Scenarios 2, FR-009
    """
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        todo_manager.mark_task_complete(999) # This function doesn't exist yet, so it will fail
    
def test_mark_already_complete_task_again(todo_manager):
    """
    Test that attempting to mark an already complete task as complete again raises an error.
    [Spec]: User Story 3 / Acceptance Scenarios 3, FR-009
    """
    task = todo_manager.add_task("Read book")
    task.status = "Complete" # Manually set for test setup, as the actual method is not yet implemented
    
    with pytest.raises(ValueError, match=f"Task with ID {task.id} is already complete."):
        todo_manager.mark_task_complete(task.id)


# [Task]: T027, T028, T029
# [From]: speckit.plan / Phase 6: User Story 4 - Update Task / Tests
# [Spec]: speckit.specify / User Story 4, FR-004, FR-009

def test_update_existing_task_description(todo_manager):
    """
    Test that an existing task's description can be updated.
    [Spec]: User Story 4 / Acceptance Scenarios 1
    """
    task = todo_manager.add_task("Buy bread")
    new_description = "Buy bread and milk"
    todo_manager.update_task(task.id, new_description) # This function doesn't exist yet, so it will fail
    
    found_task = next((t for t in todo_manager._tasks if t.id == task.id), None)
    assert found_task is not None
    assert found_task.description == new_description

def test_update_non_existent_task(todo_manager):
    """
    Test that attempting to update a non-existent task raises an error.
    [Spec]: User Story 4 / Acceptance Scenarios 2, FR-009
    """
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        todo_manager.update_task(999, "Some new description") # This function doesn't exist yet, so it will fail
    
def test_update_task_with_empty_description(todo_manager):
    """
    Test that attempting to update a task with an empty description raises an error.
    [Spec]: User Story 4 / Acceptance Scenarios 3, FR-009
    """
    task = todo_manager.add_task("Original description")
    with pytest.raises(ValueError, match="Task description cannot be empty"):
        todo_manager.update_task(task.id, "") # This function doesn't exist yet, so it will fail
    
    found_task = next((t for t in todo_manager._tasks if t.id == task.id), None)
    assert found_task.description == "Original description" # Ensure description remains unchanged


# [Task]: T034, T035
# [From]: speckit.plan / Phase 7: User Story 5 - Delete Task / Tests
# [Spec]: speckit.specify / User Story 5, FR-005, FR-009

def test_delete_existing_task(todo_manager):
    """
    Test that an existing task can be deleted.
    [Spec]: User Story 5 / Acceptance Scenarios 1
    """
    task = todo_manager.add_task("Wash car")
    todo_manager.delete_task(task.id) # This function doesn't exist yet, so it will fail
    
    found_task = next((t for t in todo_manager._tasks if t.id == task.id), None)
    assert found_task is None
    assert len(todo_manager._tasks) == 0

def test_delete_non_existent_task(todo_manager):
    """
    Test that attempting to delete a non-existent task raises an error.
    [Spec]: User Story 5 / Acceptance Scenarios 2, FR-009
    """
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        todo_manager.delete_task(999) # This function doesn't exist yet, so it will fail
    

 # This function doesn't exist yet, so it will fail


