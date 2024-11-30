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


def chercher_etudiant(df: pd.DataFrame) -> pd.DataFrame:
    nom: str = saisir.nom()
    prénom: str = saisir.prénom()
    return df[(df["Nom"]==nom) & (df["Prénom"]==prénom)]


def filtrer_nom(df: pd.DataFrame, nom: str) -> pd.DataFrame:
    return df[df["Nom"] == nom]


def filtrer_age(df: pd.DataFrame, min_age: int, max_age: int = 99) -> pd.DataFrame:
    return df[max_age >= df["Age"] >= min_age]


def filtrer_moyenne(df: pd.DataFrame, min_moyenne: float, max_moyenne: float = 20) -> pd.DataFrame:
    return df[max_moyenne >= df["Moyenne"] >= min_moyenne]


def calculer_moyenne_generale(df: pd.DataFrame) -> float:
    return df["Moyenne"].mean()