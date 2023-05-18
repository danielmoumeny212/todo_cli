from abc import ABC, abstractmethod

from todo import Todo
from todo_manager import TodoManager


class Command(ABC):
    """Interface de commande"""

    def __init__(self, service: TodoManager):
        self._service = service

    @abstractmethod
    def execute(self):
        """Exécuter la commande"""
        pass


class AddTodoCommand(Command):

    def __init__(self, service: TodoManager, todo: Todo):
        super().__init__(service)
        self._todo = todo

    def execute(self):

        self._service.add(self._todo)


class RemoveTodoCommand(Command):

    def __init__(self, service: TodoManager, title: str):
        super().__init__(service)
        self._title = title

    def execute(self):
        """Exécuter la commande"""
        self._service.remove_todo(self._title)

class GetTodoCommand(Command):
    def __init__(self, service: TodoManager, title: str):
        super().__init__(service)
        self._title = title

    def execute(self):
        """Exécuter la commande"""
        return self._service.get_todo(self._title)
      

class UpdateTodoCommand(Command):

    def __init__(self, service: TodoManager, todo_to_modify: Todo):
        super().__init__(service)
        self._todo_to_modify = todo_to_modify

    def execute(self):
        """Exécuter la commande"""
        self._service.update_todo(self._todo_to_modify)


class CompleteTodoCommand(Command):

    def __init__(self, service: TodoManager, terminate_todo: Todo):
        super().__init__(service)
        self._terminate_todo = terminate_todo

    def execute(self):
        """Exécuter la commande"""
        self._service.update_todo(self._terminate_todo)


class GetTodosCommand(Command):

    def __init__(self, service: TodoManager):
        super().__init__(service)

    def execute(self):
        """Exécuter la commande"""
        return self._service.get_todos()


class GetCompletedTodoCommand(Command):
    def __init__(self, service: TodoManager):
        super().__init__(service)

    def execute(self):
        """Exécuter la commande"""
        return self._service.completed_todos()


