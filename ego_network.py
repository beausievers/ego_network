"""A bare-bones egocentric network survey."""

import csv


def get_friend(i, n):
    """Ask the user to input the name of a friend."""
    q = ("({0} of {1}) Please enter a name, "
         "or enter \"DONE\": ".format(i, n))
    friend = input(q)
    return friend

if __name__ == "__main__":
    name = input("Please enter your name: ")
    pid = input("Please enter your participant ID: ")

    print("\nConsider the people with whom you like to spend your free time. In "
          "the last few months, who are the people you have been with most "
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
