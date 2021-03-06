from util import Stack, Queue 
from graph import Graph
import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        # print(self.users)

        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            # print(user_id)
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # print(possible_friendships)

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # print(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            # print(friendship)
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex (user) ID
        q = Queue()
        q.enqueue([user_id])

        # Create a Dictionary to store visited vertices
        visited = {}
        
        # Use breath-first-search to traverse friends and find the shortest friendship path
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first person and set to the path
            path = q.dequeue()
            # Grab the last vertex from the path and set it to our current person
            current_person = path[-1]

            # print(visited.keys())

            # If the current person is not in our visited dictionary (keeps from returning an empty dictionary if no friends)
            if current_person not in visited:
                # Set the path to the current person
                visited[current_person] = path

            # Loop through every friend
            for friend in self.friendships[current_person]:
                # print(friend)
                # Check to see if we have visited all the nodes
                if friend not in visited.keys():
                    # Make a new list from the path
                    path_copy = path.copy()
                    # Add the friend to the new path
                    path_copy.append(friend)
                    #Add our path to the queue
                    q.enqueue(path_copy)
                    # Add the path copy to our visited dictionary using the key of the current_person
                    visited[current_person] = path_copy

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
