from etudiants import Etudiant
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
            break


def chercher_etudiant(df: pd.DataFrame) -> None:
    nom: str = saisir.nom()
    prénom: str = saisir.prénom()
    étudiant_existe: bool = df[(df["Nom"]==nom) & (df["Prénom"]==prénom)].empty
    if not étudiant_existe:
        print(f"{df[(df["Nom"]==nom) & (df["Prénom"]==prénom)]}")
        modifier_étudiant(df, nom, prénom)
        modifier_note(df, nom, prénom)
    else:
        print(f"L'etudiant {nom} {prénom} n'existe pas dans le tableau.")


def chercher_note(df: pd.DataFrame) -> pd.DataFrame:
    moyenne: float = saisir.moyenne()
    moyenne_existe: bool = df[df["Moyenne"]==moyenne].empty
    if moyenne_existe:
        print(f"Le tableau ne contient aucune moyenne {moyenne}")
    else:
        print(df[df["Moyenne"]==moyenne])


def modifier_étudiant(df: pd.DataFrame, nom: str, prénom: str):
    while True:
        reponce: str = saisir.valider_input(
            f"Vous voulez modifier le nom et le prénom de l'étudiant '{nom} {prénom}' [Y/N]: ",
            lambda x: x.upper() in ["Y", "N"],
            "Option non validé."
        )
        if reponce.upper() == "N":
            break
        nouveau_nom: str = saisir.nom()
        nouveau_prénom: str = saisir.prénom()

        df.loc[df["Nom"]==nom, "Nom"] = nouveau_nom
        df.loc[df["Prénom"]==prénom, "Prénom"] = nouveau_prénom
        df.to_csv("data/étudiants.csv", index_label=False, index=False)
        print("Modification avec succée.")
        return


def modifier_note(df: pd.DataFrame, nom: str, prénom: str):
    while True:
        reponce: str = saisir.valider_input(
            f"Vous voulez modifier la moyenne de l'étudiant '{nom} {prénom}' [Y/N]: ",
            lambda x: x.upper() in ["Y", "N"],
            "Option non validé."
        )
        if reponce.upper() == "N":
            break
        nouveau_moyenne: float = saisir.moyenne()

        df.loc[(df["Nom"]==nom) & (df["Prénom"]==prénom), "Moyenne"] = nouveau_moyenne
        df.to_csv("data/étudiants.csv", index_label=False, index=False)
        print("Modification avec succée.")
        return



def supprimer_étudiants(df: pd.DataFrame) -> str:
    nom: str = saisir.nom()
    prénom: str = saisir.prénom()
    étudiant_existe: bool = df[(df["Nom"]==nom) & (df["Prénom"]==prénom)].empty
    if not étudiant_existe:
        df.drop(df[(df["Nom"]==nom) & (df["Prénom"]==prénom)].index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv("data/étudiants.csv")
        return f"L'etudiant {nom} {prénom} a été supprimé du tableau avec succés."
    return f"L'etudiant {nom} {prénom} n'existe pas dans la liste."


def filtrer_nom(df: pd.DataFrame, nom: str) -> pd.DataFrame:
    return df[df["Nom"] == nom]


def filtrer_age(df: pd.DataFrame, min_age: int, max_age: int = 99) -> pd.DataFrame:
    return df[(max_age >= df["Age"]) & (df["Age"] >= min_age)]


def filtrer_moyenne(df: pd.DataFrame, min_moyenne: float, max_moyenne: float = 20) -> pd.DataFrame:
    return df[(max_moyenne >= df["Moyenne"]) & (df["Moyenne"]>= min_moyenne)]


def calculer_moyenne_génerale(df: pd.DataFrame) -> None:
    if df.empty:
        print("Aucune donnée disponible pour calculer la moyenne.")
    print(f"La moyenne génerale est: {df["Moyenne"].mean()}")