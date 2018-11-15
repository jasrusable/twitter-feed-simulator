from src.tweets.persistence import parse_tweet_file, validate_tweet, validate_tweet_line
from src.tweets.presentation import get_user_feeds_output
from src.users.persistence import (
    parse_follow_event_file,
    validate_follow_event,
    validate_follow_event_line,
)
from src.users.lib import (
    build_user_follower_mapping_for_multiple_follow_events,
    get_users_from_user_follower_mapping,
)


def get_users_feeds_from_follow_events_and_tweets_files(follow_events_file_path, tweets_file_path):
    follow_events = parse_follow_event_file(
        follow_events_file_path,
        line_cb=validate_follow_event_line,
        follow_event_cb=validate_follow_event,
    )
    user_follower_mapping = build_user_follower_mapping_for_multiple_follow_events(follow_events)
    users = sorted(get_users_from_user_follower_mapping(user_follower_mapping))
    tweets = parse_tweet_file(
        tweets_file_path,
        line_cb=validate_tweet_line,
        tweet_cb=validate_tweet,
    )
    output = get_user_feeds_output(users, user_follower_mapping, tweets)
    return output
