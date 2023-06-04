import random
from jeux.jeu import Jeu

class Roulette(Jeu):
    def __init__(self):
        # Initialise le nom du jeu à "Roulette".
        super().__init__("Roulette")

    def run(self, user):
        # Exécute le jeu.
        while True:
            # L'utilisateur choisit le montant qu'il veut parier.
            bet = input(f"Entrez la somme à parier (ton solde est  de {user.money}), q pour quitter : ")
            if str(bet).lower() == 'q':
                break
            try:
                bet = float(bet)
            except ValueError:
                print("Entrée invalide, réessayez.")
                continue

            # L'utilisateur parie le montant choisi.
            user.bet(bet)

            # L'utilisateur choisit un numéro sur lequel parier.
            while True:
                chosen_number = input("Choisissez un numéro entre 0 et 49 : ")
                if chosen_number.isdigit() and 0 <= int(chosen_number) <= 49:
                    chosen_number = int(chosen_number)
                    break
                else:
                    print("Saisie invalide. Veuillez choisir un numéro entre 0 et 49.")
            


            # La roulette tire un numéro au hasard.
            random_number = random.randint(0, 49)

            # On vérifie si l'utilisateur a gagné ou non et on met à jour son argent en conséquence.
            if random_number == chosen_number:
                amountWin = bet * 3
                user.win(amountWin)
             
            elif random_number % 2 == chosen_number % 2:
                amountWin = bet * 0.5
                user.win(amountWin)
            
            else : 
                print("Vous avez perdu")
