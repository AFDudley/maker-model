import unittest
from cdp import CDP

class TestBasicCDP(unittest.TestCase):
    def setUp(self):
        cdp1 = cdp.CDP(self.params, self.feeds, self.env)
        self.env.actor = 'bob'
        cdp2 = cdp.CDP(self.params, self.feeds, self.env)
        self.env.actor = 'alice' # reset to alice

    def test_issue_just_enough(self):
        cdp1.add(100.)
    def test_issue_too_many(self):
        cdp1.add(100.)



if __name__ == "__main__":
    unittest.main()
