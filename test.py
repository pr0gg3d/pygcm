from client import GcmClient

if __name__ == '__main__':
    registration_id = ['APA91bFWdmFLlvX3xwaLHdFTmZBBpc7WodFDueou0Av69lEPZM_X-nzBgkLao4QIy5ktiPSqDm6iu63YF5908zvWKlLgPhLphVM95XaNfPvr6ORvIOpjX0uM5VNwAuFJoo3ehHQq-nbj2c56DIJkxIcFLAgt0XHqXg', 'xxx']
    c = GcmClient("AIzaSyCv_qQDH53J-sK94I1uLcv3iayoZWoAu_s", mode="plaintext")
    r = c.send(registration_id, dict(score=123))
    print r
