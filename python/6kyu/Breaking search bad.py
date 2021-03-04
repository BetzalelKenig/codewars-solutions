# The function must return the sequence of titles that match the string passed as an argument.

# titles = ['Rocky 1', 'Rocky 2', 'My Little Poney']
# search(titles, 'ock') --> ['Rocky 1', 'Rocky 2']
# But the function return some weird result and skip some of the matching results.

# Does the function have special movie taste?

# Let's figure out !

def search(titles, term):
    return list(filter(lambda title: term in title.lower(), titles))