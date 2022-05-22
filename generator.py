import random
from quotes import *

def generate():
    bq = random.choice(bob_quotes)
    hq = random.choice(henri_quotes)
    mq = random.choice(misc_quotes)
    quotes = [bq, hq, mq]
    random.shuffle(quotes)
    print(*quotes)

generate()