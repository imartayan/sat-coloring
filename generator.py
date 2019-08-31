from sys import argv
from random import randint
from math import sqrt

if len(argv) >= 2:
    n = int(argv[1])
else:
    n = randint(10, 1000)
if len(argv) >= 3:
    p = int(argv[2])
else:
    p = randint(0, n * sqrt(n - 1) // 2)
if len(argv) >= 4:
    fichier = argv[3]
else:
    fichier = "graphe_aleat.txt"

with open(fichier, "w") as out:
    out.write(f"{n} {p}\n")
    A = set()
    for _ in range(p):
        i = randint(1, n)
        j = randint(1, n)
        while i == j or (i, j) in A or (j, i) in A:
            i = randint(1, n)
            j = randint(1, n)
        out.write(f"{i} {j}\n")
        A.add((i, j))
