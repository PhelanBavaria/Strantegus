import string
import random


UPPDIG = string.ascii_uppercase + string.digits
def id_generator(size=6, chars=UPPDIG):
    return ''.join(random.choice(chars) for _ in range(size))