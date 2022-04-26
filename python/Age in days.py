# Did you ever want to know how many days old are you? Complete the function which returns your age in days. The birthday is given in the following order: year, month, day.

# For example if today is 30 November 2015 then

# ageInDays(2015, 11, 1) returns "You are 29 days old"

# The birthday is expected to be in the past.

# Suggestions on how to improve the kata are welcome!

from datetime import date

def age_in_days(year, month, day):
    delta = date(year, month, day) - date.today()
    return f'You are {delta.days*-1} days old'