from etudiants import Etudiant
import pandas as pd
import saisir


def ajouter_etudiants(df: pd.DataFrame) -> None:
    while True:
        étudiant = Etudiant()
        nom: str = étudiant.nom
        prénom: str =  étudiant.prénom
        age: int = étudiant.age
        moyenne: float = étudiant.moyenne
        df.loc[len(df)] = [nom, prénom, age, moyenne]


def chercher_etudiant(df: pd.DataFrame):
    nom: str = saisir.nom()
    prénom: str = saisir.prénom()
    return df[(df["Nom"]==nom) & (df["Prénom"]==prénom)]
