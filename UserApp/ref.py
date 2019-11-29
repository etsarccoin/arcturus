import random
import string
def randomString():
    letters = string.ascii_letters
    return "ARTC"+''.join(random.choice(letters) for i in range(5))