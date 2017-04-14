"""Load and analyze an egocentric network."""

import argparse
import pickle
import networkx as nx


def load_network(in_path):
    """Load pickled network info from ego_network.py."""
    with open(in_path, 'rb') as f:
        d = pickle.load(f)
    return d


def build_graph(d):
    """Build the network graph."""
    g = nx.Graph()
    g.add_nodes_from(d['nodes'])
    g.add_edges_from(d['edges'])
    return g


def ego_betweenness(g, d):
    """Get the betweenness centrality of the ego."""
    betweenness = nx.betweenness_centrality(g)
    return betweenness[d['name']]


def load(path):
    """Load data from ego_network.py and print ego betweenness."""
    d = load_network(path)
    g = build_graph(d)
    b = ego_betweenness(g, d)
    print("Betweenness for {0}: {1}".format(d['name'], b))
    return b


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    load(args.path)
