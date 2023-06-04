import hashlib

class User:
    def __init__(self, name, money=100, password=None):
        # Initialisation de l'utilisateur avec un nom, un montant d'argent et un mot de passe.
        # Le mot de passe est haché en utilisant sha512 pour des raisons de sécurité.
        self.name = name
        self.money = money
        # self.password = hashlib.sha512(password.encode()).hexdigest() if password else None
        self.password = password 


    def __str__(self):
        # Représentation de l'utilisateur sous forme de chaîne pour l'enregistrement dans le fichier.
        return f"{self.name};{self.money};{self.password}"

    def bet(self, amount):
        while True:
            try:
                assert amount > 0 and amount <= self.money, "Montant invalide"
                self.money -= amount
                return amount
            except AssertionError as e:
                print("Erreur :", e)
                amount = float(input("Entrez un montant valide : "))


    def win(self, amount):
        # Ajoute le montant gagné au total d'argent de l'utilisateur.
        self.money += amount
        print(f"Vous avez gagné {amount}")
      
