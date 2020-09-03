from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt" 
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt" 

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
shortest_path = []

discovered_rooms = {}
visited = []
opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

directions = ['n', 's', 'w', 'e']
def get_moving_direction(curr_room):
    
    for dir in sorted(discovered_rooms[curr_room]):
        if discovered_rooms[curr_room][dir] == '?':
            return dir

    # global directions
    # random.shuffle(directions)
    # if directions[0] in discovered_rooms[curr_room] and discovered_rooms[curr_room][directions[0]] == '?':
    #     return directions[0]
    # if directions[1] in discovered_rooms[curr_room] and discovered_rooms[curr_room][directions[1]] == '?':
    #     return directions[1]
    # if directions[2] in discovered_rooms[curr_room] and discovered_rooms[curr_room][directions[2]] == '?':
    #     return directions[2]
    # if directions[3] in discovered_rooms[curr_room] and discovered_rooms[curr_room][directions[3]] == '?':
    #     return directions[3]
    
    del visited[-1]
    for key, value in discovered_rooms[visited[-1]].items(): 
        if value == curr_room:
            return opposite_directions[key]

visited.append(player.current_room.id)
discovered_rooms[player.current_room.id] = {}
for door in player.current_room.get_exits():
    discovered_rooms[player.current_room.id][door] = '?'

while len(discovered_rooms) < len(room_graph):
    direction = get_moving_direction(player.current_room.id)
    player.travel(direction)
    traversal_path.append(direction)
    if player.current_room.id != visited[-1]:
        visited.append(player.current_room.id)
    if player.current_room.id not in discovered_rooms.keys():
        discovered_rooms[player.current_room.id] = {}
        for door in player.current_room.get_exits():
            discovered_rooms[player.current_room.id][door] = '?'
    if discovered_rooms[player.current_room.id][opposite_directions[direction]] == '?':
        discovered_rooms[visited[-2]][direction] = player.current_room.id
        discovered_rooms[player.current_room.id][opposite_directions[direction]] = visited[-2]

#################### Brutal force searching shortest path ###################

# for i in range(0, 150000):
#     traversal_path.clear()
#     discovered_rooms.clear()
#     visited.clear()
#     player = Player(world.starting_room)

#     visited.append(player.current_room.id)
#     discovered_rooms[player.current_room.id] = {}
#     for door in player.current_room.get_exits():
#         discovered_rooms[player.current_room.id][door] = '?'

#     while len(discovered_rooms) < len(room_graph):
#         direction = get_moving_direction(player.current_room.id)
#         player.travel(direction)
#         traversal_path.append(direction)
#         if player.current_room.id != visited[-1]:
#             visited.append(player.current_room.id)
#         if player.current_room.id not in discovered_rooms.keys():
#             discovered_rooms[player.current_room.id] = {}
#             for door in player.current_room.get_exits():
#                 discovered_rooms[player.current_room.id][door] = '?'
#         if discovered_rooms[player.current_room.id][opposite_directions[direction]] == '?':
#             discovered_rooms[visited[-2]][direction] = player.current_room.id
#             discovered_rooms[player.current_room.id][opposite_directions[direction]] = visited[-2]

#     if i == 0:
#         shortest_path = traversal_path[:]
#     if len(shortest_path) > len(traversal_path):
#         shortest_path = traversal_path[:]

    
# player = Player(world.starting_room)
# traversal_path = shortest_path[:]
# print(traversal_path)

############## Best result so far 967 moves #######################
# traversal_path = ['n', 's', 'e', 'e', 'w', 's', 'e', 's', 'n', 'w', 's', 's', 'e', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 
#                     'w', 'n', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's', 'n', 'n', 'e', 's', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 's', 's', 'n', 'n', 'e', 'e', 'w', 's', 's', 's', 's', 'n', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 's', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 'w', 'n', 's', 'e', 's', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'w', 's', 'n', 'e', 's', 'n', 'n', 'e', 'n', 'w', 'e', 'n', 'n', 'n', 'n', 'e', 'w', 'w', 'e', 's', 'w', 'e', 's', 
#                     'w', 'w', 's', 'n', 'e', 'e', 's', 'w', 'e', 's', 's', 'e', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'n', 'n', 'e', 'e', 's', 'e', 's', 's', 'e', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'n', 'e', 'n', 's', 'e', 'w', 'w', 'n', 'n', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 'n', 'w', 'w', 'n', 'w', 's', 's', 'n', 'n', 'n', 'e', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 'w', 's', 'n', 'w', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'e', 'n', 'e', 'w', 
#                     's', 'w', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'w', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'n', 's', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'n', 's', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 'n', 'n', 'e', 'n', 'n', 's', 's', 'w', 'n', 'n', 's', 's', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 'n', 's', 'e', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w', 's', 'e', 's', 's', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'w', 'w', 'e', 'e', 's', 'e', 's', 's', 's', 'e', 's', 'e', 'e', 'w', 'n', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'n', 's', 'w', 's', 'w', 's', 'w', 'n', 's', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'n', 'n', 'n', 'e', 'n', 'e', 'n', 'e', 's', 'n', 'e', 'w', 'w', 'n', 's', 's', 'w', 'n', 's', 
#                     's', 'w', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'w', 's', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 'w', 'n', 'w', 'n', 's', 'e', 'n', 's', 's', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's', 'w', 'w', 'w', 'n', 's', 'e', 'n', 's', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'e', 'e', 's', 'e', 'w', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 'w', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 's', 's', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 's', 's', 
#                     's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'e', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'e', 'e', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 'w', 'w', 'w', 'n', 'n', 's', 'w', 'w', 's', 'n', 'w', 'e', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'n', 's', 's', 'e', 's', 'w', 'e', 'e', 'e', 'e', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 's', 's', 'n', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'w', 'e', 'n', 's', 'e', 'n', 's', 's', 'w', 'w', 'e', 's', 'e', 's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 's', 'e', 'e', 'e', 's', 's', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 's', 'w', 'e', 'n', 'w', 'e', 'n', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 'e', 's', 's', 's', 'w', 'e', 
#                     'n', 'e', 'w', 'n', 'n', 'w', 's', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 's', 'e', 's', 'w', 'e', 'n', 'w', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'e', 's', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'w', 'e', 'n', 'n', 'e', 's', 's', 's', 'e', 'w', 's', 'e']

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
