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
        return f"Le tableau n'est pas crée vous devez crée un."
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

def option5(path: str) -> str:
    if not os.path.exists(path):
        return f"Vous devez initialiser un tableau."
    df: pd.DataFrame = pd.read_csv(path)
    return operation.calculer_moyenne_génerale(df)


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
            "5. Calculer Moyenne Génerale",
            "6. Quitter"
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
                interface("Création du tableau...", 1.5, option1("data/etudiants.csv"))
            case "2":
                interface("Affichage de tableau...", 1.5, option2("data/etudiants.csv"))
            case "3":
                print(option3("data/etudiants.csv"))
            case "4":
                print(option4("data/etudiants.csv"))
            case "5":
                interface("Calcule de moyenne génerale des étudiants...", 1, option5("data/etudiants.csv"))
            case "6":
                print("Fermeture d'application...")
                sleep(1.5)
                sys.exit()

main()