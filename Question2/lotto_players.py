"""
file:           lotto_players.py
created:        07/10/2021 09:53
author:         ciaran mcdevitt
version:        v1.0.0
licensing:      (c) 2021 Ciaran McDevitt, LYIT
                available under the GNU Public License (GPL)
description:
credits:

"""
import random
from collections import OrderedDict

if __name__ == '__main__':
    '''
    Main method to display the 
        1) Intersection, 
        2) Unique Numbers,
        3) Most common numbers,
        4) Occurrences of lottery player with the same number in lottery 1 and lottery 2 

    Parameters:
    :argument1 (list): week_1_namelist (list of names for week 1 lottery)
    :argument2 (list): week_2_namelist (list of names for week 2 lottery)
    :argument3 (list): week_1_nums (empty list to hold randomly generated numbers for week 1 lottery players) 
    :argument4 (list): week_2_nums (empty list to hold randomly generated numbers for week 2 lottery players)
    '''

    week_1_namelist = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
    week_2_namelist = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    week_1_nums = []
    week_2_nums = []

    for name in week_1_namelist:
        lotto_num = random.randint(1, 20)
        week_1_nums.append(lotto_num)

    for name in week_2_namelist:
        lotto_num = random.randint(1, 20)
        week_2_nums.append(lotto_num)

    week_1_lotto = dict((list(zip(week_1_namelist, week_1_nums))))
    week_2_lotto = dict((list(zip(week_2_namelist, week_2_nums))))

    print("\nweek_1_lotto: {}".format(week_1_lotto))
    print("week_2_lotto: {}".format(week_2_lotto))

    # 1. intersection
    # ---------------------------------------------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("1. intersection\n")
    intersection = [name for name in week_1_namelist if name in week_2_namelist]
    print(intersection)

    # 2. unique members
    # ---------------------------------------------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("2. unique numbers\n")
    unique_numbers = set(week_1_nums + week_2_nums)
    print(unique_numbers)

    # 3. most common numbers
    # ---------------------------------------------------------------------------------------------------------
    print("\n" + "-"*80)
    print("3. most common numbers\n")
    occurrences = {}
    all_numbers = week_1_nums + week_2_nums
    print(all_numbers)
    for num in unique_numbers:
        count = all_numbers.count(num)
        occurrences |= {num: count}

    sorted_occurrences = OrderedDict(sorted(occurrences.items(), reverse=True, key=lambda t: t[1]))

    for key in sorted_occurrences:
        print(f"{key} appears {sorted_occurrences[key]} times")

    # 4. user has same number in multiple lotteries
    # ---------------------------------------------------------------------------------------------------------
    print("\n" + "-"*80)
    print("4. same number multiple times (matches don't always occur, run a few times to see a match)\n")
    print(f"week_1_lotto: {week_1_lotto}")
    print(f"week_2_lotto: {week_2_lotto}")

    members_on_two_lists = []
    for key in week_1_lotto.keys():
        if key in week_2_lotto.keys():
            members_on_two_lists.append(key)

    for name in members_on_two_lists:
        if week_1_lotto[name] == week_2_lotto[name]:
            print(f"\nMatch:\n{name}'s has: {week_1_lotto[name]} in week_1_lotto "
                  f"and: {week_2_lotto[name]} in week_2_lotto")

