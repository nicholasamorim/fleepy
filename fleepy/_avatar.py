# -*- coding: utf-8 -*-
class Avatar(object):
    """
    """
    def __init__(self, server, handler='avatar'):
        self._server = server
        self._handler = handler

    def delete(self):
        """Deletes current avatar
        """
        self._server.post('avatar/delete')

    def upload(self):
        """
        URL: https://fleep.io/api/avatar/upload
        Upload avatar

        Optional URL arguments:
            ticket=XXX Access ticket _method=PUT This POST is actually PUT
        PUT:
            Content-Type, Content-Disposition are taken from main header

        Output:
        file_id
        name
        size
        """
        raise NotImplementedError
