import random
import string
def randomString():
    letters = string.ascii_letters
    return "ARTC"+''.join(str(random.randint(1000,9999)))