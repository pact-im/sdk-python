# Channels

```python
from pact_im import PactClient

TOKEN = 'SecretToken'

client = PactClient(TOKEN)
```

### Get channels
```python
from pact_im import PactClient
TOKEN = 'SecretToken'
client = PactClient(TOKEN)
response = client.channels.get_channels(company_id=1)
for channel in response.channels:
    print(channel.external_id, channel.provider)
```