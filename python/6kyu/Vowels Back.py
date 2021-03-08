# You need to play around with the provided string (s).

# Move consonants forward 9 places through the alphabet. If they pass 'z', start again at 'a'.

# Move vowels back 5 places through the alphabet. If they pass 'a', start again at 'z'. For our Polish friends this kata does not count 'y' as a vowel.

# Exceptions:

# If the character is 'c' or 'o', move it back 1 place. For 'd' move it back 3, and for 'e', move it back 4.

# If a moved letter becomes 'c', 'o', 'd' or 'e', revert it back to it's original value.

# Provided string will always be lower case, won't be empty and will have no special characters.

import string
def vowel_back(st):
    res, c = '', ''
    str = string.ascii_lowercase
    for i in st:
        if i in 'aiu':
            c = str[(ord(i)-102)%26]
        elif i in 'co':
            c = str[(ord(i)-98)%26]
        elif i == 'd':
            c = str[(ord(i)-100)%26]
        elif i == 'e':
            c = str[(ord(i)-101)%26]
        else:
            c = str[(ord(i)-88)%26]
        res += c if c not in 'code' else i        
    return res