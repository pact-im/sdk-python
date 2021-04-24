import json


class MockResponse:
    def __init__(self, json_data, status_code):
        self.status_code = status_code
        self.json_data = json_data

    @property
    def raw(self):
        return json.dumps(self.json_data).encode()

    def json(self):
        return self.json_data


def mocked_companies(method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/'
    if method == 'post' and url == endpoint and kwargs.get('json') == '{"name": "MockCompanyError"}':
        return MockResponse({}, 400)

    if method == 'get' and url == endpoint:
        return MockResponse({
            "status": "ok",
            "data": {
                "companies": [
                    {
                        "external_id": 1,
                        "name": "COMPANY_NAME",
                        "phone": None,
                        "description": None,
                        "webhook_url": None
                    }
                ],
                "next_page": "fslkfg2lkdfmlwkmlmw4of94wg34lfkm34lg"
            }
        }, 200)
    if method == 'put' and url == '%s1' % endpoint:
        return MockResponse({
            "status": "updated",
            "data": {
                "external_id": 1
            }
        }, 200)

    if method == 'post' and url == endpoint:
        return MockResponse({
            "status": "created",
            "data": {
                "external_id": 5
            }
        }, 200)

    return MockResponse({}, 404)
