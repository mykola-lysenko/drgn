from pathlib import Path
import unittest

VMCORE_PATH = Path("/proc/vmcore")


@unittest.skipUnless(VMCORE_PATH.exists(), "not running in kdump")
class TestDummy(unittest.TestCase):
    def test_dummy(self):
        pass
