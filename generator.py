from argparse import ArgumentParser
from random import randint
from math import sqrt

parser = ArgumentParser(description="Génération d'un graphe aléatoire")
parser.add_argument("vertices", help="number of vertices", type=int)
parser.add_argument(
    "file", help="where to write the graph", nargs="?", default="random.txt"
)
args = parser.parse_args()

edges = randint(0, args.vertices * sqrt(args.vertices - 1) // 2)

with open(args.file, "w") as out:
    out.write(f"{args.vertices} {edges}\n")
    A = set()
    for _ in range(edges):
        i = randint(1, args.vertices)
        j = randint(1, args.vertices)
        while i == j or (i, j) in A or (j, i) in A:
            i = randint(1, args.vertices)
            j = randint(1, args.vertices)
        out.write(f"{i} {j}\n")
        A.add((i, j))
