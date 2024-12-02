import operation
import os
import pandas as pd
from saisir import valider_input
import sys
from time import sleep


def menu_option(*args) -> None:
    return "\n".join(args)


def option1(path: str) -> str:
    if os.path.exists(path):
        return f"Le tableau existe déjà."
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(path, index=False)
    return f"Le Tableau a été crée."


def option2(path: str) -> str:
    if not os.path.exists(path):
        return f"Ce tableau n'existe pas"
    return pd.read_csv(path)


def option3(path: str) -> str:
    if not os.path.exists(path):
        return f"Fichier {path} n'existe déjà.\n Vous devez créer un fichier."
    df: pd.DataFrame = pd.read_csv(path)
    operation.ajouter_etudiants(df, path)


def option4(path: str) -> str:
    if not os.path.exists(path):
        return f"Fichier {path} n'existe déjà.\n Vous devez créer un fichier."
    df: pd.DataFrame = pd.read_csv(path)
    return operation.chercher_etudiant(df)


def interface(message: str, durée: int, fonction):
    print(message)
    sleep(durée)
    print(fonction)

def main() -> None:
    print(
        menu_option(
            "Menu \n",
            "1. Initialiser Tableau",
            "2. Afficher Tableau",
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
                tableau: str = input("Saisie le nom du tableau: ")
                interface("Création du tableau...", 1.5, option1(f"data/{tableau}.csv"))
            case "2":
                tableau: str = input("Saisie le nom du tableau que vous voulez afficher: ")
                interface("Affichage de tableau...", 1.5, option2(f"data/{tableau}.csv"))
            case "3":
                option3("data/etudiants.csv")
            case "4":
                print(option4("data/etudiants.csv"))
            case "5":
                print("Fermeture d'application...")
                sleep(1.5)
                sys.exit()

main()