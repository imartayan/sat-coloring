# Coloration de graphes à l'aide d'un SAT solveur

Ce projet a été réalisé avec Kelun Chai, Matthieu Lacote, Dimitri Lesnoff et Claire Zeng au cours de l'école d'été [Mathinfoly 2019](http://www.mathinfoly.org/).
Il est licencié selon les termes de la licence GPLv3.

## Prérequis

Ce projet utilise le langage [OCaml](https://ocaml.org/index.fr.html), le solveur SAT [glucose](https://www.labri.fr/perso/lsimon/glucose/) et la librairie python networkx (`pip install networkx`).

## Utilisation

```
usage: python3 coloring.py [-h] [graph] [colors]

Coloration de graphes à l'aide d'un solveur SAT

positional arguments:
  graph       file containing the graph
  colors      number of colors (3 by default)

optional arguments:
  -h, --help  show this help message and exit
```

## Format du fichier d'entrée

Le fichier d'entrée représentant le graphe doit contenir :
* sur la première ligne _n_ le nombre de sommets et _p_ le nombre d'arêtes
* sur les _p_ lignes suivantes le numéro des deux sommets reliés par une arêtes

## Générateur de graphe

```
usage: python3 generator.py [-h] vertices [file]

Génération d'un graphe aléatoire

positional arguments:
  vertices    number of vertices
  file        where to write the graph

optional arguments:
  -h, --help  show this help message and exit

```
