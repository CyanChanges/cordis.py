from unittest import TestCase

from cordis import Context


class BasicTestCase(TestCase):
    def test_creation(self):
        app = Context()
        self.assertIn('__prototype__', vars(app))
