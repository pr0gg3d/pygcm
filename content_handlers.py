import json
import urllib


class JsonHandler(object):
    content_type = 'application/json'

    def dump(self, registration_ids, send_data):
        send_data['registration_ids'] = registration_ids
        return json.dumps(send_data)

    def load(self, data):
        return json.loads(data)


class PlainTextHandler(object):
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'

    def dump(self, registration_ids, send_data):
        # Check registration_ids
        if len(registration_ids) != 1:
            raise ValueError("Only one registration_id allowed for plaintext")
        send_data['registration_id'] = registration_ids[0]

        # Flat data
        if 'data' in send_data:
            data = send_data.pop('data')
            d = dict([('data_%s' % k, v) for k, v in data.iteritems()])
            send_data.update(d)
        serialized_data = urllib.urlencode(send_data)
        return serialized_data

    def load(self, data):
        return data

CONTENT_HANDLERS = {
    'json': JsonHandler,
    'plaintext': PlainTextHandler,
}
