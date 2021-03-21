# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    if not names:
        return ''
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        return f'{names[0]["name"]} & {names[1]["name"]}'
    return ''.join([name['name'] + ', ' if i != len(names)-2 else name['name'] + ' & ' for i, name in enumerate(names)])[:-2]
