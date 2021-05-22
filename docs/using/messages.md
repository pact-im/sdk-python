# Messages

Each message belongs to conversation. Message fields:

* id (Integer)
* channel_type (String) – whatsapp, instagram, etc..
* message (String) – message body
* income (Boolean) – whether message is income or outcome

### Get conversation messages

```python
from pact_im import PactClient
client = PactClient('SecretToken')

messages_response = client.messages.get_messages(
    company_id=1,
    conversation_id=1
)

for message in messages_response.messages:
    print(message.external_id)

```

### Send message
This endpoint delivers message to the client under specified conversation.

There are two delivery modes: _synchronous_ and _asyncronous_. If `message_id` field in response is null or empty – it means asyncronous delivery.

You’ll receive a webhook with the delivery status if delivery is async.

You can check operation result manually here: [Jobs](../jobs)

```python
from pact_im import PactClient
from pact_im.schema.messages import MessageResponse
client = PactClient('SecretToken')

message_response: MessageResponse = client.messages.send_message(
    company_id=1,
    conversation_id=1,
    message='Hello'
)

print(message_response.message_id)

```
**Important**: Some messengers support only text or only attachment in one message. For example, whatsapp allows to attach a caption for an image but not allows to attach a caption to a PDF document. Multiple attachments are allowed only for vkontakte