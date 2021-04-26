# Companies

```python
from pact_im import PactClient

TOKEN = 'SecretToken'

client = PactClient(TOKEN)
```

### Get companies

```python
companies_result = client.companies.get_companies(per=100)
for company in companies_result.companies:
    print(company.name, company.description)
```

### Update company
```python
updated_external_id = client.companies.update_company(
    external_id=1,
    name='NewName',
    description='NewDescription'
)
```

### Create new company

```python
created_external_id = client.companies.create_company(
    name='MyCompany',
    description='company decription',
    phone='79250001122',
    webhook_url='https://example.com'
)
```