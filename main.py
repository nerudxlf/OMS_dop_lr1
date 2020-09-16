import os
import networkx
import pylab as plt
import numpy as np


def draw_func(graph):
    # this function is drawing png graph
    networkx.nx.draw(graph)
    plt.savefig('graph.png')
    plt.close()



def main():
    os.getcwd()
    g = networkx.read_edgelist("facebook_combined.txt")
    print("Нарисовать граф? y/n")
    user_input = str(input())
    if user_input.lower() == "y":
        draw_func(g)

    #degree = networkx.nx.degree_centrality(g) # степень связанности
    #bet = networkx.nx.betweenness_centrality(g) # степень посредничества
    #close = networkx.nx.closeness_centrality(g) # степень близости к другим вершинам
    #eigenvector = networkx.nx.eigenvector_centrality(g) # влиятельность
    #print(degree, bet, close, eigenvector)

    #clustering_coefficient = networkx.nx.clustering(g).values() # коэффициент кластерилизации
    #global_clustering_coefficient = np.mean(list(networkx.nx.clustering(g).values())) # глобальный коэффициент кластерилизации
    #mean_degree = np.mean(list(degree.values())) # средняя степень связанности
    #density_graph = networkx.nx.density(g) # плотность графа
    #diameter_graph = networkx.nx.diameter(g) # диаметр графа
    number_components = networkx.nx.number_connected_components(g)
    print(number_components) 



if __name__ == '__main__':
    main()

