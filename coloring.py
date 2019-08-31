from sys import argv
from subprocess import run
import matplotlib.pyplot as plt
import networkx as nx

if len(argv) >= 2:
    entree = argv[1]
else:
    entree = "exemples_graphes/graphe_petersen.txt"
if len(argv) >= 3:
    q = int(argv[2])
else:
    q = 3
ml = "magic_coloring_tail_general.ml"
cnf = "clauses.cnf"
sortie = "result.txt"

with open(entree, "r") as f:
    s = f.readline()
    n, p = map(int, s.split())
    adjacence = []
    for _ in range(p):
        s = f.readline()
        i, j = map(int, s.split())
        adjacence.append([i, j])

run(["ocaml", ml, entree, str(q)])
run(["glucose_static", "-model", cnf, sortie])

with open(sortie, "r") as f:
    s = f.readline().strip()
    if s == "UNSAT":
        print(">> NON SATISFIABLE <<")
    else:
        solution = list(map(int, s.split()))
        color_list = []
        for i in range(n):
            for k in range(q):
                if solution[q * i + k] >= 0:
                    color_list.append(k + 1)
        # Creation du graphe solution
        G = nx.Graph()
        for j in range(1, n + 1):
            G.add_node(j)
        for h in adjacence:
            G.add_edge(h[0], h[1])
        color_map = []
        colors = {1: "blue", 2: "green", 3: "red", 4: "yellow", 5: "purple"}
        for c in color_list:
            color_map.append(colors[c])
        # Dessin du graphe solution
        fig = plt.figure()
        nx.draw(G, node_color=color_map, with_labels=True)
        fig.savefig("graphes_solution/graphe_solution.png")
        plt.show()
