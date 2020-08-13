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

discovered_rooms = {}
visited = []
opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def get_moving_direction(curr_room):
    for dir in discovered_rooms[curr_room]:
        if discovered_rooms[curr_room][dir] == '?':
            # print(dir)
            return dir
    
    del visited[-1]
    for key, value in discovered_rooms[visited[-1]].items(): 
        if value == curr_room:
            # print("opposite_directions[key] ", opposite_directions[key])
            return opposite_directions[key]
       

visited.append(player.current_room.id)
discovered_rooms[player.current_room.id] = {}
for door in player.current_room.get_exits():
    discovered_rooms[player.current_room.id][door] = '?'

while len(discovered_rooms) < len(room_graph):
# for i in range(0, 10):

    direction = get_moving_direction(player.current_room.id)
    # print("direction", direction)
    # print("discovered rooms ", discovered_rooms)
    player.travel(direction)
    traversal_path.append(direction)
    if player.current_room.id != visited[-1]:
        visited.append(player.current_room.id)
    # print("I'm in room ", player.current_room.id)
    # print("visited", visited)
    if player.current_room.id not in discovered_rooms.keys():
        discovered_rooms[player.current_room.id] = {}
        for door in player.current_room.get_exits():
            discovered_rooms[player.current_room.id][door] = '?'
    if discovered_rooms[player.current_room.id][opposite_directions[direction]] == '?':
        discovered_rooms[visited[-2]][direction] = player.current_room.id
        discovered_rooms[player.current_room.id][opposite_directions[direction]] = visited[-2]
    




# print("main graph", discovered_rooms)



# TODO:
## traversal_path = directions I'm moving to

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
