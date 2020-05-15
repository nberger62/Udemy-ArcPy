def rand_buffer_size(min, max):
    from random import randint
    randInt = randint(min, max)
    bufSizeKm = randInt * 100
    return "{0} Kilometers".format(bufSizeKm)

# expression - rand_buffer_size(%Min%,%Max%)

# data type - Linear Unit
# Test data set Min to 1 and Max to 5
