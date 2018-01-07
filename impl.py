# -*- coding: utf-8 -*-
import networkx as nx
from pprint import pprint

filepaths = ["./dolphins.gml", "./karate.gml", './illustration.gml']

def get_graph(filepath):
    return nx.read_gml(filepath, label='id')

def get_score(x, y):
    neighbors_x = set(G.neighbors(x))
    neighbors_y = set(G.neighbors(y))
    pprint(neighbors_x)
    pprint(neighbors_y)

    N = set.union(neighbors_x, neighbors_y)
    C = set.intersection(neighbors_x, neighbors_y)
    pprint(N)
    pprint(C)

    UCX = neighbors_x - C
    UCY = neighbors_y - C
    print(UCX)
    print(UCY)

    conn_UCN = 0
    for ucx in UCX:
        for ucy in UCY:
            if G.has_edge(ucx, ucy):
                conn_UCN += 1

    print(conn_UCN)

    score_part1 = len(C) / len(N)
    score_part2 = conn_UCN / (len(UCX) * len(UCY))
    score = score_part1 + score_part2
    print(score_part1, score_part2, score)

if __name__ == "__main__":
    #Finding prob between 0 and 5

    # G = nx.read_gml(dolphin, label='id')
    # G = nx.read_gml(karate, label='id')
    G = get_graph(filepaths[2])

    # pprint(G.nodes())
    # print(list(G.neighbors(0)))

    get_score(2, 5)
