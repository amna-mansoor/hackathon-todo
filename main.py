# [Task]: T040, T041, T042
# [From]: speckit.plan / Phase 8: Polish & Cross-Cutting Concerns
# [Spec]: speckit.specify / FR-009, SC-004

from src.todo_app import TodoManager
import sys

def display_help():
    """Displays help information for the CLI commands."""
    print("\n--- Todo App CLI Help ---")
    print("Available Commands:")
    print("  add <description>             : Adds a new task with the given description.")
    print("  list                          : Displays all tasks with their ID, status, and description.")
    print("  complete <id>                 : Marks the task with the specified ID as complete.")
    print("  update <id> <new_description> : Updates the description of the task with the specified ID.")
    print("  delete <id>                   : Deletes the task with the specified ID.")
    print("  help                          : Displays this help message.")
    print("  exit                          : Exits the application.")
    print("---------------------------\n")

def main():
    todo_manager = TodoManager()
    
    print("Welcome to the Todo App!")
    display_help()

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            command_parts = user_input.split(maxsplit=1)
            command = command_parts[0].lower()
            args = command_parts[1] if len(command_parts) > 1 else ""

            if command == "exit":
                print("Exiting Todo App. Goodbye!")
                break
            elif command == "help":
                display_help()
            elif command == "add":
                if not args:
                    print("Error: 'add' command requires a description. Usage: add <description>")
                    continue
                try:
                    task = todo_manager.add_task(args)
                    print(f"Added task: {task.id}. {task.description}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "list":
                print(todo_manager.get_formatted_task_list())
            elif command == "complete":
                try:
                    task_id = int(args)
                    todo_manager.mark_task_complete(task_id)
                    print(f"Task {task_id} marked as complete.")
                except ValueError as e:
                    print(f"Error: {e}")
                except TypeError: # Catches if int() conversion fails on non-numeric input
                    print("Error: 'complete' command requires a numeric task ID. Usage: complete <id>")
            elif command == "update":
                try:
                    parts = args.split(maxsplit=1)
                    if len(parts) < 2:
                        print("Error: 'update' command requires a task ID and new description. Usage: update <id> <new_description>")
                        continue
                    task_id = int(parts[0])
                    new_description = parts[1]
                    todo_manager.update_task(task_id, new_description)
                    print(f"Task {task_id} updated.")
                except ValueError as e:
                    print(f"Error: {e}")
                except TypeError:
                    print("Error: 'update' command requires a numeric task ID. Usage: update <id> <new_description>")
            elif command == "delete":
                try:
                    task_id = int(args)
                    todo_manager.delete_task(task_id)
                    print(f"Task {task_id} deleted.")
                except ValueError as e:
                    print(f"Error: {e}")
                except TypeError:
                    print("Error: 'delete' command requires a numeric task ID. Usage: delete <id>")
            else:
                print(f"Unknown command: '{command}'. Type 'help' for available commands.")

        except EOFError:
            print("\nExiting Todo App. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please report this bug.")

if __name__ == "__main__":
    main()
