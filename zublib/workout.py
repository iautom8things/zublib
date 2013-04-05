from itertools import product
from random import shuffle
from time import time
from datetime import datetime
from collections import Counter
from os import path
import sqlite3

homedir = path.expanduser("~")
dbname = "zworkout"
dbdir = path.join(homedir,"." + dbname)
dbfile = path.join(dbdir,dbname + '.db')
excercises = [ "sit-ups", "jumping jacks", "push-ups", "burpees"]

def card_deck ( excercises = excercises ):
    deck = [ x for x in product(excercises,range(1,14)) ]
    shuffle(deck)
    msg = """Type out 'record' if you wish to record.
    Otherwise, this session will not be recorded ...
    """
    record = raw_input(msg) == 'record'
    times = Counter()
    counts = Counter()

    start = time()
    for excercise, count in deck:
        raw_input("Now do {} {}!".format(count,excercise))
        now = time()
        elapsed, start = now - start, now
        times[excercise] += elapsed
        counts[excercise] += count
        print("Time: {}".format(elapsed))

    msg = "Great work!  Here's your stats:\nTimes:{}\nCounts{}"
    print(msg.format(times,counts))
    if record:
        print("Recording to db @ {}".format(dbfile))
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        t = datetime.fromtimestamp(now)
        completed = [ (t,exc,times[exc],counts[exc]) for exc in excercises]
        c.executemany('INSERT INTO workouts VALUES (?,?,?,?);',completed)
        conn.commit()
        conn.close()
