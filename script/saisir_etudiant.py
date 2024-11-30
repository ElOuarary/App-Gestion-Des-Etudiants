"""
Ce scipt a pour but d'ajouter etudiants avec leurs informations
"""

from etudiants import Etudiant


def ajouter_étudiant():
    nom: str = input("Saisie le nom d'etudiant: ")
    prénom: str = input("Saisie le prénom d'étudiant: ")
    age: int = input("Saisie l'age de l'etudiant: ")
    moyenne: float = input("Saisie la moyenne de l'etudiant: ")
    print(f"Etudiant ajouter")
    print(f"{nom} {prénom} {age} {moyenne}")

ajouter_étudiant()