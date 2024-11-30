"""
Ce script a pour but de créer un classe de nom étudiant et qui contient ses informations
"""

class Etudiant:
    def __init__(self, nom: str, prénom: str, age: int, moyenne: float):
        self.nom: str = nom
        self.prénom: str = prénom
        self.age: int = age
        self.moyenne: float = moyenne