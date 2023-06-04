import random
from jeux.jeu import Jeu

class MachineASous(Jeu):
    def __init__(self):
        # Initialise le nom du jeu à "Machine à sous".
        super().__init__("Machine à sous")

    def run(self, user):
        # Exécute le jeu.
        while True:
            # Affiche le menu du jeu.
            print(f"Quel est votre choix? (ton solde est  de {user.money})\n1: Jouer 1€\nq: Quitter")
            choice = input("Choix : ")
            if str(choice).lower() == 'q':
                # Si l'utilisateur choisit de quitter, on arrête le jeu.
                break
            elif choice == '1':
                # Si l'utilisateur choisit de jouer, il parie 1€.
                user.bet(1)
                # La machine à sous tire 3 chiffres au hasard.
                results = [random.randint(1, 6) for _ in range(3)]
                # Si les 3 chiffres sont identiques, l'utilisateur gagne 500€.
                if len(set(results)) == 1:
                    user.win(500)
                else:
                    print('Vous avez perdu')
            else:
                # Si l'utilisateur entre autre chose, on lui dit que son entrée est invalide.
                print("Entrée invalide, réessayez.")
