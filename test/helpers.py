"""
Handy helpers for testing the bot
"""
import time

from .conftest import TEST_CHANNEL_ID, TEST_USER_ID


# Slack Message Types
MESSAGE_TYPE_ACCOUNTS_CHANGED = "accounts_changed"
MESSAGE_TYPE_BOT_ADDED = "bot_added"
MESSAGE_TYPE_BOT_CHANGED = "bot_changed"
MESSAGE_TYPE_CHANNEL_ARCHIVE = "channel_archive"
MESSAGE_TYPE_CHANNEL_CREATED = "channel_created"
MESSAGE_TYPE_CHANNEL_DELETED = "channel_deleted"
MESSAGE_TYPE_CHANNEL_HISTORY_CHANGED = "channel_history_changed"
MESSAGE_TYPE_CHANNEL_JOINED = "channel_joined"
MESSAGE_TYPE_CHANNEL_LEFT = "channel_left"
MESSAGE_TYPE_CHANNEL_MARKED = "channel_marked"
MESSAGE_TYPE_CHANNEL_RENAME = "channel_rename"
MESSAGE_TYPE_CHANNEL_UNARCHIVE = "channel_unarchive"
MESSAGE_TYPE_COMMANDS_CHANGED = "commands_changed"
MESSAGE_TYPE_DND_UPDATED = "dnd_updated"
MESSAGE_TYPE_DND_UPDATED_USER = "dnd_updated_user"
MESSAGE_TYPE_EMAIL_DOMAIN_CHANGED = "email_domain_changed"
MESSAGE_TYPE_EMOJI_CHANGED = "emoji_changed"
MESSAGE_TYPE_FILE_CHANGE = "file_change"
MESSAGE_TYPE_FILE_COMMENT_ADDED = "file_comment_added"
MESSAGE_TYPE_FILE_COMMENT_DELETED = "file_comment_deleted"
MESSAGE_TYPE_FILE_COMMENT_EDITED = "file_comment_edited"
MESSAGE_TYPE_FILE_CREATED = "file_created"
MESSAGE_TYPE_FILE_DELETED = "file_deleted"
MESSAGE_TYPE_FILE_PUBLIC = "file_public"
MESSAGE_TYPE_FILE_SHARED = "file_shared"
MESSAGE_TYPE_FILE_UNSHARED = "file_unshared"
MESSAGE_TYPE_GOODBYE = "goodbye"
MESSAGE_TYPE_GROUP_ARCHIVE = "group_archive"
MESSAGE_TYPE_GROUP_CLOSE = "group_close"
MESSAGE_TYPE_GROUP_HISTORY_CHANGED = "group_history_changed"
MESSAGE_TYPE_GROUP_JOINED = "group_joined"
MESSAGE_TYPE_GROUP_LEFT = "group_left"
MESSAGE_TYPE_GROUP_MARKED = "group_marked"
MESSAGE_TYPE_GROUP_OPEN = "group_open"
MESSAGE_TYPE_GROUP_RENAME = "group_rename"
MESSAGE_TYPE_GROUP_UNARCHIVE = "group_unarchive"
MESSAGE_TYPE_HELLO = "hello"
MESSAGE_TYPE_IM_CLOSE = "im_close"
MESSAGE_TYPE_IM_CREATED = "im_created"
MESSAGE_TYPE_IM_HISTORY_CHANGED = "im_history_changed"
MESSAGE_TYPE_IM_MARKED = "im_marked"
MESSAGE_TYPE_IM_OPEN = "im_open"
MESSAGE_TYPE_MANUAL_PRESENCE_CHANGE = "manual_presence_change"
MESSAGE_TYPE_MEMBER_JOINED_CHANNEL = "member_joined_channel"
MESSAGE_TYPE_MEMBER_LEFT_CHANNEL = "member_left_channel"
MESSAGE_TYPE_MESSAGE = "message"
MESSAGE_TYPE_PIN_ADDED = "pin_added"
MESSAGE_TYPE_PIN_REMOVED = "pin_removed"
MESSAGE_TYPE_PREF_CHANGE = "pref_change"
MESSAGE_TYPE_PRESENCE_CHANGE = "presence_change"
MESSAGE_TYPE_PRESENCE_QUERY = "presence_query"
MESSAGE_TYPE_PRESENCE_SUB = "presence_sub"
MESSAGE_TYPE_REACTION_ADDED = "reaction_added"
MESSAGE_TYPE_REACTION_REMOVED = "reaction_removed"
MESSAGE_TYPE_RECONNECT_URL = "r"
MESSAGE_TYPE_STAR_ADDED = "star_added"
MESSAGE_TYPE_STAR_REMOVED = "star_removed"
MESSAGE_TYPE_SUBTEAM_CREATED = "subteam_created"
MESSAGE_TYPE_SUBTEAM_MEMBERS_CHANGED = "subteam_members_changed"
MESSAGE_TYPE_SUBTEAM_SELF_ADDED = "subteam_self_added"
MESSAGE_TYPE_SUBTEAM_SELF_REMOVED = "subteam_self_removed"
MESSAGE_TYPE_SUBTEAM_UPDATED = "subteam_updated"
MESSAGE_TYPE_TEAM_DOMAIN_CHANGE = "team_domain_change"
MESSAGE_TYPE_TEAM_JOIN = "team_join"
MESSAGE_TYPE_TEAM_MIGRATION_STARTED = "team_migration_started"
MESSAGE_TYPE_TEAM_PLAN_CHANGE = "team_plan_change"
MESSAGE_TYPE_TEAM_PREF_CHANGE = "team_pref_change"
MESSAGE_TYPE_TEAM_PROFILE_CHANGE = "team_profile_change"
MESSAGE_TYPE_TEAM_PROFILE_DELETE = "team_profile_delete"
MESSAGE_TYPE_TEAM_PROFILE_REORDER = "team_profile_reorder"
MESSAGE_TYPE_TEAM_RENAME = "team_rename"
MESSAGE_TYPE_USER_CHANGE = "user_change"
MESSAGE_TYPE_USER_TYPING = "user_typing"


def generate_event_object(event_type, **additional_data):
    data = additional_data.copy()
    data[u'type'] = event_type
    return data


def generate_message_object(text, channel=TEST_CHANNEL_ID, user=TEST_USER_ID, ts=None):
    """
    Create a Slack message object
    Timestamp will default to now
    """
    ts = ts or str(time.time())
    return generate_event_object(
        event_type=MESSAGE_TYPE_MESSAGE,
        channel=channel,
        user=user,
        text=text,
        ts=ts,
    )
