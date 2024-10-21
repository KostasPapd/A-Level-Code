import unittest
from testingNameFunc import formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name("pete", "seeger")
        self.assertEqual(result, "Pete Seeger")

if __name__== '__main__':
    unittest.main()
