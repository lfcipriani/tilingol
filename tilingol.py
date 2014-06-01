from goalstream import GoalStream

txtfile = open("config/credentials.txt", "r")
credentials = txtfile.readlines()
txtfile.close()

APP_KEY = credentials[0].strip()
APP_SECRET = credentials[1].strip()
OAUTH_TOKEN = credentials[2].strip()
OAUTH_TOKEN_SECRET = credentials[3].strip()

stream = GoalStream(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.configure(3,5)
stream.statuses.filter(track='gol', language="pt")
