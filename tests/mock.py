import json
import unittest
from unittest.mock import patch

from pact_im import PactClient
from pact_im.schema import Method
from pact_im.services.base import Service


class MockResponse:
    def __init__(self, json_data, status_code):
        self.status_code = status_code
        self.json_data = json_data

    @property
    def content(self):
        return json.dumps(self.json_data).encode()

    def json(self):
        return self.json_data


class ServiceTestCase(unittest.TestCase):
    service = None
    mock_func = None

    def setUp(self):
        self.client = PactClient('some_token')
        self.srv = None
        if issubclass(self.service, Service):
            service_name = self.service.class_name()
            if hasattr(self.client, service_name):
                self.srv = getattr(self.client, service_name)

        if not self.srv:
            raise AttributeError('Service %s not found' % self.service.class_name())

        if self.mock_func:
            self.patcher = patch('requests.request', side_effect=self.mock_func)
            self.mock_request = self.patcher.start()

    def tearDown(self) -> None:
        if self.mock_func:
            self.patcher.stop()
        super().tearDown()


def mocked_companies(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/'
    if method == Method.POST and url == endpoint and kwargs.get('json') == '{"name": "MockCompanyError"}':
        return MockResponse({}, 400)

    if method == Method.GET and url == endpoint:
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
    if method == Method.PUT and url == '%s1' % endpoint:
        return MockResponse({
            "status": "updated",
            "data": {
                "external_id": 1
            }
        }, 200)

    if method == Method.POST and url == endpoint:
        return MockResponse({
            "status": "created",
            "data": {
                "external_id": 5
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_channels(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/channels/'

    if method == Method.GET and url == endpoint % 5:
        return MockResponse({
            "status": "ok",
            "data": {
                "channels": [
                    {
                        "external_id": 399,
                        "provider": "whatsapp"
                    }
                ],
                "next_page": "fslkfg2lkdfmlwkmlmw4of94wg34lfkm34lg"
            }
        }, 200)

    if method == Method.POST and endpoint % 54:
        return MockResponse({
            "status": "created",
            "data": {
                "external_id": 1
            }
        }, 200)

    if method == Method.PUT and (endpoint % 54) + '1':
        return MockResponse({
            "status": "updated",
            "data": {
                "external_id": 1
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_conversations(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/conversations/'

    if method == Method.GET and url == endpoint % 54:
        return MockResponse({
            "status": "ok",
            "data": {
                "conversations": [
                    {
                        "external_id": 1,
                        "name": "Friend",
                        "channel_id": 1,
                        "channel_type": "whatsapp",
                        "created_at": "2017-04-25T18:30:23.076Z",
                        "created_at_timestamp": 1603119600,
                        "avatar": "/avatars/original/missing.png",
                        "sender_external_id": "79260000001",
                        "meta": {

                        }
                    }
                ],
                "next_page": "fslkfg2lkdfmlwkmlmw4of94wg34lfkm34lg"
            }
        }, 200)
    if (method == Method.POST and endpoint % 54) or (method == Method.GET and (endpoint % 54) + '/1'):
        return MockResponse({
            "status": "ok",
            "data": {
                "conversation": {
                    "external_id": 1,
                    "name": "79250000001",
                    "channel_id": 1,
                    "channel_type": "whatsapp",
                    "created_at": "2017-11-11T10:17:10.655Z",
                    "created_at_timestamp": 1603119600,
                    "avatar": "/avatars/original/missing.png",
                    "sender_external_id": "79250000001",
                    "meta": {

                    }
                }
            }
        }, 200)
    if method == Method.PUT and (endpoint % 54) + '/1/assign':
        return MockResponse({
            "status": "ok",
            "data": {
                "conversation": {
                    "external_id": 1,
                }
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_jobs(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/channels/%s/jobs/%s/'

    if method == Method.GET and url == endpoint % (54, 1, 1):
        return MockResponse({
            "status": "ok",
            "data": {
                "id": 1,
                "company_id": 1,
                "channel": {
                    "id": 1,
                    "type": "whatsapp"
                },
                "conversation_id": 1,
                "state": "delivered",
                "message_id": 1,
                "details": {
                    "result": "DELIVERED"
                },
                "created_at": 1510393147
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_service_messages_service(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/service_messages/'

    if method == Method.POST and url == endpoint % 54:
        return MockResponse({
            "status": "ok",
            "data": {
                "id": 42,
                "company_id": 154
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_messages_service(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/conversations/%s/messages/'

    if method == Method.GET and url == endpoint % (54, 1):
        return MockResponse({
            "status": "ok",
            "data": {
                "messages": [
                    {
                        "external_id": 47098,
                        "channel_id": 381,
                        "channel_type": "whatsapp",
                        "message": "Hello",
                        "income": False,
                        "created_at": "2017-09-17T12:44:28.000Z",
                        "created_at_timestamp": 1603119600,
                        "attachments": [

                        ]
                    }
                ],
                "next_page": "fslkfg2lkdfmlwkmlmw4of94wg34lfkm34lg"
            }
        }, 200)

    if method == Method.POST and url == endpoint % (54, 1):
        return MockResponse({
            "status": "ok",
            "data": {
                "id": 18,
                "company_id": 154,
                "channel": {
                    "id": 399,
                    "type": "whatsapp"
                },
                "conversation_id": 8741,
                "state": "trying_deliver",
                "message_id": None,
                "details": None,
                "created_at": 1510396057
            }
        }, 200)

    return MockResponse({}, 404)


def mocked_attachment_service(_, method, url, **kwargs):
    endpoint = 'https://api.pact.im/p1/companies/%s/conversations/%s/messages/attachments/'

    if method == Method.POST and url == endpoint % (54, 1):
        return MockResponse({
            "status": "ok",
            "data": {
                "external_id": 1
            }
        }, 200)

    return MockResponse({}, 404)