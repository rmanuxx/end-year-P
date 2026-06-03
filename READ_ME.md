# projet 1 :gestionnaire de mot de passe python

&#x20;

### présentation des rapide des modules





* voila on commence la conception d un projet python liant **SQLite** pour la base de donnée
* la bibliothèque **cryptographie** pour le chiffrement
* **PyQt** ou **t-kinter** je ne me suis pas encore décider sur la bibliothèque du GUI (interface utilisateur) mais je pense aller sur PyQt
* apprendre la bibliothèque secret pour la génération de mots de passes fort
* a venir…

## créer l interface 





………… en développement 



## ce qu'on attends de cette application



l application doit être capable de :



* ### ajouter des mots de passes
* on va donner chaque détail ou mise à jour pour la fonction add\_mdp()



* #### voir les mots de passes ( les déchiffrer )
* on va donner chaque détail ou mise à jour pour la fonction **see\_mdp()**

&#x20;

* #### modifier les mots de passes
* on va donner chaque détail ou mise à jour pour la fonction **mod\_mdp()**



* #### supprimer les mots de passes
* on va donner chaque détail ou mise à jour pour la fonction **rmv\_mdp()**



* #### rechercher les mots de passes
* on va donner chaque détail ou mise à jour pour la fonction **sea\_mdp()**



* #### générer des mots passes forts
* on va donner chaque détail ou mise à jour pour la fonction **generate\_mdp**
* il fonctionne de la manière suivante :

&#x20;   on va utiliser string : pour avoir une listes de tout les caractères disponible(chiffres , lettres , spéciaux )

&#x20;   on utilise secret pour tout ce qui va toucher a l aléatoire ou le pseudo aléatoire

&#x20;   on va générer un mot de passe hexadécimal

&#x20;   on ajoute 4 caractère de chaque type  pour chaque type de caractères donc il va nous rester encore 12 a compléter

&#x20;   vu qu'on va pas répéter l action plusieurs fois on va utiliser une boucle **for**  qui va choisir un élément au hasard de type aléatoire aussi

&#x20;   assez pour compléter la longueur

&#x20;   maintenant qu'on a nos 16 caractères on va les mélanger pour éviter qu'ils soient à la même place

&#x20;

&#x20;  j ai ajoute l option de choisir sois meme son mot de passe avec un evaluateur de securite

&#x20;

&#x20;

* ###### gestion d erreur

&#x20;

&#x20;   et si quelqu'un  utilise ma fonction n'importe comment

&#x20;

&#x20;   et si un nombre trop petit était entrer dans la fonction = le mot passes générer est toujours hexadécimal donc ok

&#x20;   et si quelqu'un n entre pas le bon type de donnée = c est ok

&#x20;   et si la valeur n est pas positive  =  c est réglé

&#x20;

&#x20;





&#x20;

* #### copier ses mots de passes
* &#x20;on va donner chaque détail ou mise à jour pour la fonction   **copy\_mdp()**







## Structure du projet



Gestionnaire de mot de passes

|

|\_\_main.py ( la fonction principale )

|

|\_\_base\_de\_donnée.py

|

|\_\_chiffrement.py

|

|\_\_generation\_mdp.py

|

|\_\_coffre-fort.dB





…possible évolution création d un petit serveur personnelle pour pouvoir accéder a mes mots de passes partout

