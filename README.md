# Coloration de graphes à l'aide d'un SAT solveur

Ce projet a été réalisé avec Kelun Chai, Matthieu Lacote, Dimitri Lesnoff et Claire Zeng au cours de l'école d'été [Mathinfoly 2019](http://www.mathinfoly.org/).
Il est licencié selon les termes de la licence GPLv3.

## Prérequis

Ce projet utilise le langage [OCaml](https://ocaml.org/index.fr.html), le SAT solveur [glucose](https://www.labri.fr/perso/lsimon/glucose/) et la librairie python networkx (`pip install networkx`).

## Utilisation

Le programme se lance de la façon suivante :
`python3 coloring.py fichier_graphe nombre_de_couleurs sat_solveur`

Par défaut, le nombre de couleurs vaut 3 et le SAT solveur est [glucose](https://www.labri.fr/perso/lsimon/glucose/).

## Format du fichier d'entrée

Le fichier d'entrée représentant le graphe doit contenir :
* sur la première ligne _n_ le nombre de sommets et _p_ le nombre d'arêtes
* sur les _p_ lignes suivantes le numéro des deux sommets reliés par une arêtes

## Générateur de graphe

Le programme `generator.py` permet de générer un fichier d'entrée de la façon suivante :
`python3 generator.py nombre_de_sommets nombre_d_aretes nom_du_fichier`
