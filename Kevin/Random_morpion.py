import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)

def verifier_victoire(plateau, symbole):
    # Vérification des lignes
    for ligne in plateau:
        if all(cellule == symbole for cellule in ligne):
            return True

    # Vérification des colonnes
    for col in range(3):
        if all(plateau[i][col] == symbole for i in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False

def est_match_nul(plateau):
    return all(cellule != " " for ligne in plateau for cellule in ligne)

def coup_ordinateur_random(plateau):
    cases_vides = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]
    return random.choice(cases_vides)

def random_morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symbole_joueur = "X"
    symbole_ordi = "O"

    while True:
        afficher_plateau(plateau)

        if symbole_joueur == "X":
            print("Tour du joueur. Entrez les coordonnées (ligne et colonne) de votre prochain coup (ex: 1 2):")
            try:
                ligne, colonne = map(int, input().split())
            except ValueError:
                print("Coordonnées invalides. Veuillez entrer des nombres séparés par un espace.")
                continue
        else:
            print("Tour de l'ordinateur...")
            ligne, colonne = coup_ordinateur_random(plateau)

        if ligne < 1 or ligne > 3 or colonne < 1 or colonne > 3:
            print("Coordonnées en dehors du plateau. Veuillez entrer des coordonnées valides.")
            continue

        if plateau[ligne - 1][colonne - 1] == " ":
            plateau[ligne - 1][colonne - 1] = symbole_joueur
        else:
            print("La case est déjà occupée. Veuillez choisir une case vide.")
            continue

        if verifier_victoire(plateau, symbole_joueur):
            afficher_plateau(plateau)
            if symbole_joueur == 'X':
                return 'Croix'
            
            elif symbole_joueur == 'O':
                return 'Rond'

        if est_match_nul(plateau):
            afficher_plateau(plateau)
            return 'Full'

        symbole_joueur, symbole_ordi = symbole_ordi, symbole_joueur