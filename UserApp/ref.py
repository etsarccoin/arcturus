import random
import string
def randomString():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(6))