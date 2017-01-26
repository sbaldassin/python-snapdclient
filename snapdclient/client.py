import requests_unixsocket


class Client:

    def __init__(self):
        self.session = requests_unixsocket.Session()
