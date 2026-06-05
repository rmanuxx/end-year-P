import hashlib 
import os 

MAITREEEEE="maitre.txt"

def hachage_mot_de_passe_maitre(mot_de_passe):
    """1.on formate le texte pour avoir un format utile au hashage vu que le text ça passe pas
    2.sha256 est une methode de hashage (https://emn178.github.io/online-tools/sha256.html) 
    3. hexdigest  transforme le resultat en quelque chose de lisible"""
    mdp=mot_de_passe.encode()
    mdp_hash=hashlib.sha256(mdp).hexdigest()
    return mdp_hash 

def creation_mdp_maitre():
    if os.path.exists(MAITREEEEE):#verifie si le fichier est deja disponible , si oui la fonction s arrete d ou le return  rien 
        return
    print("Aucun mot de passe maitre maitre configurée")
    print("creation d'un mot de passe maitre...")

    while True : 
        mdp1=input("Entrez un mot de passe")
        mdp2=input("confirmer le mot de passe maitre ")

        if mdp1 == "" or mdp2 == "" : 
            print("veuillez remplir les deux champs") # si l un des champs est vide 
        elif mdp1 != mdp2 :
            print("Les mots de passes ne correspondent pas") # si ils ne correspondent pas
        else :
            mdp_hashe= hachage_mot_de_passe_maitre(mdp1) #ensuite si tout est bon le mdp est hashé

            with open(MAITREEEEE,"w") as maitre :# il ouvre le fichier et ecrit la master key
                maitre.write(mdp_hashe)

            print("Mot de passe maitre configuré avec succes ")
            break

def  verification_mdp_maitre():
     creation_mdp_maitre()
     """1. on lis le fichier 
        2. ensuite on demande a l utilisateur de proposer ce qu'il a
        3. on ne compare pas les deux mots de passe
        4.on le hash et on compare qui sont dans le fichier
        5. Il a trois essaie avant que ça se bloque """
     with open(MAITREEEEE,"r") as maitre :
        mdp_enregistree = maitre.read()

     for test in range(3):
        mdp = input("entrez le mots de passe : ")
        mdp_chiff=hachage_mot_de_passe_maitre(mdp)

        if mdp_chiff == mdp_enregistree:
            print("Accès authorized")
            return True

        else : 
            print("hmm recommence")
     print("trop de tentative , Acces unauthorized")
     return False
    



