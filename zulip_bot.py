#!/usr/bin/env python3
from zulip import Client

# Pass the path to your zuliprc file here:
client = Client(config_file="zuliprc_bot")

# Send Message:
def send_msg(sending_user, msg_topic, msg_text):

    # Send a stream message:
    request = {
        "type" : "stream",    # private & stream
        "to" : sending_user,  # recipient
        "topic" : msg_topic,  # chat topic work only on type (stream)
        "content" : msg_text, # message text
    }

    # Send Message:
    result = client.send_message(request)

    # Result:
    print(result)


# Get History Chat:
def get_msg(chat):

    # Get the 100 last messages sent by "iago@zulip.com" to the stream "Verona"
    request: Dict[str, Any] = {
        "anchor" : "newest",
        "num_before" : 100,
        "num_after" : 0,
        "narrow" : [
            {"operator": "stream", "operand": chat},
        ],
    }

    # Getting History Chat:
    result = client.get_messages(request)

    print(result)


# Edit Message:
def edit_msg(message_id):

    # Edit Message Parametrs:
    request = {
        "message_id": message_id,
        "content": "New content",
    }

    # Editing Message:
    result = client.update_message(request)

    # Result:
    print(result)


# Delete message:
def del_msg(message_id):

    # Deleting Message With ID Message:
    result = client.delete_message(message_id)

    # Result:
    print(result)


# Render Message:
def render_msg():

    # Render a Message:
    request = {
        "content": "**foo**",
    }

    # Rendering Message to HTML:
    result = client.render_message(request)

    # Result:
    print(result)
