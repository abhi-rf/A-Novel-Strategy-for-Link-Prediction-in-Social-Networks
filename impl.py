# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:08:40 2018

@author: Dell
"""

import networkx as nx
dolphin = "./dolphins.gml"
karate = "./karate.gml"

if __name__ == "__main__":
    #Finding prob between 0 and 5
    G = nx.read_gml(dolphin, label='id')
    #G = nx.read_gml(karate,label='id')
    #print(G.nodes())
    #print(list(G.neighbors(0)))
    neighbors_x = set((G.neighbors(0)))
    neighbors_y = set((G.neighbors(5)))
    print(neighbors_x," ",neighbors_y)
    C = (set.intersection(set(neighbors_x),set(neighbors_y)))
    N = (set.union(set(neighbors_x),set(neighbors_y)))
    print(N)
    print(C)
    UCX = neighbors_x - C
    UCY = neighbors_y - C
    print(UCX)
    Score = (len(C)/len(N))
    print(Score)
