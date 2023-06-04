#!/usr/bin/env python

from user import User
from jeux.machine_a_sous import MachineASous
from jeux.roulette import Roulette
from getpass import getpass
import hashlib
import os

def start_game():
    # Charge la liste des utilisateurs depuis le fichier score.txt.
    users = load_users()
    
    while True:
        # affiche le tableau des scores.
        display_scores(users)
    
        # L'utilisateur entre son nom et son mot de passe.
        name = str(input("Bienvenue au mini casino. Entrez votre nom : ")).lower()
        password = getpass("Entrez votre mot de passe : ")
        password = hashlib.sha512(password.encode()).hexdigest()

        # On vérifie si l'utilisateur existe déjà. Si ce n'est pas le cas, on crée un nouvel utilisateur.
        user = find_user(name, users)
        if user:
            if user.password != password:
                print("Mot de passe incorrect. Fin du programme.")
                return
        else:
            user = User(name, password=password)
            users.append(user)

        # L'utilisateur choisit le jeu auquel il veut jouer.
        while True:
            print(f"Bienvenue {user.name}, ton solde est de {user.money}. A quel jeux veux tu jouer? \n1: Machine à sous\n2: Roulette\nq: Quitter")
            choice = input("Choix : ")
            if str(choice).lower() == 'q':
                # Si l'utilisateur choisit de quitter, on sauvegarde les scores et on quitte le programme.
                save_users(users)
                break
            elif choice == '1':
                # Si l'utilisateur choisit la machine à sous, on lance le jeu de la machine à sous.
                mas = MachineASous()
                mas.bienvenue()
                mas.run(user)
            elif choice == '2':
                # Si l'utilisateur choisit la roulette, on lance le jeu de la roulette.
                roulette = Roulette()
                roulette.bienvenue()
                roulette.run(user)
            else:
                print("Choix non valide, réessayez.")

def load_users():
    # Charge la liste des utilisateurs depuis le fichier score.txt.
    if not os.path.exists('score.txt'):
        return []

    with open('score.txt', 'r') as file:
        lines = file.readlines()
    users = []
    for line in lines:
        data = line.strip().split(';')
        if len(data) == 3:
            name, money, password = data
            users.append(User(name, float(money), password))
    return users


def find_user(name, users):
    # Trouve un utilisateur dans la liste des utilisateurs.
    for user in users:
        if user.name == name:
            return user
    return None

def display_scores(users):
    # Affiche le tableau des scores.
    for user in users:
        print(f'{user.name} à une mise de {user.money}\n')

def save_users(users):
    # Trie les utilisateurs par montant d'argent décroissant
    sorted_users = sorted(users, key=lambda user: user.money, reverse=True)

    # Sauvegarde la liste des utilisateurs dans le fichier score.txt
    with open('score.txt', 'w') as file:
        for user in sorted_users:
            file.write(f"{user.name};{user.money};{user.password}\n")


if __name__ == "__main__":
    start_game()
