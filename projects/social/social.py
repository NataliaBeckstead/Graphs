import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    def __str__(self):
        return 'Queue: {self.queue}'.format(self=self)

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
    
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User {i}")

        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):

        paths = {}

        for user in self.users:
            if user == user_id:
                paths[user] = [user]
                continue
            q = Queue()
            visited = set()
            path = [user_id]
            q.enqueue(path)

            while q.size() > 0:
                current_path = q.dequeue()
                current_node = current_path[-1]
                if current_node == user:
                    paths[user] = current_path
                    break
                if current_node not in visited:
                    visited.add(current_node)
                    for next_vertex in self.friendships[current_node]:
                        path_copy = list(current_path)
                        path_copy.append(next_vertex)
                        q.enqueue(path_copy)
                paths[user] = ["No connections"]

        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
