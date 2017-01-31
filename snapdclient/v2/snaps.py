from snapdclient.base import Manager

class Snap(Manager):

    def __init__(self):
        self.url = 'snaps'
        self.version = 'v2'
        super().__init__(self.url, self.version)

    def install(self, snap_name):
        message = {"action": "install", "snaps": [snap_name]}
        self.client.session.post(self.url, json=message)
