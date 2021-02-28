# Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

# formatWords(['ninja', 'samurai', 'ronin']) // should return "ninja, samurai and ronin"
# formatWords(['ninja', '', 'ronin']) // should return "ninja and ronin"
# formatWords([]) // should return ""

def format_words(words):   
    if words == [] or words == None: return ''
    words = [w for w in words if w != '']
    if words == [] or words == None: return ''
    if len(words) == 1: return words[0]
    if len(words) == 2: return ' and '.join(words)
    for i in range(len(words)-2):
        words[i] += ','
    words.insert(-1, 'and')
    return ' '.join(words)