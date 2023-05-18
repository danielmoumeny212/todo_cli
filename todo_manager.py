from typing import List
import copy
from todo_error import TodoNotFoundError, TodoError
from todo_repository import TodoRepository
from todo import Todo


class TodoManager:
    """Classe de gestion de tâches"""

    def __init__(self, repository: TodoRepository) -> None:
        self.repository = repository
        self.selected_todo: Todo = None

    def update_todo(self, todo: Todo) -> None:
        """Mettre à jour une tâche existante"""
        if self.selected_todo:
            try:
                self._todos = self.repository.read()
                index = self._todos.index(self.selected_todo)
                self._todos.remove(self.selected_todo)
                self._todos.insert(index, todo)
            except ValueError:
                raise TodoError(
                    "La tâche sélectionnée n'a pas été trouvée dans la liste des tâches")
            self.repository.update(self._todos)
        else:
            raise TodoError("Aucune tâche sélectionnée")

    def add(self, todo: Todo) -> None:
        """Ajouter une tâche à la liste"""
        self._todos = self.repository.read()
        if todo in self._todos:
            anwser = input(
                "warning existing todo! do you want to add it ?(yes or no) -> ")
            if not anwser.strip() == "yes":
                print('cancelled adding todo')
                return
            self._todos.append(todo)
            self.repository.update(self._todos)
        else:
            self._todos.append(todo)
            self.repository.update(self._todos)

    def get_todos(self) -> List[Todo]:
        """Obtenir la liste complète des tâches"""
        self._todos = self.repository.read()
        return self._todos

    def get_todo(self, title: str) -> Todo:
        """Obtenir une tâche par son titre"""
        self._todos = self.repository.read()
        for todo in self._todos:
            if todo.title.lower() == title.lower():
                self.selected_todo = copy.deepcopy(todo)
                return todo
        raise TodoNotFoundError(
            f"La tâche avec le titre '{title}' n'a pas été trouvée")

    def _filter_todo_list(self, todo: Todo, is_completed: bool = False):
        if todo.is_completed == is_completed:
            return todo

    def remove_todo(self, title: str) -> None:
        self._todos = self.repository.read()
        for todo in self._todos:
            if todo.title.lower() == title.lower():
                self._todos.remove(todo)
                self.repository.update(self._todos)
                return

    def completed_todos(self):
        self._todos = self.repository.read()
        filtered_todos = filter(
            lambda todo: self._filter_todo_list(todo, True), self._todos)
        return list(filtered_todos)

    def uncompleted_todos(self):
        self._todos = self.repository.read()
        filtered_todos = filter(
            lambda todo: self._filter_todo_list(todo, False), self._todos)
        return list(filtered_todos)
