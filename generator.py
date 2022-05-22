import random
from quotes import *
import time

def generate():
    bq = random.choice(bob_quotes)
    hq = random.choice(henri_quotes)
    mq = random.choice(misc_quotes)
    quotes = [bq, hq, mq]
    random.shuffle(quotes)
    print(*quotes)

generate()

time.sleep(5)