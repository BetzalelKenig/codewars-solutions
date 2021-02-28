# mispelled('versed', 'xersed') # returns True
# mispelled('versed', 'applb') # returns False
# mispelled('versed', 'v5rsed') # returns True
# mispelled('1versed', 'versed') # returns True

# It checks if the word2 differs from word1 by only one character.

# This can include an extra char at the end or the beginning of either of words.

# In the tests that expect true, the mispelled word will always differ only by one character.

# The only exception to the rule above is if one string is empty, in that case, it should return false (if both strings are empty, then return true).

def mispelled(word1, word2):
    if not word1 and not word2:
        return True
    if not word1 or not word2:
        return False
    if abs(len(word1) - len(word2)) > 1:
        return False
    if word1[1:] == word2 or word2[1:] == word1:
        return True
    dif = 0
    for i in range(min(len(word1), len(word2))):
        if word1[i] is not word2[i]:
            dif += 1
            if dif > 1:
                return False
    return True
