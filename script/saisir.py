"""
Ce script valide les inputs de l'utilisateur en fonction du type de valeur attendue.
"""
from time import sleep

def valider_input(message: str, f_validation, message_erreur, convert_type=None):
    while True:
        valeur = input(message).strip()
        sleep(0.5)
        if f_validation(valeur):
            return convert_type(valeur) if convert_type else valeur
        print(message_erreur)


def nom() -> str:
    return " ".join(valider_input(
        "Saisie le nom de l'étudiant: ",
        lambda x: x.replace(" ", "").isalpha(),
        "Le nom n'est pas valide."
    ).split()).title()


def prénom() -> str:
    return " ".join(valider_input(
        "Saisie le prénom de l'étudiant: ",
        lambda x: x.replace(" ", "").isalpha(),
        "Le prénom n'est pas valide."
    ).split()).title()


def age() -> int:    
    return valider_input(
        "Saisie l'age de l'étudiant: ",
        lambda x: x.isdigit() and  0 < int(x) < 100,
        "L'age n'est pas valide.",
        int
        )


def moyenne() -> float:
    return round(
                valider_input(
                    "Saisie la moyenne de l'étudiant: ",
                    lambda x: x.replace(".", "", 1).isdigit() and  0 <= float(x) <= 20,
                    "La moyenne n'est pas valide.",
                    float
                ),
                2)