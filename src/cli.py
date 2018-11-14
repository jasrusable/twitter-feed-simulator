import click

from src.tweets.persistence import parse_tweet_file, validate_tweet, validate_tweet_line
from src.tweets.presentation import get_user_feeds_output
from src.users.persistence import parse_follow_event_file
from src.users.lib import build_user_follower_mapping_for_multiple_follow_events, get_users_from_user_follower_mapping


@click.group()
@click.option('--tweets-file', help='Path for file containing tweets.')
@click.option('--user-mapping-file', help='Path for file containing user follower mapping.')
@click.pass_context
def cli(ctx, tweets_file, user_mapping_file):
    ctx.ensure_object(dict)
    ctx.obj['tweets_file'] = tweets_file
    ctx.obj['user_mapping_file'] = user_mapping_file


@click.command()
@click.pass_context
def print_users_feeds(ctx):
    user_mapping_file = ctx.obj['user_mapping_file']
    tweets_file = ctx.obj['tweets_file']
    follow_events = parse_follow_event_file(user_mapping_file)
    user_follower_mapping = build_user_follower_mapping_for_multiple_follow_events(follow_events)
    users = sorted(get_users_from_user_follower_mapping(user_follower_mapping))
    tweets = parse_tweet_file(tweets_file, line_cb=validate_tweet_line, tweet_cb=validate_tweet)
    output = get_user_feeds_output(users, user_follower_mapping, tweets)
    for line in output:
        print(line)


cli.add_command(print_users_feeds)


if __name__ == '__main__':
    cli()
