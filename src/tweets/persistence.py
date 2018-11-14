from src import utils


SPLIT = '> '


def validate_tweet_line(tweet_line):
    reasons_invalid = []
    if SPLIT not in tweet_line:
        reasons_invalid.append(f'Missing author/body seperator sequence: {SPLIT}.')
    return reasons_invalid or None


def parse_tweet_line(tweet_line):
    author, body = (
        tweet_line
        .split('> ')
    )
    return {
        'author': author,
        'body': body,
    }


# TODO: Use generator experssion?
def parse_tweet_file(path):
    tweets_file = utils.read_text_file(path)
    return [parse_tweet_line(line.strip('\n')) for line in tweets_file]
