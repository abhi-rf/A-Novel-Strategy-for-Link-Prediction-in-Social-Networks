# -*- coding: utf-8 -*-
import networkx as nx
from pprint import pprint
import random

filepaths = ["./dolphins.gml", "./karate.gml", './illustration.gml']

class EdgeScore:
    def __init__(self, x, y, score):
        self.tuple = (x, y)
        self.score = score

    def __str__(self):
        return "%d <--> %d : %.3f" %(self.tuple[0], self.tuple[1], self.score)

    def __repr__(self):
        return str(self)

def get_graph(filepath):
    return nx.read_gml(filepath, label='id')

def get_score(x, y):
    neighbors_x = set(G.neighbors(x))
    neighbors_y = set(G.neighbors(y))
    # pprint(neighbors_x)
    # pprint(neighbors_y)

    N = set.union(neighbors_x, neighbors_y)
    C = set.intersection(neighbors_x, neighbors_y)
    # pprint(N)
    # pprint(C)

    UCX = neighbors_x - C
    UCY = neighbors_y - C
    # print(UCX)
    # print(UCY)

    conn_UCN = 0
    for ucx in UCX:
        for ucy in UCY:
            if G.has_edge(ucx, ucy):
                conn_UCN += 1

    # print(conn_UCN)

    score_part1 = len(C) / len(N)
    score_part2 = 0

    if (len(UCX) != 0 and len(UCY) != 0):
        score_part2 = conn_UCN / (len(UCX) * len(UCY))

    score = score_part1 + score_part2
    return score

def remove_probe_edges(graph, num_remove):
    removed = 0
    removed_edges = []
    while (removed < num_remove):
        edges = list(G.edges());
        remove_index = random.randint(0, len(edges) - 1)
        # print("Removing %d --> %d" % (edges[remove_index][0], edges[remove_index][1]))
        removed_edges.append(edges[remove_index])
        G.remove_edge(*(edges[remove_index]))
        removed += 1

    return removed_edges

def calculate_auc(n, missing_edges_scores, non_exist_edges_scores):
    n_p = 0
    n_dp = 0

    for i in range(0, n):
        miss_index = random.randint(0, len(missing_edges_scores) - 1)
        non_exist_index = random.randint(0, len(non_exist_edges_scores) - 1)

        missing_score = missing_edges_scores[miss_index].score
        non_exist_score = non_exist_edges_scores[non_exist_index].score

        if (missing_score > non_exist_score):
            n_p += 1
        else:
            n_dp += 1

    auc = (n_p + (0.5 * n_dp)) / n

    return auc


if __name__ == "__main__":
    #Finding prob between 0 and 5

    # G = nx.read_gml(dolphin, label='id')
    # G = nx.read_gml(karate, label='id')
    G = get_graph(filepaths[2])

    # pprint(G.nodes())
    # print(list(G.neighbors(0)))

    missing_edges = remove_probe_edges(G, int(len(G.edges) / 10))
    # pprint(removed_edges)
    non_exist_edges = []

    missing_edges_scores = []
    non_exist_edges_scores = []

    nodes = list(G.nodes())

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            x = nodes[i]
            y = nodes[j]
            if not G.has_edge(x, y):
                score = get_score(x, y)
                if (x, y) not in missing_edges and (y, x) not in missing_edges:
                    non_exist_edges.append((x, y))
                    non_exist_edges_scores.append(EdgeScore(x, y, score))
                else:
                    missing_edges_scores.append(EdgeScore(x, y, score))
                # print("%d --> %d" % (x, y))

    print(calculate_auc(10, missing_edges_scores, non_exist_edges_scores))
