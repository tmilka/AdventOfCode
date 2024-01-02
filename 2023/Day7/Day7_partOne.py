def CheckforEnd(instruction):
    if instruction == "ZZZ":
        return True
    else:
        return False

# Read data from the file
with open('2023\Day7\input1.txt', 'r') as file:
    instructions = file.readline().strip()
    emptyLine = file.readline() #empty line gets stored in a var to avoid
    lines = file.readlines()

#prep instructions
letters = list(instructions)
print("prep instructions")
print(letters)

#prep directions
data = {}

for line in lines:
    cleanLine = line.strip()
    parts = cleanLine.split("=")

    last = parts[0].strip()
    nextMove = parts[1].strip()

    nextMove = nextMove.replace('(', '')
    nextMove = nextMove.replace(')', '')
    
    nextMove = nextMove.split(",")
    nextMove[1] = nextMove[1].strip()
    data[last] = nextMove

for last, nextMove in data.items():
    print(f"{last}: {nextMove}")

#######################################################
# get start value

#lastInstruction, startValues = next(iter(data.items()))
#print(lastInstruction)
lastInstruction = "AAA"
counter = 0 #kept track of the amount of instructions
end = False

def simDirections(letters, data, counter, end, lastInstruction):

    for instruction in letters: #instruction R/L
        NextInstrution = data[lastInstruction]
        counter += 1
        if instruction == "L":
            #take data on left side
            lastInstruction = NextInstrution[0]
            if CheckforEnd(lastInstruction):
                end = True
                break
        else:
            lastInstruction = NextInstrution[1]
            if CheckforEnd(lastInstruction):
                end = True
                break
    return counter, lastInstruction, end

while end == False:
    counter, lastInstruction, end = simDirections(letters, data, counter, end, lastInstruction)
    print(counter)
    print(end)

print(counter)