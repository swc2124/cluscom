import redis

from tweepy import OAuthHandler
from tweepy import Stream

from django.db import models

from .tweeper import Listener


class Words(models.Model):
    word = models.CharField(default="people", max_length=25)


class StreamMonitor(models.Model):

    # Basic settings
    name = models.CharField(default="Stream 1", max_length=100)

    # Status.
    stream_count = models.IntegerField(default=0, editable=False)
    stream_run = models.NullBooleanField(default=False)
    stream_status = models.BooleanField(default=False, editable=False)
    authenticated = models.BooleanField(default=False, editable=False)
    
    # Stream authorization.
    access_token = models.CharField(max_length=100, blank=True, null=True)
    access_token_secret = models.CharField(max_length=100, blank=True, null=True)
    consumer_key = models.CharField(max_length=100, blank=True, null=True)
    consumer_secret = models.CharField(max_length=100, blank=True, null=True)

    # Misc.
    listener = Listener
    auth = OAuthHandler
    stream = Stream

    # Words to track in stream.
    track_words = models.ManyToManyField(Words)

    # Redis setup.
    # TODO could pull from env.
    redis_errors = models.IntegerField(default=0, editable=False)
    allowed_redis_errors = models.IntegerField(default=0)
    redis_ip = models.GenericIPAddressField(default="127.0.0.1", protocol="IPv4")
    redis_port = models.PositiveIntegerField(default=6379)
    redis_db_id = models.SmallIntegerField(default=0)
    redis_db = redis.StrictRedis
    
    def set_redis(self):
        self.redis_db = self.redis_db(host=self.redis_ip, port=self.redis_port, db=self.redis_db_id)

    def set_authhandeler(self):

        self.auth(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

    def set_stream(self):
        self.set_authhandeler()
        self.stream(auth, self.listener(monitor=self))

    def start(self):
        self.set_stream()
        selfstream.filter(track=track_words)

    def __str__(self):
        return self.name.title()