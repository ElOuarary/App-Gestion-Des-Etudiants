from etudiants import Etudiant
import keyboard
import pandas as pd
import saisir


def ajouter_etudiants(df: pd.DataFrame, path: str) -> None:
    while True:
        étudiant = Etudiant()
        nom: str = étudiant.nom
        prénom: str =  étudiant.prénom
        age: int = étudiant.age
        moyenne: float = étudiant.moyenne
        nouveau_étudiant = pd.Series({"Nom": nom, "Prénom": prénom, "Age": age, "Moyenne": moyenne})
        if (df.apply(lambda row: row.equals(nouveau_étudiant), axis=1)).any():
            print(f"Etudiant {nom} {prénom} existe déjà.")
            continue
        df = pd.concat([df, nouveau_étudiant.to_frame().T], ignore_index=False)
        print(f"Etudiant {nom} {prénom} ajouté avec succés.")

        print(f"Si tu veux ajouter un autre étudiant clique sur 'entrée', sinon clique sur n'import quelle touche")
        while True:
            if keyboard.is_pressed("enter"):
                break
            elif not keyboard.is_pressed("enter"):
                df.to_csv(path)
                return


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