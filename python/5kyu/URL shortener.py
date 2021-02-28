# ========not pass maybe performence============

# Background Information
# When do we use an URL shortener?

# In your PC life you have probably seen URLs like this before:

#     https://bit.ly/3kiMhkU

# If we want to share a URL we sometimes have the problem that it is way too long, for example this URL:

#     https://www.google.com/search?q=codewars&tbm=isch&ved=2ahUKEwjGuLOJjvjsAhXNkKQKHdYdDhUQ2-cCegQIABAA&oq=codewars&gs_lcp=CgNpbWcQAzICCAAyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBggAEAUQHlDADlibD2CjEGgAcAB4AIABXIgBuAGSAQEymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=RJmqX8aGHM2hkgXWu7ioAQ&bih=1099&biw=1920#imgrc=Cq0ZYnAGP79ddM

# In such cases a URL shortener is very useful.
# How does it work?

# The URL shortener is given a long URL, which is then converted into a shorter one. Both URLs are stored in a database. It is important that each long URL is assigned a unique short URL.

# If a user then calls up the short URL, the database is checked to see which long URL belongs to this short URL and you are redirected to the original/long URL.

# Important Note: Some URLs like www.google.com are used very often, it can happen that two users want to shorten the same URL, so you have to check if this URL has been shortened before to save memory in your database.
# Task
# URL Shortener

# Write a function url_shortener(long_url), which receives a long URL and returns an URL consisting only of lowercase letters (and one dot and one slash).

# Every short URL has to include short.ly/ and must not be longer than 13.

# Note: short.ly/ is not a valid short URL.
# Redirect URL

# Write a function url_redirector(short_url), which receives the shortened URL and returns the corresponding long URL.
# Performance

# There are 300_000 random tests.

# You don't need a complicated algorithm to solve this kata, but iterating each time through the whole database to check if a URL was used before, won't pass.

# GOOD LUCK AND HAVE FUN!

import itertools as it

chars = 'abcdefghijklmnopqrstuvwxyz'
keys = it.product(chars, repeat=1)
for length in range(2, 5): # only do lengths of 1 + 2
    keys = it.chain(keys, it.product(chars, repeat=length))
data = {}

def url_shortener(long_url):
    
    if long_url in data.keys():
        return data[long_url]
    data[long_url] = 'short.ly/'+ ''.join(next(keys))
    return data[long_url]

def url_redirector(short_url):
    return list(data.keys())[list(data.values()).index(short_url)]
   