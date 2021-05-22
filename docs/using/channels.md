# Channels


### Get channels

```python
from pact_im import PactClient
client = PactClient('SecretToken')

response = client.channels.get_channels(company_id=1)
for channel in response.channels:
    print(channel.external_id, channel.provider)
```

### Create new channel

> You can connect only one channel per one company for each provider. Contact with support if you want to use more than one channel


```python
import datetime

from pact_im import PactClient
from pact_im.schema import Provider

client = PactClient('SecretToken')

external_id = client.channels.create_channel_unified(
    company_id=1,
    provider=Provider.WhatsApp
)

external_id_another = client.channels.create_channel_whatsapp(
    company_id=2,
    sync_messages_from=datetime.datetime(2021, 1, 1)
)
```

### Update channel

For instagram channel

```python
from pact_im import PactClient
client = PactClient('SecretToken')

external_id = client.channels.update_channel_instagram(
    company_id=1,
    channel_id=1,
    login='some_login',
    password='some_password'
)

```

For facebook/vkontakte/vkontakte_direct/telegram/viber channels

```python
from pact_im import PactClient
client = PactClient('SecretToken')

# For instagram channel
external_id = client.channels.update_channel_token(
    company_id=1,
    channel_id=1,
    token='some_token'
)

```

### Delete channel

```python
from pact_im import PactClient
client = PactClient('SecretToken')

response = client.channels.delete_channel(
    company_id=1,
    channel_id=2
)

print(response.is_success())

```


## Telegram Personal
### Request code

```python
from pact_im import PactClient
client = PactClient('SecretToken')

response: dict = client.channels.request_telegram_personal_code(
    company_id=1,
    channel_id=2
)

print(response)
```

###### Example Response
```json
{
  "code_length": 6,
  "code_type": "app",
  "expires_in": 60,
  "next_type": "app",
  "session_id": 1337,
  "status": "ok"
}
```

### Confirm Code
```python
from pact_im import PactClient
from pact_im.schema import ConfirmationType

client = PactClient('SecretToken')

response: dict = client.channels.confirm_telegram_personal_code(
    company_id=1,
    channel_id=1,
    code='some_code',
    confirmation_type=ConfirmationType.CODE
)

print(response)
```
###### Example Response
```json
{
  "result": "ok",
  "state": "enabled"
}
```

## Instagram
### Request code
```python
from pact_im import PactClient
client = PactClient('SecretToken')

response: dict = client.channels.request_instagram_code(
    company_id=1,
    channel_id=2,
    challenge_variant=0
)

print(response)
```
###### Example Response
```json
{
  "result": "ok"
}
```

### Request two factor SMS authentication code
```python
from pact_im import PactClient
client = PactClient('SecretToken')

response: dict = client.channels.request_instagram_two_factor_code(
    company_id=1,
    channel_id=2
)

print(response)
```
###### Example Response
```json
{
  "result": "ok"
}
```

### Confirm code
```python
from pact_im import PactClient
client = PactClient('SecretToken')

response: dict = client.channels.confirm_instagram_code(
    company_id=1,
    channel_id=2,
    confirmation_code='some_code'
)

print(response)
```
###### Example Response
```json
{
  "result": "ok"
}
```

### Confirm two factor authentication code
```python
from pact_im import PactClient
client = PactClient('SecretToken')

response: dict = client.channels.confirm_instagram_two_factor_code(
    company_id=1,
    channel_id=2,
    confirmation_code='some_code',
    confirmation_variant=1
)

print(response)
```
###### Example Response
```json
{
  "result": "ok"
}
```

## How to write first message to Whatsapp
>  Whatsapp requires using this method to write the first message.

```python
from pact_im import PactClient
from pact_im.schema.messages import MessageResponse
client = PactClient('SecretToken')

response: MessageResponse = client.channels.send_first_whatsapp_message(
    company_id=1,
    channel_id=2,
    phone='79999999999',
    message='Some text message'
)

print(response)
```

## How to write first message to Whatsapp Business
This endpoint provides an ability to create conversation with a client in whatsapp channel. When you execute this request we will add a job for delivery. We will send webhook when the operation is complete or failed.

You can also poll delivery status here: [Jobs](../jobs)

> Whatsapp business requires using this method to write the first message.

```python
from pact_im import PactClient
from pact_im.schema.messages import MessageResponse
client = PactClient('SecretToken')

response: MessageResponse = client.channels.send_whatsapp_template_message(
    company_id=1,
    channel_id=2,
    phone='79999999999',
    template_id=111,
    template_language='ru'
)

print(response)
```