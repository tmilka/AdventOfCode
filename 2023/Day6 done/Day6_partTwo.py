# Read data from the file
with open('2023\Day6 done\input.txt', 'r') as file:
    lines = file.readlines()

data = {}

# prep data in two lists time_list / distance_list
for line in lines:
    
    parts = line.split(":")

    category = parts[0].strip()

    numbers = [int(num) for num in parts[1].split()]

    data[category] = numbers

for category, numbers in data.items():
    print(f"{category}: {numbers}")


time_list = data["Time"]
distance_list = data["Distance"]
results = []
time_product = ""
distance_product = ""

# combine the numbers
for time, distance in zip(time_list, distance_list):
    time_product += str(time)
    distance_product += str(distance)

print(time_product)
print(distance_product)

#change data type back to int
time_product = int(time_product)
distance_product = int(distance_product)

# var dump
holdtime = 0  # dynamic
time = time_product
speed = 0
distanceRecord = distance_product 
ways = 0 #ways of winning

while holdtime < time:
    # Increase hold time
    holdtime += 1
    restTime = time - holdtime
    speed = holdtime
    distance = restTime * speed

    #winning condition distance > distanceRecord
    if distance > distanceRecord:
        ways +=1

    # Check for end of loop and safe results in a list
    if holdtime == time:
        results.append(ways)

# calculate final result
result = 1 #set 1 so it starts right 
for number in results:
    result *= number

print(result)
