# -*- coding: utf-8 -*-
class Task(object):
    """
    """
    def __init__(self, server, handler='task'):
        self._server = server
        self._handler = handler

    def sync(self, conversation_id, from_message_nr=None):
        """Sync all tasks into client.

        :param from_message_nr:  earliest message nr client has received.
        previous messages are read and returned
        """
        self._server.post(
            'task/sync/{}'.format(conversation_id),
            {'from_message_nr': from_message_nr})
