from etudiants import Etudiant
import keyboard
import pandas as pd
import saisir


def ajouter_etudiants(df: pd.DataFrame, path: str) -> None:
    while True:
        étudiant = Etudiant()

        nouveau_étudiant = pd.Series({
            "Nom": étudiant.nom,
            "Prénom": étudiant.prénom,
            "Age": étudiant.age,
            "Moyenne": étudiant.moyenne})
        
        if not df[(df["Nom"] ==  étudiant.nom) & (df["Prénom"] == étudiant.prénom)].empty:
            print(f"Etudiant {étudiant.nom} {étudiant.prénom} existe déjà.")
            continue

        df = pd.concat([df, nouveau_étudiant.to_frame().T], ignore_index=True)
        print(f"Etudiant {étudiant.nom} {étudiant.prénom} a été ajouté avec succès.")

        continuer = input("Appuyez sur 'Entrée' pour continuer ou une autre touche pour quitter: ")
        if continuer.strip() != "":
            try:
                df.to_csv(path, index=False)
                print("Données sauvegardées avec succès.")
            except Exception as e:
                print(f"Erreur lors de la sauvegarde des données: {e}")
            return


def chercher_etudiant(df: pd.DataFrame) -> pd.DataFrame:
    nom: str = saisir.nom()
    prénom: str = saisir.prénom()
    étudiant_existe: bool = df[(df["Nom"]==nom) & (df["Prénom"]==prénom)].empty
    if not étudiant_existe:
        return f"{df[(df["Nom"]==nom) & (df["Prénom"]==prénom)]}"
    return f"L'etudiant {nom} {prénom} n'existe pas dans la liste."


def filtrer_nom(df: pd.DataFrame, nom: str) -> pd.DataFrame:
    return df[df["Nom"] == nom]


def filtrer_age(df: pd.DataFrame, min_age: int, max_age: int = 99) -> pd.DataFrame:
    return df[(max_age >= df["Age"]) & (df["Age"] >= min_age)]


def filtrer_moyenne(df: pd.DataFrame, min_moyenne: float, max_moyenne: float = 20) -> pd.DataFrame:
    return df[(max_moyenne >= df["Moyenne"]) & (df["Moyenne"]>= min_moyenne)]


def calculer_moyenne_generale(df: pd.DataFrame) -> float:
    if df.empty:
        print("Aucune donnée disponible pour calculer la moyenne.")
        return 0.0
    return df["Moyenne"].mean()