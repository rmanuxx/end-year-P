import string as st  # string provides characters: digits, letters, symbols
import secrets as se  # selection more secure than random
import random as ra  # library for simple randomness


def generate_mdp(longueur=16):
    # pour eviter les erreur du genre mauvais type ou autre
    try:
        longueur = int(longueur)
        if longueur < 4:
            print("Attention : La longueur doit être d'au moins 4. Utilisation de la longueur par défaut (16).")
            longueur = 16
    except (ValueError, TypeError):
        print("Attention : La longueur fournie est invalide. Utilisation de la longueur par défaut (16).")
        longueur = 16

    minuscules = st.ascii_lowercase
    majuscules = st.ascii_uppercase
    chiffres = st.digits
    symboles = st.punctuation

    ensemble = minuscules + majuscules + chiffres + symboles
    # on melange tout pour creer une grosse boite avec tout les type de caractere

    password = []
    password.append(se.choice(minuscules))
    password.append(se.choice(majuscules))
    password.append(se.choice(chiffres))
    password.append(se.choice(symboles))
    # pour le reste, une boucle va s'en occuper
    for i in range(longueur - 4):
        choix = se.choice(ensemble)
        password.append(choix)

    # Melange sans repetition
    password = ra.sample(password, len(password))
    final_password = "".join(password)
    return final_password


def evaluation_mdp(mot):
    score = 0
    if len(mot) >= 12:
        score += 1
    if any(i.islower() for i in mot):
        score += 1
    if any(i.isupper() for i in mot):
        score += 1
    if any(i.isdigit() for i in mot):
        score += 1
    if any(i in st.punctuation for i in mot):
        score += 1

    if score <= 2:
        return 'faible, je vous déconseille de le garder'
    elif score <= 4:
        return "moyen"
    else:
        return "fort"


def choisir():
    while True:
        print("1. Générer un mot de passe sécurisé\n2. Choisir un mot de passe personnalisé")
        choix = input("Votre choix (1 ou 2) : ")

        if choix == "1":
            while True:
                try:
                    longueur = int(input("Longueur du mot de passe : "))
                    password = generate_mdp(longueur)
                    print(f"Votre mot de passe sécurisé : {password}")
                    return password
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre entier valide supérieur ou égal à 4.")
                except TypeError as e:
                    print(f"Erreur : {e}")
        elif choix == "2":
            password = input('Entrez votre mot de passe : ')
            level = evaluation_mdp(password)
            print(f"Niveau de sécurité: {level}")
            return password
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.\n")


if __name__ == "__main__":
    choisir()
