# Read data from the file
with open('2021/Day2/input.txt', 'r') as file:
    instructions = file.readlines()

# Initialize starting position
current_position = [0, 0, 0]  # [horizontal, depth, aim]

# List with instructions
movements = []

for instruction in instructions:
    direction, distance = instruction.split()
    distance = int(distance)
    if direction == "forward":
        new_position = current_position[0] + distance
        current_position[0] = new_position
        # calculate depth
        new_depth = current_position[2] * distance
        current_position[1] += new_depth
        print(current_position[1])
    elif direction == "down":
        # calculate aim increase
        new_aim = current_position[2] + distance # aim + X
        current_position[2] = new_aim
    elif direction == "up":
        # calculate aim decrease
        new_aim = current_position[2] - distance # aim - X
        current_position[2] = new_aim

print(current_position)

#get final result
resultH = current_position[0]
resultD = current_position[1]
resultA = current_position[2]

result = resultD * resultH

print(resultA)
print(result)
