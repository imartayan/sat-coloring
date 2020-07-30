from argparse import ArgumentParser
from subprocess import run
import matplotlib.pyplot as plt
import networkx as nx

parser = ArgumentParser(description="Coloration de graphes à l'aide d'un solveur SAT")
parser.add_argument(
    "graph",
    help="file containing the graph",
    nargs="?",
    default="example/simple.txt",
    type=str,
)
parser.add_argument("colors", help="number of colors", default=3, type=int)
args = parser.parse_args()

sat_solver = ["glucose_static", "-model"]
sat_result = "result.txt"
cnf_file = "clauses.cnf"
coloring_ml = "coloring.ml"

with open(args.graph, "r") as f:
    s = f.readline()
    n, p = map(int, s.split())
    adjacence = []
    for _ in range(p):
        s = f.readline()
        i, j = map(int, s.split())
        adjacence.append([i, j])

run(["ocaml", coloring_ml, args.graph, str(args.colors)])
run(sat_solver + [cnf_file, sat_result])

colors = {1: "blue", 2: "green", 3: "red", 4: "yellow", 5: "purple"}

with open(sat_result, "r") as f:
    s = f.readline().strip()
    if s == "UNSAT":
        print(">> IMPOSSIBLE <<")
    else:
        solution = list(map(int, s.split()))
        color_list = []
        for i in range(n):
            for k in range(args.colors):
                if solution[args.colors * i + k] >= 0:
                    color_list.append(k + 1)
        # Création du graphe solution
        G = nx.Graph()
        for j in range(1, n + 1):
            G.add_node(j)
        for h in adjacence:
            G.add_edge(h[0], h[1])
        color_map = []
        for c in color_list:
            color_map.append(colors[c])
        # Dessin du graphe solution
        fig = plt.figure()
        nx.draw(G, node_color=color_map, with_labels=True)
        plt.show()
