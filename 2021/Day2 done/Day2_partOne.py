# Read data from the file
with open('2021/Day2/input.txt', 'r') as file:
    instructions = file.readlines()

# Initialize starting position
current_position = [0, 0]  # [horizontal, depth]

# List with instructions
movements = []

for instruction in instructions:
    direction, distance = instruction.split()
    distance = int(distance)
    if direction == "forward":
        new_position = current_position[0] + distance
        current_position[0] = new_position
    elif direction == "down":
        new_position = current_position[1] + distance
        current_position[1] = new_position
    elif direction == "up":
        new_position = current_position[1] - distance
        current_position[1] = new_position

print(current_position)

#get final result
resultH = current_position[0]
resultD = current_position[1]

result = resultD * resultH

print(result)
