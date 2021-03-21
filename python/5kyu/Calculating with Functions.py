# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(op=None):
    if not op:
        return 0
    return eval('0'+op)


def one(op=None):
    if not op:
        return 1
    return eval('1'+op)


def two(op=None):
    if not op:
        return 2
    return eval('2'+op)


def three(op=None):
    if not op:
        return 3
    return eval('3'+op)


def four(op=None):
    if not op:
        return 4
    return eval('4'+op)


def five(op=None):
    if not op:
        return 5
    return eval('5'+op)


def six(op=None):
    if not op:
        return 6
    return eval('6'+op)


def seven(op=None):
    if not op:
        return 7
    return eval('7'+op)


def eight(op=None):
    if not op:
        return 8
    return eval('8'+op)


def nine(op=None):
    if not op:
        return 9
    return eval('9'+op)


def plus(n):
    return f'+{n}'


def minus(n):
    return f'-{n}'


def times(n):
    return f'*{n}'


def divided_by(n):
    return f'//{n}'
