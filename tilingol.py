#!/usr/bin/env python

import sys

if len(sys.argv) != 4:
    print "Usage tilingol.py FREQUENCY_WINDOW MOVING_AVERAGE_WINDOW PEAK_THRESHOLD"
    exit()

# configure parameters here
TRACK    = 'gol,goal,gooool,goaaal,golo'#'tocaosino'
FOLLOW = ''
#FOLLOW   = '158487331,932429090,331975075,973277052,333152159,309340221,25073959,344801362,201352564,2424510447,473340249,575565118,307807956,106444705,1704998570,142204481,2178230389,586950556'
LANGUAGE = ''

from goalstream import GoalStream

txtfile = open("config/credentials.txt", "r")
credentials = txtfile.readlines()
txtfile.close()

APP_KEY = credentials[0].strip()
APP_SECRET = credentials[1].strip()
OAUTH_TOKEN = credentials[2].strip()
OAUTH_TOKEN_SECRET = credentials[3].strip()

print "Howdy! I'm tracking:"
print "  TRACK     = " + TRACK
print "  FOLLOW    = " + FOLLOW
print "  LANGUAGE  = " + LANGUAGE
print sys.argv[1] + " - " + sys.argv[2] + " - " + sys.argv[3] + "\n"

stream = GoalStream(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.configure(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), True)
stream.statuses.filter(track=TRACK, language=LANGUAGE)
