"""
Ce script a pour but de créer un classe de nom étudiant et qui contient ses informations
"""
import saisir

class Etudiant:
    """
    Représente un étudiant avec des méthodes pour modifier ses informations.
    """
    def __init__(self, nom: str = None, prénom: str = None, age: int = None, moyenne: float =  None):
        self.nom: str = nom if nom else saisir.nom().capitalize()
        self.prénom: str = prénom if prénom else saisir.prénom().capitalize()
        self.age: int = age if age else saisir.age()
        self.moyenne: float = moyenne if moyenne else saisir.moyenne()

    def modifier_nom(self) -> None:
        self.nom: str = saisir.nom().capitalize()
    
    def modifier_prénom(self) -> None:
        self.prénom: str = saisir.prénom().capitalize()

    def modifier_nom_compet(self) -> None:
        self.nom: str = saisir.nom().capitalize()
        self.prénom: str = saisir.prénom().capitalize()

    def modifier_age(self) -> None:
        self.age: int = saisir.age()
    
    def modifier_moyenne(self) -> None:
        self.moyenne: float = saisir.moyenne()