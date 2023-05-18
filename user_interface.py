from typing import List 
from todo import Todo 

class UserInterface:
    def display_welcome_message(self):
        print("Bienvenue sur votre gestionnaire de tâche ")
        print("""
                  tapez:
                   1-pour ajouter une nouvelle tâche
                   2-supprimer une tâche
                   3-modifier une tâche
                   4-terminer une tâche
                   5-afficher la liste des tâche en cours
                   6-liste des tâches terminées
                   7-pour quitter le programme
                """)

    def ask_for_input(self, help_text: str) -> str:
        return input(help_text).strip()

    def display_todo_added_message(self):
        print("La tâche a été bien ajoutée")

    def display_todo_removed_message(self):
        print("La tâche a été supprimée")

    def display_todo_modified_message(self):
        print("La tâche a été modifiée")

    def display_todo_completed_message(self):
        print("La tâche a été terminée")

 
    def display_pending_todos(self, todo_list: List[Todo]):
        print("Liste des tâches en cours :")
        for i in range(len(todo_list)):
            print("Tache n°", i+1)
            print(todo_list[i])

    def display_completed_todos(self, todo_list: List[Todo]):
        print("Liste des tâches terminées :")
    
        
        for index, todo in enumerate(todo_list):
            print("Tache n°", index, "")
            print(todo)

    def display_invalid_choice_error(self):
        print("Choix invalide, réessayez encore")

    def display_todo_not_found_error(self):
        print("La tâche entrée est introuvable")


