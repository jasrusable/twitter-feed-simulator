from src import utils


TWEET_LINE_AUTHOR_BODY_SEPERATOR = '> '


def get_reasons_tweet_line_invalid(tweet_line):
    reasons = []
    if TWEET_LINE_AUTHOR_BODY_SEPERATOR not in tweet_line:
        reasons.append(f"Missing author/body seperator sequence: '{TWEET_LINE_AUTHOR_BODY_SEPERATOR}'.")
    return reasons or None


def get_reasons_tweet_invalid(tweet):
    reasons = []
    if len(tweet['body']) > 140:
        reasons.append(f'Tweet length exceeds 140 characters.')
    return reasons or None


def parse_tweet_line(tweet_line):
    """
    Parses a tweet line into tweet dictionary of author and body.
    Returns a dictionary of tweet author and body.
    """
    author, body = (
        tweet_line
        .split('> ')
    )
    return {
        'author': author,
        'body': body,
    }


# TODO: Use generator?
def parse_tweet_file(path):
    """
    Parses tweet file into a list of tweet dictionaries.
    Returns list of tweet dictionaries.
    """
    tweets_file = utils.read_text_file(path)
    return [parse_tweet_line(line.strip('\n')) for line in tweets_file]
