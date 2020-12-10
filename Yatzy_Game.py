import collections
import random
from random import shuffle

list_of_players = []
scoring_pad = {}
Player = collections.namedtuple('Player', 'player, Scoring_pad,  dice')


def rolling(no_of_dice: int):
    for _ in range(no_of_dice):
        yield random.randint(1, 6)


def chan_ce():
    no_of_dice = 5
    chance = 0
    stored_dice = list()
    while True:
        if len(stored_dice) == 5 or chance == 3:
            break
        elif chance == 2:
            inpu_t = input('Enter start to start or quit to quit this round: ')
            if inpu_t != 'quit' and inpu_t == 'start':
                result = list(rolling(no_of_dice - len(stored_dice)))
                print(result)
                for die in result:
                    stored_dice.append(die)
                chance += 1
            elif inpu_t == 'quit':
                break
            else:
                print('Please enter correct choice:')
        else:
            inpu_t = input('Enter start to start or quit to quit this round: ')
            if inpu_t != 'quit' and inpu_t == 'start':
                result = list(rolling(no_of_dice - len(stored_dice)))
                print(result)
                hold_val = list(map(int, input('Please enter position of dice you want '
                                               'to hold with space(if nothing enter 0): ').split(' ')))
                if 0 not in hold_val:
                    for j in hold_val:
                        stored_dice.append(result[j - 1])
                chance += 1
            elif inpu_t == 'quit':
                break
            else:
                print('Please enter correct choice:')
    return stored_dice


def num_ones(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 1:
            count = count + 1
    return count


def num_twos(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 2:
            count = count + 1
    return count


def num_threes(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 3:
            count = count + 1
    return count


def num_fours(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 4:
            count = count + 1
    return count


def num_fives(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 5:
            count = count + 1
    return count


def num_sixes(dice_s, p_layer):
    count = 0
    for i in dice_s:
        if i == 6:
            count = count + 1
    return count


def single_pair(dice_s, p_layer):
    score_for_single_pair = 0
    for i in set(dice_s):
        dice_s.remove(i)
    if len(dice_s) != 0:
        score_for_single_pair = 2 * max(dice_s)
    return score_for_single_pair


def double_pair(dice_s, p_layer):
    score_for_double_pair = 0
    lis_t = set(dice_s)
    for i in lis_t:
        dice_s.remove(i)
    if len(dice_s) > 1:
        score_for_double_pair += 2 * sum(dice_s)
    return score_for_double_pair


def three_of_a_kind(dice_s, p_layer):
    score_for_three_kind = 0
    dice = collections.Counter(dice_s)
    die_count_list = list(dice.keys())
    if 3 in dice.values():
        score_for_three_kind += 3*die_count_list[0]
    return score_for_three_kind


def four_of_a_kind(dice_s, p_layer):
    score_for_four_kind = 0
    dice = collections.Counter(dice_s)
    die_count_list = list(dice.keys())
    if 4 in dice.values():
        score_for_four_kind += 4 * die_count_list[0]
    return score_for_four_kind


def small_straight(dice_s, p_layer):
    score_for_small_straight = 0
    small_straight1 = [1, 2, 3, 4, 5]
    small_straight_count = 0
    for i in small_straight1:
        if i in dice_s:
            small_straight_count += 1
    if small_straight_count == 5:
        score_for_small_straight += 15
    return score_for_small_straight


def large_straight(dice_s, p_layer):
    score_for_large_straight = 0
    large_straight1 = [2, 3, 4, 5, 6]
    large_straight_count = 0
    for i in large_straight1:
        if i in dice_s:
            large_straight_count += 1
    if large_straight_count == 5:
        score_for_large_straight += 20
    return score_for_large_straight


def full_house(dice_s, p_layer):
    score_for_full_house = 0
    dice = collections.Counter(dice_s)
    die_list = list(dice.keys())
    die_list.sort(reverse=True)
    die_count = list(dice.values())
    if 3 in die_count:
        if 2 in die_count:
            score_for_full_house += ((3 * die_list[0]) + (2 * die_list[1]))
    return score_for_full_house


def high_sum(dice_s, p_layer):
    for _ in dice_s:
        return sum(dice_s)


def ya_tzy(dice_s, p_layer):
    score_for_yatzy = 0
    for _ in dice_s:
        if len(dice_s) == 5:
            if dice_s[0] == dice_s[1] == dice_s[2] == dice_s[3] == dice_s[4]:
                score_for_yatzy += 50
    return score_for_yatzy


num_players = int(input('Enter number of players who wants to play Yatzyy! game: '))
count1 = 1
while count1 <= num_players:
    player = (input('Enter player name: '))
    list_of_players.append(Player(player, scoring_pad.copy(), rolling(5)))
    count1 += 1
print("Welcome to Yatzy Game!")
shuffle(list_of_players)

for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for one's")
    dice_held = chan_ce()
    player[1]["Score for One's"] = num_ones(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Two's")
    dice_held = chan_ce()
    player[1]["Score for Two's"] = 2 * num_twos(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Three's")
    dice_held = chan_ce()
    player[1]["Score for Three's"] = 3 * num_threes(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Four's")
    dice_held = chan_ce()
    player[1]["Score for Four's"] = 4 * num_fours(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Five's")
    dice_held = chan_ce()
    player[1]["Score for Five's"] = 5 * num_fives(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Sixe's")
    dice_held = chan_ce()
    player[1]["Score for Sixe's"] = 6 * num_sixes(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Single Pair")
    dice_held = chan_ce()
    player[1]["Score for Single Pair"] = single_pair(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Double Pairs")
    dice_held = chan_ce()
    player[1]["Score for Double Pairs"] = double_pair(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Three of a Kind")
    dice_held = chan_ce()
    player[1]["Score for Three of dice_held Kind"] = three_of_a_kind(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Four of a Kind")
    dice_held = chan_ce()
    player[1]["Score for Four of dice_held Kind"] = four_of_a_kind(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Small Straight")
    dice_held = chan_ce()
    player[1]["Score for Small Straight"] = small_straight(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Large Straight")
    dice_held = chan_ce()
    player[1]["Score for Large Straight"] = large_straight(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Full House")
    dice_held = chan_ce()
    player[1]["Score for Full House"] = full_house(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for High Sum")
    dice_held = chan_ce()
    player[1]["Score for High Sum"] = high_sum(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")
for player in list_of_players:
    print(player[0], "your chance")
    print("This round is for Yatzyy")
    dice_held = chan_ce()
    player[1]["Score for Yatzyy"] = ya_tzy(dice_held, player)
    print(f"Player='{player[0]}', Scoring Pad={player[1]}, Dice held={dice_held}")

sorting_dict = {}
for player in list_of_players:
    sorting_dict[player[0]] = sum(player[1].values())

final = sorted(sorting_dict.items(), key=lambda s: s[1], reverse=True)
print("The first player is winner, the total score is also given besides \n", final)
