# ZulipBot-Python

<div id="header" align="left">
  <img src="https://play-lh.googleusercontent.com/JEo4Q5Ed3TIJRxL8A-moTh0HoYF74Hmg4WFISopAach2CjcpgSiTDQXU2d6JnxNz0g" width="100"/>
</div>

Bot for the messanger Zulip.

> <a href="https://zulip.com/api/">Link</a> <strong><=</strong> This link to the official documentation API

<br/>

### <strong>Functin list:</strong>
* Send Message
* Getting Message
* Delete the Message
* Edit the Message
* Render Message text to HTML

<br/>

## Start

<div id="header" align="left">
  <img src="https://preview.redd.it/hewrzv1fi8k81.jpg?width=640&crop=smart&auto=webp&s=5ee82bdd668b2b54eab3a842b5960ea570960690" width="100"/>
</div>


Download file *** <strong>zilprc</strong> ***. This file will store all the data for managing the bot.

### Example:
<pre>
[api]
email=email@zulip.com
key=Udsdk32JKJKmdsksdjfkjkUksfI9
site=https://zulip.com
</pre>

<br/>

# Function:

### Send Message
<pre>
send_msg(sending_chat, msg_topic, msg_text)
</pre>

> Gets 3 parametrs:
* sending_chat => Message recipient
* msg_topic => Chat topic 
* msg_text => Message text

<br/>

### Get Message
<pre>
get_msg(chat)
</pre>

> Gets 1 parametrs:
* chat => Name want chat from which you will receive

<br/>

### Edit Message 
<pre>
edit_msg(message_id)
</pre>

> Gets 1 parametrs:
* message_id => ID message which need to edit

<br/>

### Delete Message 
<pre>
del_msg(message_id)
</pre>

> Gets 1 parametrs:
* message_id => ID message which need to delete

<br/>

### Render Message to HTML 
<pre>
render_msg(msg_text)
</pre>

> Gets 1 parametrs:
* msg_text => The text of the message to be rendered
