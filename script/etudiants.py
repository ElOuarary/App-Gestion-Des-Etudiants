"""
Ce script a pour but de créer un classe de nom étudiant et qui contient ses informations
"""

class Etudiant:
    def __init__(self, nom: str, prénom: str, age: int, moyenne: float):
        self.nom: str = nom
        self.prénom: str = prénom
        self.age: int = age
        self.moyenne: float = moyenne

    def modifier_nom(self, nom: str) -> None:
        self.nom: str = nom
    
    def modifier_prénom(self, prénom: str) -> None:
        self.prénom: str = prénom

    def modifier_nom_compet(self, nom: str, prénom: str) -> None:
        self.modifier_nom(nom)
        self.modifier_prénom(prénom)

    def modifier_age(self, age: int) -> None:
        self.age: int = age
    
    def modifier_moyenne(self, moyenne: float) -> None:
        self.moyenne: float = moyenne