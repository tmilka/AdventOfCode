import re

input_counts = {'red': 12, 'blue': 14, 'green': 13}

input = """Game 1: 7 blue, 5 red; 10 red, 7 blue; 5 blue, 4 green, 15 red; 4 green, 6 red, 7 blue; 5 green, 8 blue, 4 red; 5 red, 4 blue, 3 green
Game 2: 8 green, 3 red; 7 blue, 6 red, 8 green; 7 blue, 3 green, 6 red; 8 green, 6 blue, 11 red; 6 blue, 3 green, 12 red
Game 3: 6 blue, 3 red, 7 green; 3 red, 3 green, 8 blue; 8 blue, 11 red, 4 green; 5 blue, 7 red, 6 green; 9 blue, 7 green, 1 red
Game 4: 3 red, 4 green; 5 red, 1 blue; 2 green; 3 green, 1 blue; 2 green, 1 blue, 1 red
Game 5: 17 red, 5 blue, 3 green; 8 green, 9 red, 10 blue; 2 green, 9 blue, 4 red
Game 6: 5 blue, 6 green, 3 red; 1 green, 8 blue, 12 red; 2 blue, 13 red, 6 green
Game 7: 1 green, 1 blue, 6 red; 1 red, 8 green; 3 red, 8 green, 2 blue; 14 green, 4 blue, 4 red; 4 green, 5 blue; 7 green, 2 blue, 1 red
Game 8: 6 blue, 9 red, 3 green; 2 red, 6 blue; 2 green, 1 red, 2 blue; 2 green, 9 blue, 6 red
Game 9: 5 green, 8 blue, 8 red; 2 blue, 6 green, 8 red; 6 red, 9 green
Game 10: 2 red, 2 blue, 12 green; 8 green, 3 red; 5 blue, 11 red, 6 green; 14 red, 1 green
Game 11: 2 green, 1 red, 1 blue; 4 blue, 7 red; 7 red, 7 green, 5 blue; 2 blue, 3 red, 6 green; 3 blue, 9 red, 7 green
Game 12: 9 green, 7 red, 7 blue; 6 green, 4 blue, 1 red; 3 blue, 5 red, 7 green; 9 green, 10 red, 12 blue; 11 green, 5 red; 9 blue, 12 green, 3 red
Game 13: 7 blue, 7 red, 2 green; 5 blue, 5 green, 7 red; 1 blue, 10 red; 11 red, 2 blue, 1 green; 1 green, 1 blue, 4 red
Game 14: 2 blue, 10 red; 3 blue, 6 green, 17 red; 3 green, 4 blue, 14 red
Game 15: 7 blue, 2 green, 4 red; 7 blue, 3 red, 3 green; 4 red, 2 green, 1 blue; 2 red, 9 green, 5 blue; 2 red, 4 green, 5 blue
Game 16: 5 blue, 1 red; 8 blue, 1 green; 5 green, 3 blue, 2 red; 8 blue, 2 green; 2 red, 2 blue, 5 green
Game 17: 2 blue, 5 red; 7 red, 1 blue; 2 blue, 2 green, 3 red; 3 blue, 2 red, 1 green; 5 green, 7 red; 6 red, 3 green
Game 18: 4 blue, 1 red, 14 green; 8 red, 4 blue, 14 green; 6 red, 11 blue, 10 green; 5 blue, 2 green, 3 red; 16 green, 10 blue, 2 red; 6 red, 4 blue, 12 green
Game 19: 10 green, 12 red, 12 blue; 5 blue, 12 red, 7 green; 15 red, 8 blue, 6 green; 13 green, 1 red, 10 blue; 4 blue, 8 red, 9 green; 16 red, 7 green, 3 blue
Game 20: 10 blue, 9 green; 9 blue, 1 red, 3 green; 11 blue; 6 blue; 8 blue, 10 green
Game 21: 4 blue, 4 red; 1 green, 3 red, 3 blue; 4 blue, 1 green, 2 red
Game 22: 5 blue, 4 green, 1 red; 14 green, 4 blue, 1 red; 4 blue, 4 red, 13 green
Game 23: 6 red, 8 green; 4 green, 1 blue, 7 red; 10 green, 5 red; 2 red, 9 green
Game 24: 1 blue, 10 green; 12 green, 5 blue; 1 red, 3 green; 2 red, 4 blue
Game 25: 2 blue, 3 red, 13 green; 7 blue, 15 green, 1 red; 7 blue, 2 green
Game 26: 20 red, 5 blue, 4 green; 1 green, 8 blue, 11 red; 7 blue, 6 red, 2 green; 4 green, 7 blue, 4 red; 5 red, 8 blue
Game 27: 3 red, 3 green, 1 blue; 3 red, 1 blue, 8 green; 3 blue, 4 red
Game 28: 1 blue, 15 red, 2 green; 15 red; 3 red, 2 green; 3 red, 1 green
Game 29: 4 blue, 7 green, 1 red; 5 green, 9 red; 8 green, 1 red, 10 blue; 2 blue, 1 green
Game 30: 9 blue, 5 red, 6 green; 15 red, 6 blue, 3 green; 13 red, 2 blue, 4 green; 2 green, 3 blue; 13 red, 8 blue; 5 green, 6 blue, 17 red
Game 31: 1 green, 9 blue, 9 red; 4 green, 8 red, 1 blue; 10 blue, 2 green; 1 red, 1 blue; 1 red, 1 blue; 6 blue, 9 red, 5 green
Game 32: 7 red, 7 green, 3 blue; 14 green, 11 red, 11 blue; 10 green, 7 red, 2 blue; 1 green, 4 blue, 4 red; 9 blue, 10 green, 5 red
Game 33: 12 red, 4 green, 11 blue; 4 blue, 10 red, 1 green; 7 green, 10 red, 16 blue; 15 red, 5 blue; 10 green, 4 red; 8 green, 5 blue, 6 red
Game 34: 8 blue, 1 red, 2 green; 3 green, 3 blue, 4 red; 6 red, 3 green; 6 red; 9 blue, 4 red, 3 green
Game 35: 6 green, 6 blue, 1 red; 3 green, 3 blue; 1 red, 5 blue, 2 green; 1 red, 13 green, 1 blue; 3 green, 1 red, 10 blue; 5 green, 4 blue
Game 36: 15 blue, 1 red; 2 red, 3 green, 17 blue; 6 blue, 7 red, 8 green; 12 red, 7 green, 14 blue; 4 blue, 2 red; 8 green, 12 blue, 10 red
Game 37: 2 green, 2 blue; 6 red, 3 blue, 1 green; 2 green, 3 blue, 1 red
Game 38: 2 blue, 7 red, 9 green; 3 red, 18 green, 6 blue; 6 red, 19 green, 2 blue; 2 blue, 13 green, 7 red
Game 39: 12 blue, 7 green, 3 red; 16 green, 6 blue; 1 red, 4 green, 2 blue; 15 blue, 2 red, 2 green
Game 40: 18 blue, 1 red; 4 green, 15 blue; 5 green, 17 blue, 3 red; 4 red, 16 blue, 2 green
Game 41: 3 blue, 14 green; 11 green, 8 blue; 14 blue, 4 red, 1 green; 5 blue, 2 red, 15 green
Game 42: 7 red, 9 green; 10 red, 19 green, 10 blue; 16 blue, 8 green, 7 red; 6 blue, 11 green, 7 red
Game 43: 1 blue, 5 red; 8 red, 2 green, 1 blue; 4 red, 3 green; 2 green, 1 red
Game 44: 5 green, 13 blue, 12 red; 18 blue, 3 green, 8 red; 2 green, 3 blue, 11 red
Game 45: 3 blue, 1 red, 4 green; 2 blue, 1 red; 1 blue, 4 green; 3 red, 16 green
Game 46: 10 red, 1 green, 4 blue; 4 green, 14 blue, 2 red; 12 red, 3 blue, 2 green; 4 green, 2 red, 2 blue; 2 red, 1 green, 11 blue; 2 green, 19 blue
Game 47: 10 blue, 10 green, 3 red; 3 red, 11 blue, 9 green; 4 blue, 10 green
Game 48: 5 green, 1 blue; 4 red, 8 green, 8 blue; 17 red, 5 blue, 2 green; 12 green, 18 red, 7 blue; 15 green, 14 red, 8 blue; 11 green, 1 blue, 16 red
Game 49: 2 red, 4 green, 1 blue; 1 green, 5 blue, 2 red; 8 green, 3 blue, 1 red; 4 blue, 3 red, 9 green
Game 50: 2 blue; 7 green, 5 red; 3 red, 3 blue; 5 green, 1 blue, 2 red; 5 blue, 3 green; 4 green, 3 blue, 1 red
Game 51: 6 green, 13 blue, 3 red; 7 blue, 7 green, 1 red; 15 green, 2 red, 13 blue; 1 red, 7 blue, 3 green; 11 blue, 16 green, 1 red
Game 52: 5 blue, 2 green, 14 red; 4 blue, 3 red; 10 green, 7 red; 1 blue, 10 green, 10 red; 9 blue, 5 green, 12 red
Game 53: 1 green, 2 red, 1 blue; 4 green; 1 green; 2 green; 2 green, 1 red
Game 54: 3 green, 11 blue; 12 blue; 1 red, 3 blue; 7 blue, 1 red
Game 55: 7 green, 7 red; 1 blue, 7 green, 14 red; 17 red, 2 blue, 5 green; 1 blue, 7 red; 2 blue, 3 green, 14 red
Game 56: 3 blue, 2 red, 1 green; 1 red, 4 blue, 2 green; 5 green, 1 red, 2 blue; 7 blue
Game 57: 1 blue, 14 red, 7 green; 2 red, 1 green; 1 blue, 6 red, 6 green
Game 58: 11 red, 2 green; 3 green, 8 red, 8 blue; 10 red, 1 green, 13 blue
Game 59: 11 green, 5 blue, 11 red; 13 red, 6 blue, 11 green; 6 red, 7 blue, 12 green; 9 blue, 9 red, 1 green
Game 60: 3 red, 8 blue, 4 green; 5 blue, 2 red, 3 green; 7 green, 3 red; 8 blue, 2 red, 7 green
Game 61: 17 red, 12 blue, 9 green; 20 green, 5 red, 14 blue; 9 blue, 11 green, 15 red; 14 green, 6 blue, 14 red; 16 green, 7 red, 4 blue
Game 62: 3 red, 11 blue, 16 green; 1 green, 6 red, 6 blue; 7 green, 6 red, 9 blue
Game 63: 3 blue, 20 red, 1 green; 11 red, 5 green; 13 red, 2 green; 15 red, 1 blue, 6 green
Game 64: 8 blue, 1 red, 11 green; 1 red, 11 blue, 4 green; 5 red, 7 green, 1 blue
Game 65: 3 blue, 13 green, 2 red; 2 blue, 3 red; 10 green, 8 blue, 2 red; 2 red, 6 blue, 8 green; 10 blue, 12 green
Game 66: 4 blue, 3 red, 8 green; 1 red, 9 green; 7 blue, 6 red, 6 green; 1 blue, 1 red, 11 green
Game 67: 10 blue, 15 green; 3 red, 2 blue, 1 green; 4 blue, 12 green, 2 red; 8 green, 11 blue, 8 red; 9 blue, 5 green, 6 red; 10 green, 4 red, 14 blue
Game 68: 4 green, 3 blue, 4 red; 9 green, 2 blue; 6 blue, 6 red, 10 green; 5 blue, 4 green, 5 red; 3 blue, 10 green; 5 blue, 5 red
Game 69: 6 blue, 1 red, 1 green; 4 red, 3 green, 2 blue; 5 green, 3 red, 5 blue; 5 red, 5 blue
Game 70: 2 green, 1 red; 12 green, 1 red, 11 blue; 7 green, 12 blue; 13 blue, 10 green
Game 71: 9 red, 9 green, 4 blue; 10 red, 1 blue, 12 green; 3 blue, 13 red, 3 green
Game 72: 2 red, 8 blue, 5 green; 2 green; 1 red, 5 green, 6 blue; 1 blue, 3 red, 12 green; 5 green, 14 blue, 1 red; 8 blue, 13 green
Game 73: 19 blue, 11 red, 8 green; 18 blue, 9 red, 11 green; 6 green, 19 blue, 6 red
Game 74: 2 green, 4 red, 2 blue; 1 green, 1 red, 4 blue; 2 red, 4 green, 2 blue; 3 red, 2 blue, 6 green
Game 75: 2 blue; 1 red, 1 blue, 1 green; 1 blue; 5 blue, 2 green; 1 green, 1 red, 3 blue
Game 76: 9 blue, 4 red, 3 green; 8 blue, 8 green, 3 red; 3 red, 2 green, 8 blue; 8 green, 6 blue, 5 red
Game 77: 7 blue, 17 green; 1 blue, 2 red, 18 green; 18 green, 1 blue, 2 red
Game 78: 2 red, 2 green, 1 blue; 5 green, 3 blue; 1 green, 2 blue; 2 blue, 6 red, 5 green
Game 79: 4 red, 6 green, 17 blue; 2 blue, 3 red, 8 green; 8 red, 19 blue, 12 green; 5 red, 8 green, 12 blue; 16 blue, 1 red, 12 green; 5 green, 18 blue, 8 red
Game 80: 1 blue, 4 red, 10 green; 6 green; 6 red, 3 green, 2 blue
Game 81: 2 green, 5 blue, 4 red; 3 red, 1 green, 14 blue; 3 red, 10 blue, 2 green
Game 82: 12 red, 5 blue, 2 green; 12 blue, 6 red, 5 green; 13 blue, 1 green, 3 red; 11 red, 3 blue; 4 red, 3 green
Game 83: 10 blue, 16 red, 4 green; 6 red, 2 blue, 14 green; 9 blue, 14 green; 7 blue, 1 red; 4 green, 2 red, 8 blue; 5 red, 7 green
Game 84: 3 red, 3 blue, 6 green; 9 red, 17 green, 16 blue; 13 blue, 7 red; 14 green, 2 red, 14 blue
Game 85: 7 blue; 8 red, 10 blue, 1 green; 6 blue, 9 red
Game 86: 9 red, 6 green, 9 blue; 1 blue, 5 red; 11 red, 1 green, 11 blue; 3 green, 8 blue; 8 red, 5 green, 4 blue; 15 blue, 4 green, 2 red
Game 87: 2 red, 2 green; 5 red, 2 blue; 6 red
Game 88: 2 green, 5 red; 9 blue, 7 red, 3 green; 1 blue, 2 green, 3 red; 3 green, 6 blue, 1 red; 1 red, 3 green, 6 blue
Game 89: 10 blue, 13 red; 15 red, 6 blue, 2 green; 2 green, 10 red, 18 blue; 1 green, 18 red, 8 blue
Game 90: 2 red, 2 blue, 9 green; 1 red, 9 green; 7 green, 3 blue, 2 red; 4 blue, 2 red, 4 green
Game 91: 6 green, 4 red, 9 blue; 4 green, 4 red, 17 blue; 6 blue, 2 red, 4 green; 7 green, 2 red, 13 blue; 1 green, 13 blue, 1 red
Game 92: 4 green, 1 blue, 8 red; 7 green, 6 red; 13 red; 9 green; 6 red, 1 blue, 4 green; 2 red, 1 blue, 15 green
Game 93: 8 green, 8 red, 13 blue; 4 red, 10 green; 15 blue, 11 red; 14 green, 5 red, 6 blue; 12 red, 3 blue, 13 green; 9 red, 10 green, 6 blue
Game 94: 14 red, 10 green; 15 red; 4 red; 4 green, 7 red, 1 blue; 6 red, 5 green; 1 red, 2 green
Game 95: 1 blue, 11 red; 15 red, 1 blue, 3 green; 13 red, 2 blue, 3 green; 1 green, 1 blue
Game 96: 4 red, 4 blue, 4 green; 5 blue, 5 green, 4 red; 2 red, 8 blue; 16 red, 5 green, 13 blue
Game 97: 6 red, 13 green, 3 blue; 10 green, 4 blue; 3 red, 12 green, 4 blue; 3 red, 5 blue, 16 green; 3 red, 9 green, 1 blue
Game 98: 8 red, 12 green, 2 blue; 7 green, 8 red, 1 blue; 2 blue, 6 red, 3 green; 9 red, 1 blue, 4 green
Game 99: 6 blue, 11 red, 7 green; 9 red, 6 green, 1 blue; 9 red, 2 blue
Game 100: 1 red, 4 blue, 2 green; 6 red, 2 green, 11 blue; 1 red, 1 blue, 2 green; 1 red, 7 blue"""

def parse_games(input_string):
    games = []

    # Split the input into individual games
    game_strings = re.split(r'Game \d+:', input_string)[1:]

    for game_str in game_strings:
        game_dict = {'red': 0, 'blue': 0, 'green': 0}

        # Extract color and number pairs using regex
        color_number_pairs = re.findall(r'(\d+)\s*([a-zA-Z]+)', game_str)

        for number, color in color_number_pairs:
            game_dict[color.lower()] += int(number)

        games.append(game_dict)

    return games

matching_items = []

###############################################################################################################################
#prepare input string to list
data = parse_games(input)

#get the values for each game
for game_number, item in enumerate(data, start=1):
    if all(item[color] <= input_counts[color] for color in ['red', 'blue', 'green']):
        matching_items.append({'Game': game_number, 'Data': item})

print("Matching items:", matching_items)

#################################################################################################################################
#extract the "Game" values in a new list "game_values"
game_values = [item['Game'] for item in matching_items]

# Sum the 'Game' values
sum_of_game_values = sum(game_values)

print("Sum of 'Game' values:", sum_of_game_values)
