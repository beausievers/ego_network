"""Load and analyze an egocentric network."""

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

