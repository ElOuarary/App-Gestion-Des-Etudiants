from operation import ajouter_etudiants
import os
import pandas as pd
from saisir import valider_input
import sys


def option1(path: str) -> str:
    if os.path.exists(path):
        return f"Fichier {path} existe déjà."
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(path, mode="a")
    return f"Fichier {path} a été crée"


def option2(path: str) -> str:
    if not os.path.exists(path):
        return f"Fichier {path} n'existe pas."
    return pd.read_csv(path)


def option3(path: str) -> str:
    if not os.path.exists(path):
        return f"Fichier {path} n'existe déjà.\n Vous devez créer un fichier."
    df: pd.DataFrame = pd.read_csv(path)
    ajouter_etudiants(df, path)


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
                print(option1("data/etudiants.csv"))
            case "2":
                print(option2("data/etudiants.csv"))
            case "3":
                option3("data/etudiants.csv")
            case "6":
                print("Fermeture d'application")
                sys.exit()

main()