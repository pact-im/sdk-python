# Getting started

### 5 easy steps for integration

1. [Signup here](https://app.pact.im/signup)
1. Get your API token in [account settings](https://app.pact.im/account)
1. Connect WhatsApp or Instagram or anything [here](https://app.pact.im/project_settings)
1. Setup webhooks [using this doc](https://pact-im.github.io/api-doc/#webhooks)
1. Try to [send or receive message](https://pact-im.github.io/api-doc/#conversations)

### Installation

```shell
pip install -U pact_im
```

```python
from pact_im import PactClient
TOKEN = 'SecretToken'
client = PactClient(TOKEN)
```