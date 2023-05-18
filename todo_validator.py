from todo_error import TodoError 



class TodoValidator:
    def avoid_empty_todo(self, title: str, description: str):
        if title == "" and description == "":
            raise TodoError(
                "vous ne pouvez pas creer une tâche sans titre ni description")
