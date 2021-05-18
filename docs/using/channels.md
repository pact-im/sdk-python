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
from pact_im.schema.channels import TelegramPersonalCodeResponse
client = PactClient('SecretToken')

response: TelegramPersonalCodeResponse = client.channels.request_telegram_personal_code(
    company_id=1,
    channel_id=2
)

print(response.status)
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
