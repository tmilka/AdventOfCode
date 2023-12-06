# Read data from the file
with open('2021/input.txt', 'r') as file:
    lines = file.readlines()

# Convert lines to a list of integers
measurements = [int(line.strip()) for line in lines]

# Define a three-measurement sliding window function
def sliding_window(data):
    result = []
    for i in range(len(data) - 2):
        window = data[i:i+3]
        result.append(window)
    return result

# Apply the sliding window to the measurements
result = sliding_window(measurements)

increased = 0

# check if increased or decreased
for i, entry in enumerate(result):
    if (sum(entry) > sum(result[i -1])):
        increased +=1
        #print('increased')
    else:
        pass

print(increased)
