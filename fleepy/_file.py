# -*- coding: utf-8 -*-
class Upload(object):
    def __init__(self, server, handler='file/upload'):
        self._server = server
        self._handler = handler

    def __call__(self):
        raise NotImplementedError

    def external(self, file_url, file_name, file_size=0,
                 conversation_id=None, upload_id=None):
        """Add file into Fleep from an external source.
        Maximum allowed file size is 1GB. Upload request is
        put into queue and processed by a background job.
        Upload progress events are sent to the client during the
        upload process, see UploadInfo for more details.

        :param file_url: The URL to get the file.
        :param file_name: The name of the file.
        :param file_size: Max 1073741824. Defaults to 0.
        :param conversation_id: Needed if file is related to a conversation.
        :param upload_id: Upload ID on client side.
        """
        return self._server.post(
            'file/upload/external/',
            {'file_url': file_url,
             'file_name': file_name,
             'file_size': file_size,
             'conversation_id': conversation_id,
             'upload_id': upload_id})


class File(object):
    """Empty wrapper for Upload for now.
    """
    def __init__(self, server, handler='file'):
        self._server = server
        self._handler = handler

        self.upload = Upload(self._server)
