import sqlite3

DATA="coffre.db"

def creation_tablesql_pour_lesmdp():
    connexion = sqlite3.connect(DATA)
    #connect va creer le fichier si il n existe pas deja
    #et connecter la base de donnée
    control=connexion.cursor()
    #cursor permet d executer des commandes sqlite

    control.execute("""
    CREATE TABLE IF NOT EXISTS mdp_utilisitateur(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Service TEXT NOT NULL,
    identifiant TEXT NOT NULL,
    mot_de_passe TEXT NOT NULL,
    note TEXT
    )
    """)
    #NOT NULL pour dire que ce sont des donnée obligatoires 

    connexion.commit()
    #va valider et sauvegarder 
    connexion.close()
    #fermeture et deconnexion de la base de donnée

def ajout_comptedb(Service,identifiant,mot_de_passe,note=""):
    creation_tablesql_pour_lesmdp()
    connexion=sqlite3.connect(DATA)
    control =connexion.cursor()

    control.execute("""INSERT INTO
 mdp_utilisitateur(Service,identifiant,mot_de_passe,note)
 VALUES(?,?,?,?)""",(Service,identifiant,mot_de_passe,note))

    connexion.commit()
    connexion.close()


def voir_tous_comptes():
    creation_tablesql_pour_lesmdp()

    connexion=sqlite3.connect(DATA)
    
    control = connexion.cursor()

    control.execute("""
    SELECT id,Service,identifiant,mot_de_passe,note
    FROM mdp_utilisitateur""")

    comptes= control.fetchall()
    connexion.close()
    return comptes
    