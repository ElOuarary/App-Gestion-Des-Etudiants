from etudiants import Etudiant
import keyboard
import pandas as pd
import saisir


def ajouter_etudiants(df: pd.DataFrame) -> None:
    while True:
        étudiant = Etudiant()
        nom: str = étudiant.nom
        prénom: str =  étudiant.prénom
        age: int = étudiant.age
        moyenne: float = étudiant.moyenne
        nouveau_étudiant = pd.Series({"Nom": nom, "Prénom": prénom, "Age": age, "Moyenne": moyenne})
        if ((df == nouveau_étudiant).all(axis=1)).any():
            print(f"Etudiant {nom} {prénom} existe déjà.")
            continue
        df.loc[len(df)] = [nom, prénom, age, moyenne]
        print(f"Etudiant {nom} {prénom} ajouté avec succés.")

        print(f"Si tu veux ajouter un autre étudiant clique sur 'entrée', sinon clique sur n'import quelle touche")
        if not keyboard.is_pressed("enter"):
            break



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