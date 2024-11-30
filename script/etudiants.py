"""
Ce script a pour but de créer un classe de nom étudiant et qui contient ses informations
"""
import saisir

class Etudiant:
    def __init__(self):
        self.nom: str = saisir.nom().capitalize()
        self.prénom: str = saisir.prénom().capitalize()
        self.age: int = saisir.age()
        self.moyenne: float = saisir.moyenne()

    def modifier_nom(self) -> None:
        self.nom: str = saisir.nom().capitalize()
    
    def modifier_prénom(self) -> None:
        self.prénom: str = saisir.prénom().capitalize()

    def modifier_nom_compet(self, nom: str, prénom: str) -> None:
        self.modifier_nom(nom)
        self.modifier_prénom(prénom)

    def modifier_age(self) -> None:
        self.age: int = saisir.age()
    
    def modifier_moyenne(self) -> None:
        self.moyenne: float = saisir.moyenne()