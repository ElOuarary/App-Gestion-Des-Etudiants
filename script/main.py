import operation
import os
import pandas as pd
from saisir import valider_input
import sys
from time import sleep


def menu_option(*args) -> None:
    return "\n".join(args)


def interface(message: str, durée: int):
    print(message)
    sleep(durée)


def option1(path: str) -> str:
    if os.path.exists(path):
        print(f"Le tableau existe déjà.")
        return
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(path, index=False)
    print(f"Le Tableau a été crée.\n")


def option2(path: str) -> str:
    if not os.path.exists(path):
        print(f"Vous devez initialiser un tableau.\n")
        return
    
    while True:
        print(menu_option(
            "1. Tableau",
            "2. Etudiant",
            "3. Moyenne",
            "4. Retour"
        ))

        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 5),
            "Option non validé."
        )
        
        df: pd.DataFrame =  pd.read_csv(path)
        match choix:
            case "1":
                interface("Affichage du tableau...", 1.5)
                print(df)
            case "2": 
                operation.chercher_etudiant(df)
            case "3":
                operation.chercher_note(df)
            case "4":
                return


def option3(path: str) -> None:
    if not os.path.exists(path):
        print(f"Vous devez initialiser un tableau.\n")
        return
    df: pd.DataFrame = pd.read_csv(path)
    operation.ajouter_etudiants(df, path)


def option4(path: str) -> str:
    if not os.path.exists(path):
        print(f"Vous devez initialiser un tableau.\n")
        return
    df: pd.DataFrame = pd.read_csv(path)
    operation.chercher_etudiant(df)


def option5(path: str) -> None:
    if not os.path.exists(path):
        print(f"Vous devez initialiser un tableau.\n")
        return
    df: pd.DataFrame = pd.read_csv(path)
    operation.calculer_moyenne_génerale(df)


def option6(path: str) -> str:
    if not os.path.exists(path):
            print("Vous devez initialiser un tableau.\n")
            return
    
    while True:
        print(menu_option(
            "1. Tableau",
            "2. Etudiant",
            "3. Retour"
        ))
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 4),
            "Option non validé."
        )
        df: pd.DataFrame = pd.read_csv(path)
        match choix:
            case "1":
                interface("Supprimage du tableau...", 1.5, os.remove(path))
                print("Tableau supprimé avec succés.")
            case "2":
                print(operation.supprimer_étudiants(df))
            case "3":
                return


def main() -> None:
    path: str = "data/étudiants.csv" 
    while True:
        print(
            menu_option(
                "Menu\n",
                "1. Initialiser Tableau",
                "2. Afficher",
                "3. Ajouter Etudiant",
                "4. Rechercher",
                "5. Calculer Moyenne Génerale",
                "6. Supprimer",
                "7. Quitter"
            )
        )

        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 8),
            "Option non validé."
        )
    
        match choix:
            case "1":
                interface("Création du tableau...", 1.5)
                option1(path)
            case "2":
                option2(path)
            case "3":
                print(option3(path))
            case "4":
                print(option4(path))
            case "5":
                interface("Calcule de moyenne génerale des étudiants...", 1)
                option5(path)
            case "6":
                option6(path)
            case "7":
                print("Fermeture d'application...")
                sleep(1.5)
                sys.exit()

main()