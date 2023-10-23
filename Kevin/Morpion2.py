import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print(ligne[0], "|", ligne[1], "|", ligne[2])
        print("-" * 9)

def verifier_victoire(plateau, symbole):
    for ligne in plateau:
        if ligne == [symbole, symbole, symbole]:
            return True

    for colonne in range(3):
        if plateau[0][colonne] == plateau[1][colonne] == plateau[2][colonne] == symbole:
            return True

    if (plateau[0][0] == plateau[1][1] == plateau[2][2] == symbole) or (plateau[0][2] == plateau[1][1] == plateau[2][0] == symbole):
        return True

    return False

def jouer_morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "1"
    tour = 0

    while True:
        afficher_plateau(plateau)
        ligne, colonne = -1, -1

        if joueur_actuel == "1":
            ligne = int(input(f"Joueur {joueur_actuel}, entrez le numéro de ligne (0, 1, 2) : "))
            colonne = int(input(f"Joueur {joueur_actuel}, entrez le numéro de colonne (0, 1, 2) : "))
        else:
            while True:
                ligne = random.randint(0, 2)
                colonne = random.randint(0, 2)
                if plateau[ligne][colonne] == " ":
                    return False

        plateau[ligne][colonne] = joueur_actuel

        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur_actuel} a gagné !")
            return False

        tour += 1

        if tour == 9:
            afficher_plateau(plateau)
            print("Match nul !")
            return False

        joueur_actuel = "O" if joueur_actuel == "X" else "X"

if __name__ == "__main__":
    jouer_morpion()