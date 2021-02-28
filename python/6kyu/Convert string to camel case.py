# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples

# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

import re
def to_camel_case(t):
    return t if not t else t[0]+''.join([w.title() for w in re.split(r'[_-]', t)])[1:]
