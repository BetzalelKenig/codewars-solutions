# Variation of this nice kata, the war has expanded and become dirtier and meaner; both even and odd numbers will fight with their pointy 1s. And negative integers are coming into play as well, with, ça va sans dire, a negative contribution (think of them as spies or saboteurs).

# A number's strength is determined by the number of set bits (1s) in its binary representation. Negative integers work against their own side so their strength is negative. For example -5 = -101 has strength -2 and +5 = +101 has strength +2.

# The side with the largest cumulated strength wins.

# Again, three possible outcomes: odds win, evens win and tie.

# Examples:

# bits_war([1,5,12]) => "odds win" #1+101 vs 1100, 3 vs 2
# bits_war([7,-3,20]) => "evens win" #111-11 vs 10100, 3-2 vs 2
# bits_war([7,-3,-2,6]) => "tie" #111-11 vs -1+110, 3-2 vs -1+2

def bits_war(numbers):
    odds = ["{0:b}".format(i).count('1') if i > 0 else "{0:b}".format(i).count('1') * -1 for i in numbers if i % 2 == 1]
    evens = ["{0:b}".format(i).count('1') if i > 0 else "{0:b}".format(i).count('1') * -1 for i in numbers if i % 2 == 0]
    if sum(odds) < sum(evens): return 'evens win'
    if sum(odds) > sum(evens): return 'odds win'
    return 'tie'