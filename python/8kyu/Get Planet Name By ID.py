# The function is not returning the correct values. Can you figure out why?

# get_planet_name(3) # should return 'Earth'


def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]