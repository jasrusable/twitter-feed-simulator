from src.tweets.lib import get_user_tweet_feed


def format_tweet(tweet):
    return '@{}: {}'.format(tweet['author'], tweet['body'])


def get_user_feed_output(user, followers, tweets):
    result = [user]
    user_feed = get_user_tweet_feed(user, followers, tweets)
    for tweet in user_feed:
        result.append(format_tweet(tweet))
    return result


def get_user_feeds_output(users, user_follower_mapping, tweets):
    result = []
    for user in users:
        followers = user_follower_mapping.get(user, [])
        result.extend(get_user_feed_output(user, followers, tweets))
    return result
