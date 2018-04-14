from tweepy.streaming import StreamListener


class Listener(StreamListener):
    """docstring for Listener"""
    def __init__(self, monitor):
        super(Listener, self).__init__()
        self.monitor = monitor

    def on_data(self):
        self.monitor.stream_count += 1
