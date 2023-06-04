class Jeu:
    def __init__(self, nom_du_jeu):
        # Initialisation du jeu avec un nom.
        self.nom_du_jeu = nom_du_jeu

    def bienvenue(self):
        # Affiche un message de bienvenue pour le jeu.
        print(f"Bienvenu dans {self.nom_du_jeu}")

