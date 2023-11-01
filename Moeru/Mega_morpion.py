import random as rdm

def choix_de_case(size : int):
    ''' Paramètre - size (int) : taille de la grille (100 ou 250)
    Return - renvoit l'id de la case choisie (str) '''

    # Choix de la colone
    col = int(input("Choississez une colone \n> "))
    col = 0 if col < 0 else col
    col = size - 1 if col >= size else col

    # Choix de la ligne
    lin = int(input("Choississez une ligne \n> "))
    lin = 0 if lin < 0 else lin
    lin = size - 1 if lin >= size else lin

    return f'c{col}_l{lin}'

def random_choice_ord(cases : list, size : int):
    ''' Paramètre - cases (list) : listes des cases occupées, size (int) : taille de la grille (100 ou 250)
    Return - renvoit l'id de la case choisie (str) '''

    cases_jouables = []

    for col in range(size):
        for lin in range(size):
            if f'c{col}_l{lin}' not in cases and (f'c{col - 1}_l{lin}' in cases or f'c{col + 1}_l{lin}' in cases or f'c{col}_l{lin - 1}' in cases or f'c{col}_l{lin + 1}' in cases):
                cases_jouables.append(f'c{col}_l{lin}')

    if cases_jouables != []:
        return rdm.choice(cases_jouables)
    
    # Choix par défaut
    else:
        return 'c0_l0'

def choice_ord(cases : list, cases_adv : list, size : int):
    ''' Paramètre - cases (list) : listes des cases occupées, cases_adv (list) : liste des cases de l'adversaire, size (int) : taille de la grille (100 ou 250)
    Return - renvoit l'id de la case choisie de manière aléatoire (str) '''

    cases_jouables = []

    for col in range(size):
        for lin in range(size):
            if f'c{col}_l{lin}' not in cases and (f'c{col - 1}_l{lin}' in cases or f'c{col + 1}_l{lin}' in cases or f'c{col}_l{lin - 1}' in cases or f'c{col}_l{lin + 1}' in cases):
                cases_jouables.append(f'c{col}_l{lin}')
    
    print(cases_jouables)
    if cases_jouables != []:
        for col in range(size):
            for lin in range(size):
                if f'c{col}_l{lin}' in cases_adv:
                    # - Tests défensifs

                    # Test colone
                    if f'c{col - 1}_l{lin}' in cases_adv and f'c{col - 2}_l{lin}' in cases_adv:
                        if f'c{col - 3}_l{lin}' in cases_jouables:
                            return f'c{col - 3}_l{lin}'
                        
                        elif f'c{col + 1}_l{lin}' in cases_jouables:
                            return f'c{col + 1}_l{lin}'
                    
                    # Test ligne
                    elif f'c{col}_l{lin + 1}' in cases_adv and f'c{col}_l{lin + 2}' in cases_adv:
                        if f'c{col}_l{lin + 3}' in cases_jouables:
                            return f'c{col}_l{lin + 3}'
                        
                        elif f'c{col}_l{lin - 1}' in cases_jouables:
                            return f'c{col}_l{lin - 1}'
                    
                    # Test diagonal gauche
                    elif f'c{col + 1}_l{lin - 1}' in cases_adv and f'c{col + 2}_l{lin - 2}' in cases_adv:
                        if f'c{col + 3}_l{lin - 3}' in cases_jouables:
                            return f'c{col + 3}_l{lin - 3}'
                        
                        elif f'c{col - 1}_l{lin + 1}' in cases_jouables:
                            return f'c{col - 1}_l{lin + 1}'
                    
                    # Test diagonal droite
                    elif f'c{col + 1}_l{lin + 1}' in cases_adv and f'c{col + 2}_l{lin + 2}' in cases_adv:
                        if f'c{col + 3}_l{lin + 3}' in cases_jouables:
                            return f'c{col + 3}_l{lin + 3}'
                        
                        elif f'c{col - 1}_l{lin - 1}' in cases_jouables:
                            return f'c{col - 1}_l{lin - 1}'

                    # Choix offensif aléatoire
                    else:
                        return random_choice_ord(cases, size)
    
    # Choix par défaut
    else:
        return 'c0_l0'

