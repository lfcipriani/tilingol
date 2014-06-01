from twython import TwythonStreamer

class GoalStream(TwythonStreamer):

    def on_success(self, data):
        print(data)
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

