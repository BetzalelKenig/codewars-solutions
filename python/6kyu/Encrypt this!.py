# Acknowledgments:
# I thank yvonne-liu for the idea and for the example tests :)

# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

encrypt_this = lambda t:' '.join([str(ord(i[0]))+i[2:][-1:]+i[2:len(i)-1]+i[1:2]for i in t.split()])