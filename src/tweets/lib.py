

# TODO: Use generator?
# TODO: Rename to filter_tweets?
def get_user_tweet_feed(user, followers, tweets):
    """
    Filter tweets on author followers.
    Returns filtered list of tweets.
    """
    feed = []
    for tweet in tweets:
        if tweet['author'] in followers or tweet['author'] == user:
            feed.append(tweet)
    return feed
