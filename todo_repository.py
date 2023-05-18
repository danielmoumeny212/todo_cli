import os
from typing import List
import json
from todo import Todo,  TodoEncoder


class TodoRepository:
    """Classe de stockage de tâches"""

    def __init__(self, filepath: str = 'store.json') -> None:
        self.filepath = filepath

    def read(self) -> List[Todo]:
        if os.path.exists(self.filepath):
            return self.__load_todos()
        else:
            self.__create_file_if_not_exists()
            return []

    def __create_file_if_not_exists(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                f.write('')

    def __load_todos(self):
        with open(self.filepath) as f:
            todos_data = json.load(f)
            return [Todo(**todo) for todo in todos_data]

    def update(self, todos: List[Todo]) -> None:
        """Écrire la liste des tâches dans le fichier"""
        with open(self.filepath, 'w') as f:
            json.dump(todos, f, indent=4, cls=TodoEncoder)
