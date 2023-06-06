# Mini Casino

Le but de ce programme en python est de simuler un petit casino avec deux jeux : une machine à sous et une roulette. Les scores des joueurs sont enregistrés dans un fichier score.txt.

## Prérequis
Python 3.x installé sur votre système.

## Installation
Clonez ou téléchargez ce dépôt sur votre machine.

## Utilisation
Ouvrez un terminal et accédez au répertoire du projet.

Exécutez le programme en utilisant la commande suivante :
```bash
python main.py
```

Suivez les instructions affichées à l'écran pour jouer aux différents jeux du casino.

## Fonctionnalités
Lors du début de la partie, le tableau des scores est affiché et enregistré dans le fichier score.txt.

Les utilisateurs peuvent s'inscrire avec leur nom et leur mot de passe. S'ils sont déjà inscrits, ils peuvent se connecter avec leur mot de passe.

Les utilisateurs peuvent choisir entre la machine à sous et la roulette pour jouer.

Les résultats des jeux sont affichés à l'écran, et les scores des joueurs sont mis à jour en conséquence.

Les scores des joueurs sont enregistrés dans le fichier score.txt à la fin de chaque partie.

## Règles du jeu 

### La Roulette
L'utilisateur peut choisir de miser une somme d'argent (qui doit être un nombre positif et qu'il doit posséder). Une fois la somme misée, il doit choisir un numéro compris entre 0 et 49. La roulette tire ensuite un numéro au hasard également compris entre 0 et 49. Si le numéro tiré est celui choisi par l'utilisateur, il reçoit trois fois la somme misée (après l'avoir donnée à la roulette). Si le numéro choisi par l'utilisateur et celui tiré par la roulette sont tous les deux pairs, l'utilisateur récupère seulement 50% de sa somme initiale. De même, s'ils sont tous les deux impairs. Dans le cas où le numéro choisi par l'utilisateur est pair mais celui tiré par la roulette ne l'est pas (ou inversement), alors l'utilisateur ne reçoit rien. L'utilisateur peut choisir de miser à nouveau une somme ou quitter. 

### La Machine à sous
Si 1€ est joué, l'utilisateur perd 1€. La machine à sous tire au hasard alors 3 chiffres entre 1 et 6 compris. Si les 3 chiffres sont identiques, il gagne 500€, sinon il ne gagne rien. De nouveau il peut choisir entre jouer 1€ ou quitter.

