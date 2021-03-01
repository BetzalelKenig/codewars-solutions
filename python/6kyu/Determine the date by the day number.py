# What date corresponds to the nth day of the year?
# The answer depends on whether the year is a leap year or not.

# Write a function that will help you determine the date if you know the number of the day in the year, as well as whether the year is a leap year or not.
# The function accepts the day number and a boolean value isLeap as arguments, and returns the corresponding date of the year as a string "Month, day".
# Only valid combinations of a day number and isLeap will be tested.
# Examples:

# get_day(41, False)   =>  "February, 10"  #  41st day of non-leap year is February, 10
# get_day(60, False)   =>  "March, 1"      #  60th day of non-leap year is March, 1
# get_day(60, True)    =>  "February, 29"  #  60th day of leap year is February, 29
# get_day(365, False)  =>  "December, 31"  #  365th day of non-leap year is December, 31
# get_day(366, True)   =>  "December, 31"  #  365th day of leap year is December, 31

def get_day(day, is_leap): 
    month = {
        'January': 31,
        'February':28,
        'March':31,
        'April':30,
        'May':31,
        'June':30,
        'July':31,
        'August':31,
        'September':30,
        'October':31,
        'November':30,
        'December':31
    }
    if is_leap:
        month['February'] = 29
    sum = 0
    for (k,v) in month.items():     
        if sum+v >= day:
            return f'{k}, {abs(day-sum)}'
        sum+=v
            