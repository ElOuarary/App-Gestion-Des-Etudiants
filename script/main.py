import operation
import os
import pandas as pd
from saisir import valider_input
import sys
from time import sleep


def menu_option(*args) -> None:
    return "\n".join(args)


def interface(message: str, durée: int, fonction):
    print(message)
    sleep(durée)
    print(fonction)


def option1(path: str) -> str:
    if os.path.exists(path):
        print(f"Le tableau existe déjà.")
        main()
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(path, index=False)
    print(f"Le Tableau a été crée.\n")
    main()


def option2(path: str) -> str:
    print(menu_option(
        "1. Tableau",
        "2. Etudiant",
        "3. Moyenne",
        "4. Retour"
    ))
    while True:
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 5),
            "Option non validé."
        )
        
        if not os.path.exists(path):
            print(f"Vous devez initialiser un tableau.\n")
            main()
        df: pd.DataFrame =  pd.read_csv(path)
        match choix:
            case "1":
                interface("Affichage du tableau...", 1.5, df)
            case "2": 
                operation.chercher_etudiant(df)
            case "3":
                operation.chercher_note(df)
            case "4":
                pass
        print()
        main()


def option3(path: str) -> str:
    if not os.path.exists(path):
        return f"Vous devez initialiser un tableau.\n"
    df: pd.DataFrame = pd.read_csv(path)
    operation.ajouter_etudiants(df, path)
    print()
    main()


def option4(path: str) -> str:
    if not os.path.exists(path):
        print(f"Vous devez initialiser un tableau.\n")
        main()
    df: pd.DataFrame = pd.read_csv(path)
    operation.chercher_etudiant(df)
    print()
    main()


def option5(path: str) -> None:
    if not os.path.exists(path):
        return f"Vous devez initialiser un tableau.\n"
    df: pd.DataFrame = pd.read_csv(path)
    operation.calculer_moyenne_génerale(df)
    print()
    main()


def option6(path: str) -> str:
    print(menu_option(
        "1. Tableau",
        "2. Etudiant",
        "3. Retour"
    ))
    while True:
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 4),
            "Option non validé."
        )
        if not os.path.exists(path):
            print("Vous devez initialiser un tableau.\n")
            main()
        df: pd.DataFrame = pd.read_csv(path)
        match choix:
            case "1":
                interface("Supprimage du tableau...", 1.5, os.remove(path))
                print("Tableau supprimé avec succés.")
            case "2":
                print(operation.supprimer_étudiants(df))
            case "3":
                pass
        print()
        main()


def main() -> None:
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
 
    while True:
        choix: str = valider_input(
            "Choisir une option: ",
            lambda x: x.isdigit() and int(x) in range(1, 8),
            "Option non validé."
        )
    
        match choix:
            case "1":
                interface("Création du tableau...", 1.5, option1("data/étudiants.csv"))
            case "2":
                option2("data/étudiants.csv")
            case "3":
                print(option3("data/étudiants.csv"))
            case "4":
                print(option4("data/étudiants.csv"))
            case "5":
                interface("Calcule de moyenne génerale des étudiants...", 1, option5("data/étudiants.csv"))
            case "6":
                option6("data/étudiants.csv")
            case "7":
                print("Fermeture d'application...")
                sleep(1.5)
                sys.exit()

main()