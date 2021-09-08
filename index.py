def affichage(liste):
    """ Affichage dynamique des menus
        Entrée : liste de chaines de caractère contenant l'affiche du menu en question
        Sortie : Affiche un menu fonctionnel et renvoie un entier correspondant a l'action choisie
    """
    for ligne in liste:
        print(ligne)



def initMenu():
    """ Partie dynamique du menu avec 4 options possibles
        Sortie : Renvoie un entier correspondant a l'action choisie du menu en question
    """
    isCorrect = False
    while not(isCorrect):
        rep = input('Quel fonctinnalité ?: ')
        # si la reponse est bien un entier
        try:
            int(rep)
            # si la valeur reponse n'est pas comprise dans l'intervalle [1;4]
            if int(rep) < 1 or int(rep) > 4:
                print('Veuillez saisir une valeur correcte !')
                isCorrect = False
                pass
            else:
                return int(rep)
        except ValueError:
            # si la valeur n'est pas un entier
            print('Veuilllez mettre un nombre entier !')
            isCorrect = False

# Création de l'interface utilisateur
def menu():
    """
        Menu navigble pour sélectionner une fonctionnalité du jeu
        Sortie : Affichage du menu et renvoie un int / entier
    """
    affichage(['========================\n\t1- Jouer une partie','\n\t2- Montant de la banque\n\t3- Statistiques','\n\t4- Quitter\n========================'])
    # conditions pour toutes les fonctionnalitées du menu
    rep = initMenu()
    if rep == 1:
        print("La partie vient de commencer !")
    elif rep == 2:
        montantBanque()
    elif rep == 3:
        print('ICI les statistiques de toutes les parties jouer !')
    elif rep == 4:
        quit()

def montantBanque():
    """
        Affiche le menu pour le montant de la banque du joueur
        Sortie : Renvoie un entier du montant de la banque
    """
    affichage(['========== Montant de la Banque ==============\n\t1- 100€','\n\t2- 250€\n\t3- 500€','\n\t4- Personnaliser\n==============================================='])
    rep = initMenu()
    # Pour 100€
    if rep == 1:
        banque = 100
        return banque
    # Pour 250€
    elif rep == 2:
        banque = 250
        return banque
    # Pour 500 #
    elif rep == 3:
        banque = 500
        return banque
    # Montant personnaliser
    elif rep == 4:
        isCorrect =  False
        while not(isCorrect):
            montant = input("Quel budget voulez-vous mettre dans votre banque : ")
            try:
                # Voir si la convertion c'est bien faite
                int(montant)
                banque = int(montant)
                # retourne le montant de la banque / porte-monnaie du joueur
                return banque
            except ValueError:
                print('Veuilllez mettre un nombre entier !')
                isCorrect = False
