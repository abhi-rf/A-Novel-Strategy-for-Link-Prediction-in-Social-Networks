# -*- coding: utf-8 -*-
import networkx as nx
from pprint import pprint

dolphin = "./dolphins.gml"
karate = "./karate.gml"

if __name__ == "__main__":
    #Finding prob between 0 and 5

    # G = nx.read_gml(dolphin, label='id')
    G = nx.read_gml(karate, label='id')

    # pprint(G.nodes())
    # print(list(G.neighbors(0)))

    x = 1
    y = 5

    neighbors_x = set(G.neighbors(x))
    neighbors_y = set(G.neighbors(y))
    # print(neighbors_x, neighbors_y)

    C = set.intersection(neighbors_x, neighbors_y)
    N = set.union(neighbors_x, neighbors_y)
    # pprint(N)
    # pprint(C)

    UCX = neighbors_x - C
    UCY = neighbors_y - C
    # print(UCX)
    # print(UCY)

    # Score = (len(C)/len(N))
    # print(Score)
