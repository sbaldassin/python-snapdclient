import unittest2

from snapdclient.base import Manager
from snapdclient.v2.snaps import Snap


class SnapsTestCase(unittest2.TestCase):

    def setUp(self):
        self.snap = Snap()

    def test_list_snaps(self):
        snaps = self.snap.list()
        self.assertNotEquals(snaps, [])

    def test_find_snap_by_name(self):
        snap = self.snap.find_by_name('core')
        self.assertIsNotNone(snap)

    def test_find_snap_by_name_return_none_if_not_found(self):
        snap = self.snap.find_by_name('fake_snap')
        self.assertIsNone(snap)
