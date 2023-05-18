from time import sleep
import os 
from pathlib import Path 
from todo_factory import TodoFactory 
from todo_repository import TodoRepository
from todo_manager import TodoManager
from user_interface import UserInterface
from todo_validator import TodoValidator
from action import Action 

from todo_command import (
    AddTodoCommand, 
    CompleteTodoCommand,
    GetCompletedTodoCommand,
    RemoveTodoCommand, 
    GetTodosCommand, 
    GetTodoCommand, 
    UpdateTodoCommand 
    
)
ROOT_DIR  = Path(os.getcwd())

repository = TodoRepository(os.path.join(ROOT_DIR/ "v2.2/store.json"))

class TodoApp:
    
    def __init__(self):
        self.todo_manager = TodoManager(repository)
        self.user_interface = UserInterface()
        self.todo_validator = TodoValidator()
        self.todo_factory = TodoFactory()
        
        
    
    def run(self):

        while True:
            self.user_interface.display_welcome_message()
            choix_str = self.user_interface.ask_for_input("Entrez votre choix ->")
            try:
                choix = int(choix_str)
            except ValueError:
                print("Choix invalide, réessayez encore")
                return self.app_logic()

            if choix == Action.ADD_TODO:
                title = self.user_interface.ask_for_input("Entrez le titre de la tâche -> ")
                description = self.user_interface.ask_for_input("Entrez la description  -> ")
                self.todo_validator.avoid_empty_todo(title, description)
                todo = self.todo_factory.create_todo(title, description)
                command = AddTodoCommand(self.todo_manager, todo)
                command.execute()
                self.user_interface.display_todo_added_message()
                sleep(.5)
          
            elif choix == Action.REMOVE_TODO:
                title = self.user_interface.ask_for_input(
                    "Entrez le titre de la tâche à supprimer -> ")
                try:
                    command = RemoveTodoCommand(self.todo_manager, title)
                    command.execute()
                    self.user_interface.display_todo_removed_message()
                except ValueError:
                    self.user_interface.display_todo_not_found_error()
                sleep(.5)
            elif choix == Action.UPDATE_TODO:
                title = self.user_interface.ask_for_input(
                    "Entrer  le titre de la tâche à modifier -> ")
                command = GetTodoCommand(self.todo_manager, title)
                todo_to_modify = command.execute()
                modified_title = self.user_interface.ask_for_input(
                    "Entrer  la modification sur le titre ->  ")
                modified_description = self.user_interface.ask_for_input(
                    "Entrez la modification sur la description -> ")
                self.todo_validator.avoid_empty_todo(modified_title, modified_description)
                todo_to_modify.modify(modified_title, modified_description)
                command = UpdateTodoCommand(self.todo_manager, todo_to_modify)
                command.execute()
                self.user_interface.display_todo_modified_message()
                sleep(.5)
            elif choix == Action.COMPLETE_TODO:
                title = self.user_interface.ask_for_input(
                    "Entrer  le titre de la tâche à terminer -> ")
                command = GetTodoCommand(self.todo_manager, title)
                terminate_todo = command.execute()
                terminate_todo.completed()
                command = CompleteTodoCommand(self.todo_manager, terminate_todo)
                command.execute()
                self.user_interface.display_todo_completed_message()
            elif choix == Action.SHOW_TODO:
                command = GetTodosCommand(self.todo_manager)
                todos = command.execute()
                self.user_interface.display_pending_todos(todos)
            elif choix == Action.SHOW_COMPLETED_TODO:
                command = GetCompletedTodoCommand(self.todo_manager)
                completed_todos = command.execute()
                self.user_interface.display_completed_todos(completed_todos)
            elif choix == Action.EXIT_APP:
                return

