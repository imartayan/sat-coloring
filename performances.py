from random import randint
from math import sqrt
from time import perf_counter
from subprocess import run
import matplotlib.pyplot as plt

entree = "exemples_graphes/graphe_aleat.txt"
ml = "magic_coloring.ml"
ml_tail = "magic_coloring_tail.ml"
cnf = "clauses.cnf"


def creer_graphe(n, p):
    with open(entree, "w") as out:
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


def performances(N, n_min, n_max):
    S = []
    A = []
    O = []
    for i in range(N):
        print(f"{i+1} / {N}")
        n = randint(n_min, n_max)
        p = randint(0, n * sqrt(n - 1) // 4)
        creer_graphe(n, p)
        t1 = perf_counter()
        run(["ocaml", ml_tail, entree])
        t2 = perf_counter()
        S.append(n)
        A.append(p)
        O.append(t2 - t1)
    return S, A, O


def performances_comp(N, n_min, n_max):
    S = []
    A = []
    O1 = []
    O2 = []
    for i in range(N):
        print(f"{i+1} / {N}")
        n = randint(n_min, n_max)
        p = randint(0, n * sqrt(n - 1) // 4)
        creer_graphe(n, p)
        t1 = perf_counter()
        run(["ocaml", ml, entree])
        t2 = perf_counter()
        run(["ocaml", ml_tail, entree])
        t3 = perf_counter()
        S.append(n)
        A.append(p)
        O1.append(t2 - t1)
        O2.append(t3 - t2)
    return S, A, O1, O2


def tracer_performances(N, n_min, n_max):
    S, A, O = performances(N, n_min, n_max)
    fig = plt.figure()
    plt.xlabel("Nombre de sommets")
    plt.ylabel("Temps d'exécution (s)")
    plt.scatter(S, O)
    fig.savefig(f"performances_S_{n_max}.png")
    X = [n*p for n, p in zip(S, A)]
    fig = plt.figure()
    plt.xlabel("Nombre de sommets * Nombre d'arêtes")
    plt.ylabel("Temps d'exécution (s)")
    plt.scatter(X, O)
    fig.savefig(f"performances_SA_{n_max}.png")


def tracer_performances_comp(N, n_min, n_max):
    S, A, O1, O2 = performances(N, n_min, n_max)
    fig = plt.figure()
    plt.xlabel("Nombre de sommets")
    plt.ylabel("Temps d'exécution (s)")
    plt.scatter(S, O1, label="Première version")
    plt.scatter(S, O2, label="Version récursive terminale")
    plt.legend()
    fig.savefig(f"performances_comp_S_{n_max}.png")
    X = [n*p for n, p in zip(S, A)]
    fig = plt.figure()
    plt.xlabel("Nombre de sommets * Nombre d'arêtes")
    plt.ylabel("Temps d'exécution (s)")
    plt.scatter(X, O1, label="Première version")
    plt.scatter(X, O2, label="Version récursive terminale")
    plt.legend()
    fig.savefig(f"performances_comp_SA_{n_max}.png")
