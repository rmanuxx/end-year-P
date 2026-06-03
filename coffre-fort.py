import generateur as ge 
import Chiffrement as ch


def add_compte():
    while True:
        site = input("nom du site ou de l application  ")
        # .strip() c'est pour enlever les espaces
        site = site.strip()
        if site == "":
            print('le nom du site est requis')
        else:
            break

    while True:
        id_client = input("entrez votre email ou votre nom d'utilisateur  ")
        id_client = id_client.strip()
        if id_client == "":
            print("les identifiants (email ou nom d'utilisateur ) est requis  ")
        else:
            break

    # Génère ou sélectionne un mot de passe pour le compte
    mdp = ge.choisir()
    mdp_chiff = ch.chiffrement(mdp)

    note = input("Note optionnelle : ")

    compte = {
        "site": site,
        "identifiant": id_client,
        "mot de passe": mdp_chiff,
        "note": note,
    }
    return compte


def voir_mdp(coffre):
    """Affiche les mots de passe enregistrés dans le coffre.

    Paramètres :
    coffre (list): Liste des comptes contenant les informations chiffrées.
    """
    if len(coffre) == 0:
        print("aucun mot de passe enregistré")
        return

    for compte in coffre:
        mot_de_passe_chiffre = compte.get("mot de passe")
        
        if isinstance(mot_de_passe_chiffre, bytes):
            mot_de_passe_chiffre = mot_de_passe_chiffre.decode('utf-8')

        mot_de_passe = ch.dechiffrement(mot_de_passe_chiffre)

        print("--------------------------")
        print("site:", compte.get("site"))
        print("identifiant:", compte.get("identifiant"))
        print("mot de passe : ", mot_de_passe)
        print("--------------------------")


def rechercher_mdp(coffre, cle, recherche):
    trouve = False

    for compte in coffre:
        site = compte.get("site", "").lower()
        
        ident = compte.get("identifiant", "").lower()
        
        if recherche.lower() in site or recherche.lower() in ident:
            mot_chiff = compte.get("mot de passe")
           
            if isinstance(mot_chiff, bytes):
                mot_chiff = mot_chiff.decode('utf-8')
            mot_de_passe = ch.dechiffrement(mot_chiff)

            print("--------------------------")
            print("site:", compte.get("site"))
            print("identifiant:", compte.get("identifiant"))
            print("mot de passe : ", mot_de_passe)
            print("--------------------------")

            trouve = True

    if trouve == False :
        print("Pas de compte correspondant")
