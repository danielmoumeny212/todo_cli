class TodoError(Exception):
    """Classe de base pour les erreurs de gestion de tâches"""
    pass

class TodoNotFoundError(TodoError):
    """Erreur lorsqu'une tâche est introuvable"""
    pass