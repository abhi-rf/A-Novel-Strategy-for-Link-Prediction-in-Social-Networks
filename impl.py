# -*- coding: utf-8 -*-
import networkx as nx
from pprint import pprint

dolphin = "./dolphins.gml"
karate = "./karate.gml"
illustration = './illustration.gml'

if __name__ == "__main__":
    #Finding prob between 0 and 5

    # G = nx.read_gml(dolphin, label='id')
    # G = nx.read_gml(karate, label='id')
    G = nx.read_gml(illustration, label='id')

    # pprint(G.nodes())
    # print(list(G.neighbors(0)))

    x = 2
    y = 5

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

    # Score = (len(C))
    # print(Score)
