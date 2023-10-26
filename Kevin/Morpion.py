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

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    joueur_actif = 0

    while True:
        afficher_plateau(plateau)
        symbole = symboles[joueur_actif]

        print(f"Tour du joueur {symbole}. Entrez les coordonnées (ligne et colonne) de votre prochain coup (ex: 1 2):")

        try:
            ligne, colonne = map(int, input().split())
        except ValueError:
            print("Coordonnées invalides. Veuillez entrer des nombres séparés par un espace.")
            continue

        if ligne < 1 or ligne > 3 or colonne < 1 or colonne > 3:
            print("Coordonnées en dehors du plateau. Veuillez entrer des coordonnées valides.")
            continue

        if plateau[ligne - 1][colonne - 1] == " ":
            plateau[ligne - 1][colonne - 1] = symbole
        else:
            print("La case est déjà occupée. Veuillez choisir une case vide.")
            continue

        if verifier_victoire(plateau, symbole):
            afficher_plateau(plateau)
            print(f"Le joueur {symbole} a gagné !")
            break

        if est_match_nul(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        joueur_actif = (joueur_actif + 1) % 2

if __name__ == "__main__":
    morpion()