from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4


groups = get_input(7).strip()


groups = apply(groups, lambda x: x.split("\n"))
groups = apply(groups, lambda x: x.split(" "))


card_strength = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 13,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
}

print("groups", groups)
for g in groups:
    print(g)


def eval_hand(hand, tiebreak_hand):
    # count letters
    hand_tiebreak_value = "_".join([f"{card_strength[l]:02}" for l in tiebreak_hand])
    letters = {}
    for c in hand:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    # check if 5 of a kind
    for c in letters:
        if letters[c] == 5:
            return f"0_{hand_tiebreak_value}"
    for c in letters:
        if letters[c] == 4:
            return f"1_{hand_tiebreak_value}"
    # check if full house
    if len(letters) == 2:
        if set(letters.values()) == {2, 3}:
            return f"2_{hand_tiebreak_value}"
    for c in letters:
        if letters[c] == 3:
            return f"3_{hand_tiebreak_value}"
    # check if two pairs
    if len(letters) == 3:
        if len([c for c in letters if letters[c] == 2]) == 2:
            return f"4_{hand_tiebreak_value}"
    # check if one pair
    if len(letters) == 4:
        return f"5_{hand_tiebreak_value}"
    return f"6_{hand_tiebreak_value}"


def eval_hand_joker(hand, start_index=-1, tiebreak_hand=None):
    if tiebreak_hand is None:
        tiebreak_hand = hand
    j_indices = [i for i, x in enumerate(hand) if x == "J" and i > start_index]
    
    if len(j_indices) == 0:
        return eval_hand(hand, tiebreak_hand)
    
    j_index = j_indices[0]
        
    return min(eval_hand_joker(hand[:j_index] + l + hand[j_index + 1:], j_index, tiebreak_hand) for l in "AKQJT98765432")


groups.sort(key=lambda x: eval_hand_joker(x[0]))

rank = len(groups)
winnings = 0
for hand in groups:
    winnings += rank * int(hand[1])
    rank -= 1

print("Winning", winnings)
