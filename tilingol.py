#!/usr/bin/env python

import sys
print len(sys.argv)

if len(sys.argv) < 5:
    print "Usage tilingol.py FREQUENCY_WINDOW MOVING_AVERAGE_WINDOW PEAK_THRESHOLD KEYWORDS [LANGS]"
    exit()

TRACK    = sys.argv[4]
LANGUAGE = sys.argv[5] if len(sys.argv) == 6 else ""

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
print "  LANGUAGE  = " + LANGUAGE
print sys.argv[1] + " - " + sys.argv[2] + " - " + sys.argv[3] + "\n"

stream = GoalStream(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.configure(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), True)
stream.statuses.filter(track=TRACK, language=LANGUAGE)
