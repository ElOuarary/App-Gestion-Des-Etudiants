import pandas as pd
from operation import ajouter_etudiants


def main() -> None:
    # Initialiser le dataFrame où les informations des étudiants vont être stocké
    columns: list[str] = ["Nom", "Prénom", "Age", "Moyenne"]
    df = pd.DataFrame(columns=columns)
    
    print("Menu:\n")
    print("1. Initialiser Fichier")
    print("2. Afficher Fichier")
    print("3. Ajouter Etudiants")
    print("4. Chercher Etudiants")
    print("5. Chercher Dans Fichier")
    print("6. Quitter")