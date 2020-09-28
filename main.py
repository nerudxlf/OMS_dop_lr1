import os
import networkx
import pylab as plt
import numpy as np
import csv
import pandas as pd


def data_to_xls(path, data, sheet_name):
    df = pd.DataFrame(data, index=[0]).T
    df.to_excel(path, sheet_name=sheet_name)


def draw_func(graph):
    # this function is drawing png graph
    networkx.nx.draw(graph)
    plt.savefig('graph.png')
    plt.close()


def main():
    os.getcwd()
    g = networkx.read_edgelist("facebook_combined.txt")
    path = "data.xlsx"
    print("Нарисовать граф? y/n")
    user_input = str(input())
    if user_input.lower() == "y":
        draw_func(g)
    degree = networkx.nx.degree_centrality(g) # степень связанности !!! dict
    data_to_xls("degree.xls", degree, "Cтепень связанности")

    bet = networkx.nx.betweenness_centrality(g) # степень посредничества !!!dict
    data_to_xls("bet.xls", bet, "степень посредничества")

    close = networkx.nx.closeness_centrality(g) # степень близости к другим вершинам !!!dict
    data_to_xls("close.xls", close, "степень близости")

    eigenvector = networkx.nx.eigenvector_centrality(g) # влиятельность !!!dict
    data_to_xls("eigenvector.xls", eigenvector, "влиятельность")

    clustering_coefficient = networkx.nx.clustering(g) # коэффициент кластерилизации !!!dict
    data_to_xls("clustering_coefficient.xls", clustering_coefficient, "коэффициент кластерилизации")

    global_clustering_coefficient = np.mean(list(networkx.nx.clustering(g).values())) # глобальный коэффициент кластерилизации !!!number
    mean_degree = np.mean(list(degree.values())) # средняя степень связанности !!!number
    density_graph = networkx.nx.density(g) # плотность графа !!!number
    diameter_graph = networkx.nx.diameter(g) # диаметр графа !!!number
    number_components = networkx.nx.number_connected_components(g) # число компонентов связанности !!!number
    average_distance = networkx.nx.average_shortest_path_length(g) # среднее расстояние между вершинами !!!number

    dict_data = {
        "глобальный коэффициент кластерилизации": global_clustering_coefficient,
        "средняя степень связанности": mean_degree,
        "плотность графа": density_graph,
        "диаметр графа": diameter_graph,
        "число компонентов связанности": number_components,
        "среднее расстояние между вершинами": average_distance
    }
    data_to_xls("data.xls", dict_data, "data")


if __name__ == '__main__':
    main()

