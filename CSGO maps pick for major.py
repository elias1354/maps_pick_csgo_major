from time import sleep
import random


# Input
time = input("---Team name:\n-").strip()
time = time.title()
# Lists
maps_pool = ['inferno', 'mirage', 'nuke',
             'overpass', 'ancient', 'vertigo', 'dust 2']
list.sort(maps_pool)  # ordernar ordem alfabética
maps_pool = [item.title() for item in maps_pool]

# Variables


# Heads and tail ---- not done yet
'''while True:
    ht_p1 = input("Heads and tail: ")
    head = ht_p1
    tail = ht_p1
    ht_b1 = random.choice(head,tail)
    if ht_p1 in head or ht_p1 in tail:
        while True:
            try:
                head.remove()'''


# Process Player remove
print("---Activy duty map pool\n{}".format(maps_pool))
while True:
    rmv_map_p1 = input("Chose a map to remove:\n").strip()
    rmv_map_p1 = rmv_map_p1.title()
    if rmv_map_p1 in list(maps_pool):
        print("---Removing {} from map pool".format(rmv_map_p1,))
        sleep(1)
        for item in maps_pool.copy():
            if rmv_map_p1 in maps_pool:
                while True:
                    try:
                        maps_pool.remove(rmv_map_p1)
                    except:
                        break
        break
    else:
        print("---Chose again\n{}".format(maps_pool))
print('---{}'.format(maps_pool))

# Bot choice
print("Waiting opponent...")
sleep(2)
rmv_map_b1 = random.choice(maps_pool)
print(rmv_map_b1)
for item in maps_pool.copy():
    if rmv_map_b1 in maps_pool:
        while True:
            try:
                maps_pool.remove(rmv_map_b1)
            except:
                break
print("--- {} Map removed by bot\n{}".format(rmv_map_b1, maps_pool))
# Pick map Player
while True:
    pick_map_p1 = input("Chose a map to play in\n").strip()
    pick_map_p1 = pick_map_p1.title()
    if pick_map_p1 in maps_pool:
        print("Adding {} to matchmaking".format(pick_map_p1))
        sleep(1)
        for item in maps_pool.copy():
            if pick_map_p1 in maps_pool:
                while True:
                    try:
                        maps_pool.remove(pick_map_p1)
                    except:
                        break
        break
    else:
        print("---Chose again\n{}".format(maps_pool))
print("{}\n---Your choice for the matchmaking was {}".format(maps_pool, pick_map_p1))
# bot pick map
print("Waiting opponent...")
sleep(2)
pick_map_b1 = random.choice(maps_pool)
pick_map_b1 = pick_map_b1.title()
for item in maps_pool.copy():
    if pick_map_b1 in maps_pool:
        while True:
            try:
                maps_pool.remove(pick_map_b1)
            except:
                break
print("---{} was the map pick for matchmaking by bot".format(pick_map_b1))
print("---Resting the maps below\n{}".format(maps_pool))
print("First matchmaking starting with {} chosen by {} and second one with {} ".format(
    pick_map_p1, time, pick_map_b1))
