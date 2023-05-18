from todo import Todo


class TodoFactory:
    def create_todo(self, title: str, description: str,  **kwargs) -> Todo:
        return Todo(title, description, **kwargs)
