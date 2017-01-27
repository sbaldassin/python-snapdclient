from snapdclient.client import Client


class Manager:

    def __init__(self, api_url, api_version):
        self.url = \
            'http+unix://%2Frun%2Fsnapd.socket/{api_version}/{api_url}'.format(
                api_version=api_version, api_url=api_url)
        self.client = Client()

    def _get_all(self):
        return self.client.session.get(self.url).json()['result']

    def list(self):
        result = self._get_all()
        return result or []

    def find_by_name(self, name):
        snaps = self._get_all()
        try:
            snap = list(filter(lambda x: x['name'] == name, snaps))[0]
        except IndexError:
            snap = None
        return snap
