from snapdclient.base import Manager


class Snap(Manager):

    def __init__(self):
        self.url = 'snaps'
        self.version = 'v2'
        super().__init__(self.url, self.version)

    def install(self):
        message = {"action": "refresh", "snaps": ["ubuntu-calculator-app"]}
        self.client.session.post(self.url, json=message, auth=("balda", "zoelarayani12@"))