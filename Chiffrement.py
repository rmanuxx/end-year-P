from cryptography.fernet import Fernet
import os

FICHIER_CLE = "cle.cle"

def creation_key():
    """Crée une clé secrète si elle n'existe pas déjà."""
    if not os.path.exists(FICHIER_CLE):
        cle = Fernet.generate_key()
        with open(FICHIER_CLE, "wb") as fichier:
            fichier.write(cle)
            # les clés seront écrites en binaire pour ne pas être en clair


def charg_cle():
    with open(FICHIER_CLE, "rb") as fichier:
        # permet de lire le fichier avec la cle correspondante
        return fichier.read()


def chiffrement(mdp):
    creation_key()
    cle = charg_cle()
    fernet = Fernet(cle)
    chiffrement = fernet.encrypt(mdp.encode())
    return chiffrement.decode()


def dechiffrement(mdp_chiff):
    cle = charg_cle()
    f = Fernet(cle)
    dechiffrement = f.decrypt(mdp_chiff.encode())
    return dechiffrement.decode()


if __name__ == "__main__":
    mdp = "manuel777"
    mdp_chiff = chiffrement(mdp)
    print(mdp_chiff)
    print(dechiffrement(mdp_chiff))
