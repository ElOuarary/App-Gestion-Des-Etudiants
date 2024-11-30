"""
Ce script valide les inputs de l'utilisateur en fonction du type de valeur attendue.
"""


def valider_input(message: str, f_validation, message_erreur):
    while True:
        valeur = input(message).strip()
        if f_validation(valeur):
            return valeur
        print(message_erreur)


def nom() -> str:
    return valider_input(
        "Saisie le nom de l'étudiant: ",
        lambda x: x.isalpha(),
        "Le nom n'est pas valide."
    )


def prénom() -> str:
    return valider_input(
        "Saisie le prénom de l'étudiant: ",
        lambda x: x.isalpha(),
        "Le prénom n'est pas valide."
    )


def age() -> int:
    return int(valider_input(
        "Saisie l'age de l'étudiant: ",
        lambda x: x.isdigit() and  0 < int(x) < 100,
        "L'age n'est pas valide."
    ))


def moyenne() -> float:
    return round(
        float(
            valider_input(
                "Saisie la moyenne de l'étudiant: ",
                lambda x: x.replace(".", "", 1).isdigit() and  0 <= float(x) <= 20,
                "La moyenne n'est pas valide."
            )
            ),
        2)