def check_choice(case : str, cases : list, size : int):
    ''' Paramètre - case (int) : id de la case à vérifier, cases (list) : listes des cases occupées, size (int) : taille de la grille (100 ou 250)
    Return - "True" si la case est valide, "False" sinon '''

    if cases == []:
        return True
    
    else:
        for col in range(size):
            for lin in range(size):
                if f'c{col}_l{lin}' in cases:

                    # Vérification par colone
                    if f'c{col - 1}_l{lin}' == case or f'c{col + 1}_l{lin}' == case:
                        return True

                    # Vérification par ligne
                    elif f'c{col}_l{lin - 1}' == case or f'c{col}_l{lin + 1}' == case:
                        return True
                
        return False

def check_win(cases : list, size : int):
    ''' Paramètre - cases (list) : listes des cases à vérifier, size (int) : taille de la grille (100 ou 250)
    Return - "True" si la liste est gagnante, "False" sinon '''

    for col in range(size):
        for lin in range(size):
            if f'c{col}_l{lin}' in cases:

                # Test colone
                if f'c{col - 1}_l{lin}' in cases and f'c{col - 2}_l{lin}' in cases and f'c{col - 3}_l{lin}' in cases and f'c{col - 4}_l{lin}' in cases:
                    return True
                
                # Test ligne
                elif f'c{col}_l{lin + 1}' in cases and f'c{col}_l{lin + 2}' in cases and f'c{col}_l{lin + 3}' in cases and f'c{col}_l{lin + 4}' in cases:
                    return True
                
                # Test diagonal gauche
                elif f'c{col + 1}_l{lin - 1}' in cases and f'c{col + 2}_l{lin - 2}' in cases and f'c{col + 3}_l{lin - 3}' in cases and f'c{col + 4}_l{lin - 4}' in cases:
                    return True
                
                # Test diagonal droite
                elif f'c{col + 1}_l{lin + 1}' in cases and f'c{col + 2}_l{lin + 2}' in cases and f'c{col + 3}_l{lin + 3}' in cases and f'c{col + 4}_l{lin + 4}' in cases:
                    return True

    return False

def mega_morpion(size : int, niveau : str = 'normal'):
    ''' Paramètre - size (int) : taille de la grille (100 ou 250)
    Return - renvoie l'id du gagnant, "Full" si la partie est bloquée sans vainqueur, ou bien "Erreur" (str) '''

    if size == 250 or size == 100:
        side = 1 # 1 = croix, 2 = rond
        cases_croix = []
        cases_rond = []
        cases_occupées = []
        print("> MASTER MORPION < \n \n> Tour 1 <")

        while len(cases_occupées) < 1000 and not check_win(cases_croix, size) and not check_win(cases_rond, size):
            print(f"\n> Joueur {side} <")

            if side == 1:
                case_act = choix_de_case(size)

            elif side == 2:
                if niveau == 'facile':
                    case_act = choice_ord(cases_occupées, cases_croix, size)

                else:
                    case_act = random_choice_ord(cases_occupées, size)
            
            print('>', case_act)
            
            if case_act not in cases_occupées and check_choice(case_act, cases_occupées, size):
                cases_occupées.append(case_act)

                if side == 1:
                    cases_croix.append(case_act)
                    side = 2

                elif side == 2:
                    cases_rond.append(case_act)
                    side = 1
                    print(f"\n> Tour {(len(cases_occupées) // 2) + 1} <")

        if check_win(cases_croix, size):
            return 'Croix'
        
        elif check_win(cases_croix, size):
            return 'Rond'
        
        elif len(cases_occupées) < 1000:
            return 'Full'
        
        else:
            return 'Erreur'

    else:
        return mega_morpion(100)

print(mega_morpion(100))