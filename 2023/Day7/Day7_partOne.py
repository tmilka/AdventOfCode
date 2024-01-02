"""
five of a kind

four of a kind

full house

three of a kind

two pair 

one pair 

high card


other case both have the same rank 
the one with the first highest card wins
until there is a winner

"""
strenght_ofCards = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

def rank_value(hand_rank):
    ranks_order = {'Five of a kind': 1, 'Four of a kind': 2, 'Full house': 3,
                   'Three of a kind': 4, 'Two pair': 5, 'One pair': 6, 'High card': 7}
    
    return ranks_order[hand_rank[0]]

def get_hand_rank(hand):
    # Count occurrences of each card
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    # Sort card counts in descending order
    sorted_counts = sorted(card_counts.values(), reverse=True)

    print(sorted_counts)

    if sorted_counts[0] == 5:
        return 'Five of a kind'
    elif sorted_counts[0] == 4:
        return 'Four of a kind'
    elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return 'Full house'
    elif sorted_counts[0] == 3:
        return 'Three of a kind'
    elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return 'Two pair'
    elif sorted_counts[0] == 2:
        return 'One pair'
    else:
        return 'High card'

# Read data from the file
with open('2023\Day7\input.txt', 'r') as file:
    lines = file.readlines()

split_list = []
hands = []

# seperate cards and bets in two list
for line in lines:
    split_list = line.split()

    hands.append((list(split_list[0]),list(split_list[1])))

for hand in hands:
    get_hand_rank(hand)
    print(hand)