"""
Python wrapper for Google Cloud Messaging service.
"""

GOOGLE_SEND_URL = 'https://android.googleapis.com/gcm/send'


class BaseGcmClient(object):
    def __init__(self, api_key, client=None):
        self.api_key = api_key

        # Client setup
        self._client = client(self._content_handler)

    def send(self, registration_ids, data=None, delay_while_idle=False, time_to_live=None, collapse_key=None):
        send_data = {}

        # Set registration ids
        if not isinstance(registration_ids, (list, tuple)):
            registration_ids = [registration_ids]

        send_data['delay_while_idle'] = bool(delay_while_idle)

        # time_to_live and collapse_key need to be specified both or none.
        if (time_to_live is not None) ^ (collapse_key is not None):
            raise ValueError("'time_to_live' and 'collapse_key' need to be specified both or none")
            send_data['time_to_live'] = int(time_to_live)
            send_data['collapse_key'] = collapse_key

        # the data is optional
        if data is not None:
            send_data['data'] = data

        # send
        return self._client.send(self.api_key, registration_ids, send_data)

