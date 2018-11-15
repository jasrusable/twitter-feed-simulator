from collections import namedtuple


Tweet = namedtuple('Tweet', ['author', 'body'])


# TODO: Use generator?
# TODO: Rename to filter_tweets?
def get_user_tweet_feed(user, followers, tweets):
    """
    Filter tweets by author and their followers.
    Returns filtered list of tweets.
    """
    feed = []
    for tweet in tweets:
        author = tweet['author']
        if author == user or author in followers:
            feed.append(tweet)
    return feed
