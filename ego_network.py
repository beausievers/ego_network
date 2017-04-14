"""A bare-bones egocentric network survey."""

import datetime
import itertools
import pickle


def get_friend(i, n):
    """Ask the user to input the name of a friend."""
    q = "({0} of {1}) Please enter a name, or enter \"DONE\": ".format(i, n)
    friend = input(q)
    return friend


def get_edge(pair):
    """Ask the user whether two friends are friends with each other."""
    q = "Do {0} and {1} like to spend time together? (enter 'y' or 'n') "
    q = q.format(pair[0], pair[1])
    response = input(q)
    valid_responses = ['y', 'ye', 'yes', 'es', '1']
    connected = 0
    if response.lower() in valid_responses:
        connected = 1
    return (pair, connected)


def save_network(nodes, edges, name, pid):
    """Save the egocentric graph."""
    d = {'nodes': nodes, 'edges': edges, 'name': name, 'pid': pid}

    out_filename = "{0}-{1}.pickle".format(
        datetime.datetime.now().strftime("%Y%m%d-%H%M%S"),
        pid
    )
    with open(out_filename, 'wb') as out_file:
        pickle.dump(d, out_file)


def run_survey(max_friends=12):
    """Run an egocentric network survey."""
    name = input("Please enter your name: ")
    pid = input("Please enter your participant ID: ")

    print("\nPlease carefully read the following.")

    print("\nConsider the people with whom you like to spend your free time. "
          "In the last few months, who are the people you have been with most "
          "often for informal social activities, such as going out to lunch, "
          "dinner, drinks, films, visiting one another's homes, studying "
          "together, exercising together, and so on?")

    print("\nPlease enter up to {0} names. If you finish before "
          "{0} names, enter \"DONE\".\n".format(max_friends))

    nodes = list()
    for i in range(max_friends):
        new_friend = get_friend(i + 1, max_friends)
        if new_friend.lower() == 'done':
            break
        else:
            nodes.append(new_friend)

    print("\nNow we will ask you to consider each pair of names provided. "
          "Each of these people is someone who you like to spend time with. "
          "For each pair of people, please indicate whether those two people "
          "like to spend time with each other. Does this pair of people engage"
          " in informal social activity, such as going out to lunch, dinner, "
          "drinks, films, visting one another's homes, studying together, "
          "exercising together, and so on?\n")

    pairs = itertools.combinations(nodes, 2)
    edges = []

    # Everyone is connected to the ego
    for node in nodes:
        edges.append((name, node))

    # Who is connected to whom?
    for pair in pairs:
        edge, connected = get_edge(pair)
        if connected == 1:
            edges.append(edge)

    # The ego is a node too
    nodes.append(name)

    save_network(nodes, edges, name, pid)


if __name__ == "__main__":
    run_survey()
