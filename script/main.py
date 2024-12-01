from operation import ajouter_etudiants
import os
import pandas as pd
from saisir import valider_input
import sys


def menu_option(*args) -> None:
    return "\n".join(args)

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
    print(
        menu_option(
            "Menu \n",
            "1. Initialiser Fichier",
            "2. Afficher Fichier",
            "3. Ajouter Etudiant",
            "4. Rechercher Etudiant",
            "5. Quitter"
                    )
        )
 
    while True:
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 6),
            "Option non validé."
        )
    
        match choix:
            case "1":
                print(option1("data/etudiants.csv"))
            case "2":
                print(option2("data/etudiants.csv"))
            case "3":
                option3("data/etudiants.csv")
            case "5":
                print("Fermeture d'application")
                sys.exit()

main()