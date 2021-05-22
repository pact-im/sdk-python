# Conversation

### Get All Conversations

```python
from pact_im import PactClient
client = PactClient('SecretToken')

conversations_result = client.conversations.get_conversations(
    company_id=1,
    per=100
)
for conversation in conversations_result.conversations:
    print(conversation.name)
```

### Create new conversation
This endpoint creates conversation in the company using whatsapp channel.

> If you have a `whatsapp_business` provider, use a different method to create conversation using a template

[Create first message for whatsapp business provider](../channels#how-to-write-first-message-to-whatsapp-business)
```python
from pact_im import PactClient
from pact_im.schema import Provider
client = PactClient('SecretToken')

response = client.conversations.create_conversation(
    company_id=1,
    provider=Provider.WhatsApp,
    phone='79250000001'
)

print(response.conversation.external_id)

```

##### Example Response
```json
{
   "status":"ok",
   "data":{
      "conversation":{
         "external_id":1,
         "name":"79250000001",
         "channel_id":1,
         "channel_type":"whatsapp",
         "created_at":"2017-11-11T10:17:10.655Z",
         "created_at_timestamp":1603119600,
         "avatar":"/avatars/original/missing.png",
         "sender_external_id":"79250000001",
         "meta":{

         }
      }
   }
}
```

### Get conversation details

```python
from pact_im import PactClient
client = PactClient('SecretToken')

response = client.conversations.get_detail(
    company_id=1,
    conversation_id=1
)

print(response.conversation.external_id)

```
##### Example Response
```json
{
   "status":"ok",
   "data":{
      "conversation":{
         "external_id":1,
         "name":"79250000001",
         "channel_id":1,
         "channel_type":"whatsapp",
         "created_at":"2017-11-11T10:17:10.655Z",
         "created_at_timestamp":1603119600,
         "avatar":"/avatars/original/missing.png",
         "sender_external_id":"79250000001",
         "meta":{

         }
      }
   }
}
```

### Update assignee for conversation
Update assignee for conversation

```python
from pact_im import PactClient
client = PactClient('SecretToken')

conversation_external_id = client.conversations.update_assignee(
    company_id=1,
    conversation_id=1,
    assignee_id=1
)

print(conversation_external_id)

```

### Upload attachment for message

```python
import os.path
from pact_im import PactClient

client = PactClient('SecretToken')

file_path = os.path.join('tmp', 'image.png')
file_url = 'https://en.wikipedia.org/wiki/Altai_Republic#/media/File:Katun.jpg'

# Local File
response_attach_external_id = client.attachment.upload_file(
    company_id=1,
    conversation_id=1,
    file=file_path
)

# File url
another_attach_external_id = client.attachment.upload_file(
    company_id=1,
    conversation_id=1,
    url=file_url
)
messages = client.messages.send_message(
    company_id=1,
    conversation_id=1,
    message='Some text',
    attachments=response_attach_external_id
    # or list(response_attach_external_id, another_attach_external_id)
)

```

> Whatsapp requires using this method with existing whatsapp business template