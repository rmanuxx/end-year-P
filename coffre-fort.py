import generateur as ge 
import Chiffrement as ch
import base_de_donnee as db
import master_key   as key


def add_compte():
    while True:
        site = input("nom du site ou de l application  ")
        # .strip() c'est pour enlever les espaces
        site = site.strip()
        if site == "": # si le champs est vide 
            print('le nom du site est requis')
        else:
            break

    while True:
        id_client = input("entrez votre email ou votre nom d'utilisateur  ")
        id_client = id_client.strip()
        if id_client == "":#la meme chose que pour site 
            print("les identifiants (email ou nom d'utilisateur ) est requis  ")
        else:
            break

    # Génère ou sélectionne un mot de passe pour le compte
    mdp = ge.choisir()

    mdp_chiff = ch.chiffrement(mdp) # fais passer un "emanuel" en "fyczxalyvaxxxbmuzxxxauzm" elle le chiffre en gros

    note = input("Note optionnelle : ") # un petit commentaire ou quelque chose a savoir sur le mot de passe 

    db.ajout_comptedb(site,id_client,mdp_chiff,note)#apres recolte on ajoute tout ca a la base de donées

    print("compte ajouté avec succès à la base de données " )

    # ajouter ok

def voir_mdp(coffre):
    """Affiche les mots de passe enregistrés dans le coffre.

    Paramètres :
    coffre (list): Liste des comptes contenant les informations chiffrées.
    """
    comptes=db.voir_tous_comptes()
    if len(coffre) == 0: # si la db est vide 
        print("aucun mot de passe enregistré")
        return

    for compte in comptes:#on parcours chaque elements dns la base de donnée
        """un compte ressemble a ca (id,site,compte,identifiants,mdp,note)
        en sachant que id est à l indice 0
        ensuite on recupere tout """
        id_compte=compte[0]
        site=compte[1]
        identifiant=compte[2]
        mot_de_passe=compte[3]
        note=compte[4]

        mot_de_passe = ch.dechiffrement(mot_de_passe_chiffre)

        print("--------------------------")
        print("ID: ",id_compte )
        print("site:", site)
        print("identifiant: ", identifiant)
        print("mot de passe : ", mot_de_passe)
        print("--------------------------")


def rechercher_mdp(coffre, cle, recherche):
    recherche = input("Entrez le site ou l identifiant que vous chechez :  ")
    recherche = recherche.strip()
    
    comptes=db.rechercher_compte_db(recherche)
    """ c est le meme principe"""
    if len(comptes)==0:
        print("pas de compte correspondant")
        return
    for compte in comptes:

        id_compte=compte[0]
        site=compte[1]
        identifiant=compte[2]
        mot_de_passe_chiffre=compte[3]
        note=compte[4]

        mot_de_passe = ch.dechiffrement(mot_de_passe_chiffre)

        print("--------------------------")
        print("ID: ",id_compte )
        print("site:", site)
        print("identifiant: ", identifiant)
        print("mot de passe : ", mot_de_passe)
        if note :
            print("note: ",note)
        print("--------------------------")

def menu(): 
    db.creation_tablesql_pour_lesmdp()

    while True():
        print ("\n===+++===BIENVENUE DANS GESTIO!!===+++===")
        print ("1.Ajouter un mot de passe")
        print ("2.Voir tout les mots de passe")
        print ("3.Rechercher un mot de passe")
        print ("4.Quitter")

        choix =input ("Entrez un choix :  ")

        if choix==1: add_compte()
        elif choix == 2 : voir_mdp()
        elif choix == 3 : rechercher_mdp ()

if __name__=="__main__":
    menu()


