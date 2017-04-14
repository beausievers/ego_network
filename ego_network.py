"""A bare-bones egocentric network survey."""

import csv
import itertools


def get_friend(i, n):
    """Ask the user to input the name of a friend."""
    q = "({0} of {1}) Please enter a name, or enter \"DONE\": ".format(i, n)
    friend = input(q)
    return friend


def get_edge(pair):
    """Ask the user whether two friends are friends with each other."""
    q = "Do {0} and {1} like to spend time together? ".format(pair[0], pair[1])
    response = input(q)
    valid_responses = ['y', 'ye', 'yes', 'es', '1']
    connected = 0
    if response.lower() in valid_responses:
        connected = 1
    return (pair, connected)


if __name__ == "__main__":
    name = input("Please enter your name: ")
    pid = input("Please enter your participant ID: ")

    print("\nPlease carefully read the following.\n")

    print("\nConsider the people with whom you like to spend your free time. "
          "In the last few months, who are the people you have been with most "
          "often for informal social activities, such as going out to lunch, "
          "dinner, drinks, films, visiting one another's homes, studying "
          "together, exercising together, and so on?\n")

    n_friends = 10
    friends = list()
    for i in range(n_friends):
        new_friend = get_friend(i + 1, n_friends)
        if new_friend == "DONE":
            break
        else:
            friends.append(new_friend)
    print("Friends: ")
    print(friends)

    print("\nNow we will ask you to consider each pair of names provided. "
          "Each of these people is someone who you like to spend time with. "
          "For each pair of people, please indicate whether those two people "
          "like to spend time with each other. Does this pair of people engage"
          " in informal social activity, such as going out to lunch, dinner, "
          "drinks, films, visting one another's homes, studying together, "
          "exercising together, and so on?\n")

    pairs = itertools.combinations(friends, 2)
    edges = []
    for pair in pairs:
        edges.append(get_edge(pair))
    print("Edges: ")
    print(edges)