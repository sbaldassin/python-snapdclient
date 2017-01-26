from snapdclient.client import Client


class Manager:

    def __init__(self, api_url):
        self.url = \
            'http+unix://%2Frun%2Fsnapd.socket/{api_version}/{api_url}'.format(
                api_version='v2', api_url=api_url)
        self.client = Client()

    def list(self):
        result = self.client.session.get(self.url).json()['result']
        return result or []

    def find_by_name(self, name):
        snaps = self.client.session.get(self.url).json()['result']
        try:
            snap = list(filter(lambda x: x['name'] == name, snaps))[0]
        except IndexError:
            snap = None
        return snap
