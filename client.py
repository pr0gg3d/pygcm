from pygcm import BaseGcmClient
import urllib2

from pygcm import GOOGLE_SEND_URL
from pygcm.content_handlers import CONTENT_HANDLERS



class HTTPClient(object):
    url = GOOGLE_SEND_URL

    def __init__(self, handler):
        self._handler = handler()


class Urllib2Client(HTTPClient):
    immediate_return = False

    def _gotResponse(self, result):
        pass

    def send(self, api_key, registration_ids, send_data):
        headers = {
            'Content-Type': self._handler.content_type,
            'Authorization': 'key=%s' % api_key
        }
        x = self._handler.dump(registration_ids, send_data)
        print x
        request = urllib2.Request(
            self.url,
            self._handler.dump(registration_ids, send_data),
            headers
        )
        response = urllib2.urlopen(request).read()
        return self._handler.load(response)


class GcmClient(BaseGcmClient):
    def __init__(self, api_key, mode='json', client=Urllib2Client):
        try:
            self._content_handler = CONTENT_HANDLERS[mode]
        except KeyError:
            modes = ' or '.join(CONTENT_HANDLERS.keys())
            raise ValueError('"mode" must be %s' % modes)
        super(GcmClient, self).__init__(api_key, client=client)
