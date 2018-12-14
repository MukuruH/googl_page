import unittest
from cohort import andela_35

class TestCohort(unittest.TestCase):

    def test_attendees(self):
        andela35Dec = andela_35(70,'Dec',5,'3')
        self.assertIs(type(andela35Dec.duration), int)
        self.assertIsInstance(andela35Dec, andela_35)