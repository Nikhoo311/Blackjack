def affichage(liste):
    """ Affichage dynamique des menus
        Entrée : liste de chaines de caractère contenant l'affiche du menu en question
        Sortie : Affiche un menu fonctionnel et renvoie un entier correspondant a l'action choisie
    """
    for ligne in liste:
        print(ligne)



def initMenu():
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
    initMenu()


def MontantBanque():
    """
        Affiche le menu pour le montant de la banque du joueur
        Sortie : Renvoie un entier du montant de la banque
    """
    affichage(['========== Montant de la Banque ==============\n\t1- 100€','\n\t2- 250€\n\t3- 500€','\n\t4- Personnaliser\n==============================================='])
    initMenu()