strenght_ofCards = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

hand_ranks = [('One pair', ['3', '2', 'T', '3', 'K']),
              ('Three of a kind', ['T', '5', '5', 'J', '5']),
              ('Two pair', ['K', 'K', '6', '7', '7']),
              ('Two pair', ['K', 'T', 'J', 'J', 'T']),
              ('Three of a kind', ['Q', 'Q', 'Q', 'J', 'A'])]

def rank_value(hand_rank):
    ranks_order = {'Five of a kind': 1, 'Four of a kind': 2, 'Full house': 3,
                   'Three of a kind': 4, 'Two pair': 5, 'One pair': 6, 'High card': 7}
    
    return ranks_order[hand_rank[0]]

# Sort the list of tuples based on the ranks and highest cards
sorted_hands = sorted(hand_ranks, key=lambda x: (rank_value(x), strenght_ofCards[max(x[1], key=strenght_ofCards.get)]), reverse=True)



# Print sorted hands
for rank, hand in sorted_hands:
    print(f"{rank} - {hand}")
