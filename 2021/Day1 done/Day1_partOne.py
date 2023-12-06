lines = open('2021\input.txt', 'r').readlines()

measurements = []
increased = 0

for i, line in enumerate(lines):
    if (i != 0):
        if (line > lines[i -1]): # new line previous line
            measurements.append((line, "increased"))
        else:
            #measurements.append((line, "decreased"))
            pass
        
        print(line + '/' + lines[i -1])

#print(measurements)

print(len(measurements))

# result still wrong by 1! The correct result should be 1681 and not 1680
