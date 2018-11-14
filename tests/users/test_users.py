import unittest

from src.users.lib import (
    build_user_follower_mapping,
    build_user_follower_mapping_for_multiple_follow_events,
    get_user_list,
    )
from src.users.persistence import (
    parse_follow_event_file,
    parse_follow_event_line,
)


SAMPLE_FOLLOW_EVENT_DATA = [
    'Ward follows Alan',
    'Alan follows Martin',
    'Ward follows Martin, Alan',
]


SAMPLE_USER_FOLLOWER_MAPPING = {
    'Ward': ['Alan', 'Martin'],
    'Alan': ['Martin'],
}

SAMPLE_FOLLOW_EVENT_FILE_PATH = './sample_data/events.txt'


class TestUsers(unittest.TestCase):
    def test_parse_follow_event_line_parses_follow_event_line(self):
        parsed_follow_event = parse_follow_event_line(SAMPLE_FOLLOW_EVENT_DATA[0])
        assert parsed_follow_event['user'] == 'Ward'
        assert parsed_follow_event['action'] == 'follows'
        assert parsed_follow_event['followers'] == ['Alan']

    def test_parse_follow_event_line_parses_follow_event_line_with_multiple_followers(self):
        parsed_follow_event = parse_follow_event_line(SAMPLE_FOLLOW_EVENT_DATA[2])
        assert parsed_follow_event['user'] == 'Ward'
        assert parsed_follow_event['action'] == 'follows'
        assert parsed_follow_event['followers'] == ['Martin', 'Alan']

    def test_parse_follow_event_file_parses_file(self):
        parsed_follow_events = parse_follow_event_file(SAMPLE_FOLLOW_EVENT_FILE_PATH)
        assert len(parsed_follow_events) == 3
        assert parsed_follow_events[0]['user'] == 'Ward'
        assert parsed_follow_events[0]['action'] == 'follows'
        assert parsed_follow_events[0]['followers'] == ['Alan']

    def test_get_users_gets_users(self):
        users = sorted(get_user_list(SAMPLE_USER_FOLLOWER_MAPPING))
        expected_users = sorted(['Alan', 'Martin', 'Ward'])
        assert users == expected_users

    def test_build_user_follower_mapping_builds_mapping_with_follow_event(self):
        user_follower_mapping = build_user_follower_mapping(
            {'user': 'Alan', 'action': 'follows', 'followers': ['Ward']},
        )
        assert user_follower_mapping == {'Alan': ['Ward']}

    def test_build_user_follower_mapping_builds_mapping_with_multiple_followers(self):
        user_follower_mapping = build_user_follower_mapping(
            follow_event={'user': 'Alan', 'action': 'follows', 'followers': ['Ward', 'James']},
        )
        assert sorted(user_follower_mapping['Alan']) == sorted(['Ward', 'James'])

    def test_build_user_follower_mapping_builds_mapping_with_unfollow_event(self):
        user_follower_mapping = build_user_follower_mapping(
            follow_event={'user': 'Alan', 'action': 'unfollows', 'followers': ['James']},
            user_follower_mapping={'Alan': ['Ward', 'James']},
        )
        assert user_follower_mapping == {'Alan': ['Ward']}

    def test_build_user_follower_mapping_builds_mapping_with_many(self):
        user_follower_mapping = build_user_follower_mapping_for_multiple_follow_events(
            follow_events=[
                {'user': 'Alan', 'action': 'follows', 'followers': ['James']},
                {'user': 'Alan', 'action': 'follows', 'followers': ['John']},
                {'user': 'Alan', 'action': 'follows', 'followers': ['Sarah']},
                {'user': 'Alan', 'action': 'unfollows', 'followers': ['James']},
            ]
        )
        assert sorted(user_follower_mapping['Alan']) == sorted(['John', 'Sarah'])
