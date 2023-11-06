import Kevin.Basic_morpion as basic
import Kevin.Morpion2 as multi
import Kevin.Random_morpion as rdm
import Moeru.Master_morpion as master
import Moeru.Mega_morpion as mega

def morpion():
    ''' paramètres - Fonctions des différents morpions (imports)
    return - Jeu du Master Morpion '''
    
    print("- MORPION -")
    print("\n1 - Morpion basique \n2 - Master morpion \nChoix du mode de jeu :")
    mode = int(input('> '))

    if mode not in [1, 2]:
        print("\nChoix invalide \n")
        morpion()

    else:
        if mode == 2: # taille de grille (master morpion)
            print("\nChoix de la taille de grille (100 ou 250)")
            size = int(input('> '))
            size = 100 if size not in [100, 250] else size

            print("\nPs : Pour des raisons de tailles de grille, il est recommandé de suivre l'attribution des cases à l'aide d'une feuille")

        print("\n1 - Ordinateur \n2 - Joueur 2 \nChoix de l'adversaire :")
        adv = int(input('> '))

        if adv not in [1, 2]:
            print("\nChoix invalide \n")
            morpion()

        elif adv == 1:
            print("\n1 - Normal \n2 - Facile \nChoix du niveau de l'ordinateur :")
            lvl = int(input('> '))

            if lvl not in [1, 2]:
                print("\nChoix invalide \n")
                morpion()

            elif lvl == 1: # Morpions contre l'ordinateur (normal)
                if mode == 1:
                    result = basic.basic_morpion()

                else:
                    result = mega.mega_morpion(size)

                # Résultats
                if result == 'Full':
                    print("La grille est pleine... égalité")

                elif result == 'Croix':
                    print("Le joueur 1 à gagné !")

                elif result == 'Rond':
                    print("Le joueur 2 à gagné !")

            else: # Morpions contre l'ordinateur (facile)
                if mode == 1:
                    result = rdm.random_morpion()

                else:
                    result = mega.mega_morpion(size)

                # Résultats
                if result == 'Full':
                    print("La grille est pleine... égalité")

                elif result == 'Croix':
                    print("Le joueur 1 à gagné !")

                elif result == 'Rond':
                    print("Le joueur 2 à gagné !")

        elif adv == 2: # Morpions à deux joueurs
            if mode == 1:
                result = multi.jouer_morpion()

            else:
                result = master.master_morpion(size, 'facile')

            # Résultats
            if result == 'Full':
                print("La grille est pleine... égalité")

            elif result == 'Croix':
                print("Le joueur 1 à gagné !")

            elif result == 'Rond':
                print("Le joueur 2 à gagné !")

morpion() # Lancement du Morpion