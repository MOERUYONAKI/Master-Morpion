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

def coup_ordinateur(plateau, symbole_ordi, symbole_joueur):
    # Stratégie de victoire : vérification des lignes, colonnes et diagonales
    for i in range(3):
        # Vérifier les lignes
        if plateau[i].count(symbole_ordi) == 2 and plateau[i].count(symbole_joueur) == 0:
            for j in range(3):
                if plateau[i][j] == " ":
                    return i, j
        # Vérifier les colonnes
        if [plateau[x][i] for x in range(3)].count(symbole_ordi) == 2 and [plateau[x][i] for x in range(3)].count(symbole_joueur) == 0:
            for j in range(3):
                if plateau[j][i] == " ":
                    return j, i

    # Vérifier les diagonales
    if [plateau[i][i] for i in range(3)].count(symbole_ordi) == 2 and [plateau[i][i] for i in range(3)].count(symbole_joueur) == 0:
        for i in range(3):
            if plateau[i][i] == " ":
                return i, i
    if [plateau[i][2 - i] for i in range(3)].count(symbole_ordi) == 2 and [plateau[i][2 - i] for i in range(3)].count(symbole_joueur) == 0:
        for i in range(3):
            if plateau[i][2 - i] == " ":
                return i, 2 - i

    # Stratégie de défense : empêcher le joueur de gagner
    for i in range(3):
        # Vérifier les lignes
        if plateau[i].count(symbole_joueur) == 2 and plateau[i].count(symbole_ordi) == 0:
            for j in range(3):
                if plateau[i][j] == " ":
                    return i, j
        # Vérifier les colonnes
        if [plateau[x][i] for x in range(3)].count(symbole_joueur) == 2 and [plateau[x][i] for x in range(3)].count(symbole_ordi) == 0:
            for j in range(3):
                if plateau[j][i] == " ":
                    return j, i

    # Vérifier les diagonales
    if [plateau[i][i] for i in range(3)].count(symbole_joueur) == 2 and [plateau[i][i] for i in range(3)].count(symbole_ordi) == 0:
        for i in range(3):
            if plateau[i][i] == " ":
                return i, i
    if [plateau[i][2 - i] for i in range(3)].count(symbole_joueur) == 2 and [plateau[i][2 - i] for i in range(3)].count(symbole_ordi) == 0:
        for i in range(3):
            if plateau[i][2 - i] == " ":
                return i, 2 - i

    # Stratégie par défaut : choisir une case vide au hasard
    cases_vides = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]
    return random.choice(cases_vides)

def basic_morpion():
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
            ligne, colonne = coup_ordinateur(plateau, symbole_ordi, symbole_joueur)
            ligne += 1
            colonne += 1

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
            print("Le joueur a gagné !")
            break

        if all(cellule != " " for ligne in plateau for cellule in ligne):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        symbole_joueur, symbole_ordi = symbole_ordi, symbole_joueur

if __name__ == "__main__":
    basic_morpion()
