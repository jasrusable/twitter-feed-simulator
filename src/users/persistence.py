from src import utils
from src.users.enums import Action


def parse_follow_event_line(follow_event_line):
    user, action, _followers = (
        follow_event_line
        .replace(', ', ',')
        .split(' ')
    )
    assert action in [action.value for action in Action]
    followers = _followers.split(',')
    return {
        'user': user,
        'action': action,
        'followers': followers,
    }


def parse_follow_event_file(path):
    follow_events_file = utils.read_text_file(path)
    return [parse_follow_event_line(line.strip('\n')) for line in follow_events_file]
