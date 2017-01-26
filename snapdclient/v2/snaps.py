from snapdclient.base import Manager


class Snap(Manager):

    def __init__(self):
        self.url = 'snaps'
        super().__init__(self.url)