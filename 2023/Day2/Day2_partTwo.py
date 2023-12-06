FILE = 'input.txt'

# 1. part -  What is the sum of the IDs of possible games?
BAG_CAP = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open(FILE) as f:
    sum_of_ids = 0
    
    for game_id, line in enumerate(f.readlines(), 1): # assume game_id goes 1, 2, ...
        cube_sets = line.strip().split(": ")[1].split("; ")

        possible = True
        for cube_set in cube_sets:
            cubes = cube_set.split(", ")

            for cube in cubes:
                count, color = cube.split(" ")

                if BAG_CAP[color] < int(count):
                    possible = False
                    break

            if not possible:
                break

        if possible:
            sum_of_ids += game_id

    print(sum_of_ids)


# 2. part -  What is the sum of the power of these sets?
with open(FILE) as f:
    sum_of_powers = 0
    
    for line in f.readlines():
        cube_sets = line.strip().split(": ")[1].split("; ")
        bag = {'red': 0, 'green': 0, 'blue': 0}

        for cube_set in cube_sets:
            cubes = cube_set.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                bag[color] = max(bag[color], int(count))

        sum_of_powers += bag['red'] * bag['green'] * bag['blue']

    print(sum_of_powers)
