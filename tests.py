# -*- coding: utf-8 -*-
import pickle
import unittest

from mock import create_autospec

from fleepy import Fleepy
from fleepy._server import HTTPClient, Server, Response


class TestFleepy(unittest.TestCase):
    def setUp(self):
        self.server = create_autospec(Server)
        self.api = Fleepy(server=self.server)

    def test_handlers_are_initialized(self):
        handlers = (
            'conversation', 'task', 'avatar', 'account',
            'message', 'info', 'contact', 'file', 'alias', 'search')

        for handler in handlers:
            if not hasattr(self.api, handler):
                raise AttributeError('{} handler missing!!'.format(handler))

    def test_hangout(self):
        data = {
            'hangout_id': 123,
            'hangout_url': 'https://hangouts.com/asda',
            'participants': [1, 2],
        }

        self.api.hangout(**data)
        self.api._server.post.assert_called_once_with('hangout', data)

    def test_classificators(self):
        self.api.classificators()
        self.api._server.post.assert_called_once_with('classificators')


class TestHTTPClient(unittest.TestCase):
    def test_invalid_method(self):
        self.assertRaises(
            ValueError, HTTPClient.request, 'POSAA', 'http')


class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = create_autospec(HTTPClient)
        self.server = Server(client=self.client)

    def mock_response(self, status_code, data=None,
                      cookies=None, headers=None):
        self.client.request.return_value = Response(
            status_code, data, headers, cookies)

    def set_dummy_session(self):
        self.server._set_session(123, 'asda1', 'trrew', 'Test User', [1, 2])

    def test_logout_without_being_logged_in(self):
        self.assertRaises(ValueError, self.server.logout)

    def test_set_session(self):
        self.set_dummy_session()
        self.assertEqual(self.server.ticket, 'trrew')
        self.assertEqual(self.server._cookies['token_id'], 'asda1')
        self.assertEqual(self.server._account_id, 123)
        self.assertEqual(self.server._display_name, 'Test User')

    def test_server_properties(self):
        self.set_dummy_session()
        self.assertEqual(self.server.display_name, 'Test User')
        self.assertEqual(self.server.account_id, 123)

    def test_post(self):
        self.server.call = create_autospec(self.server.call)
        self.server.post('anurl')
        self.server.call.assert_called_with('POST', 'anurl')

        self.server.post('anurl', {'data': "1"})
        self.server.call.assert_called_with('POST', 'anurl', {'data': "1"})

    def test_put(self):
        self.server.call = create_autospec(self.server.call)
        self.server.put('anurl')
        self.server.call.assert_called_with('PUT', 'anurl')

        self.server.put('anurl', {'data': "1"})
        self.server.call.assert_called_with('PUT', 'anurl', {'data': "1"})

    def test_logout(self):
        self.set_dummy_session()
        self.server.call = create_autospec(self.server.call)
        self.server.logout()
        self.server.call.assert_called_once_with('POST', 'account/logout')

    def test_serialize(self):
        self.assertEqual(None, self.server._serialize(None))
        self.assertEqual('{"a": 1}', self.server._serialize({'a': 1}))

    def test_custom_serializer(self):
        server = Server(serializer=pickle)
        serialized_data = pickle.dumps({'a': 1})
        self.assertEqual(serialized_data, server._serialize({'a': 1}))
        self.assertEqual(
            pickle.loads(serialized_data),
            server._deserialize(serialized_data))


if __name__ == '__main__':
    unittest.main()
