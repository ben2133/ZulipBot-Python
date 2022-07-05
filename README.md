# ZulipBot-Python

Bot for the messanger Zulip.

> <a href="https://zulip.com/api/">Link</a> <strong><=</strong> This link to the official documentation API

### <strong>Functin:</strong>
* Send Message
* Getting Message
* Delete the Message
* Edit the Message
* Render Message text to HTML

## Start

Download file *** <strong>zilprc</strong> ***. This file will store all the data for managing the bot.

### Example:
<pre>
[api]
email=email@zulip.com
key=Udsdk32JKJKmdsksdjfkjkUksfI9
site=https://zulip.com
</pre>

# Function:

### Send Message
<pre>
send_msg(sending_chat, msg_topic, msg_text)
</pre>

> Gets 3 parametrs:
* sending_chat => Message recipient
* msg_topic => Chat topic 
* msg_text => Message text


### Get Message
<pre>
get_msg(chat)
</pre>

> Gets 1 parametrs:
* chat => Name want chat from which you will receive


### Edit Message 
<pre>
edit_msg(message_id)
</pre>

> Gets 1 parametrs:
* message_id => ID message which need to edit

### Delete Message 
<pre>
del_msg(message_id)
</pre>

> Gets 1 parametrs:
* message_id => ID message which need to delete

### Render Message to HTML 
<pre>
render_msg(msg_text)
</pre>

> Gets 1 parametrs:
* msg_text => The text of the message to be rendered
