def get_user_tweet_feed(user, followers, tweets):
    feed = []
    for tweet in tweets:
        if tweet['author'] in followers or tweet['author'] == user:
            feed.append(tweet)
    return feed
