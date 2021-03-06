# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

# Your objective is to determine the length of the loop.

# For example in the following picture the tail's size is 3 and the loop size is 11.
# Image and video hosting by TinyPic

# # Use the `next' attribute to get the following node

# node.next

# Note: do NOT mutate the nodes!

def loop_size(node):
    dict, count = {}, 0
    while True:
        if node not in dict:
            dict[node] = count
            node = node.next
            count += 1
        else:
            return count - dict[node]