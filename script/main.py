from operation import ajouter_etudiants
import os
import pandas as pd
from saisir import valider_input


def initialiser_fichier(path: str) -> str:
    if os.path.exists(path):
        return f"Fichier {path} existe déjà."
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(path, mode="a")
    return f"Fichier {path} a été crée"


def afficher_fichier(path: str) -> str:
    if not os.path.exists(path):
        return f"Fichier {path} n'existe pas."
    return pd.read_csv(path)


def option3(path: str) -> str:
    if os.path.exists(path):
        return f"Fichier {path} existe déjà."
    df: pd.DataFrame = pd.read_csv(path)
    ajouter_etudiants(df)


def main() -> None:
    print("Menu:\n")
    print("1. Initialiser Fichier")
    print("2. Afficher Fichier")
    print("3. Ajouter Etudiants")
    print("4. Chercher Etudiants")
    print("5. Chercher Dans Fichier")
    print("6. Quitter")

    while True:
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 7),
            "Option non validé."
        )
    
        match choix:
            case "1":
                print(initialiser_fichier("data/etudiants.csv"))
            case "2":
                print(afficher_fichier("data/etudiants.csv"))
            case "3":
                print()


main()