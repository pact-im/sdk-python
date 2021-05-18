# Companies

### Get companies

```python
from pact_im import PactClient
client = PactClient('SecretToken')

companies_result = client.companies.get_companies(per=100)
for company in companies_result.companies:
    print(company.name, company.description)
```

### Update company

```python
from pact_im import PactClient
client = PactClient('SecretToken')

updated_external_id = client.companies.update_company(
    external_id=1,
    name='NewName',
    description='NewDescription'
)
```

### Create new company
>  If you want to receive webhooks make sure that webhook_url is present. Webhook url must be valid and response code on POST json-request {'source':'pact.im', 'operation':'test'} must be 200

```python
from pact_im import PactClient
client = PactClient('SecretToken')

created_external_id = client.companies.create_company(
    name='MyCompany',
    description='company description',
    phone='79250001122',
    webhook_url='https://example.com'
)
```