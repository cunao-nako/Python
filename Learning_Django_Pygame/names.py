from all_code import get_full_name
import unittest


class NamesTestCase(unittest.TestCase):

    def test_get_full_name(self):
        full_name = get_full_name('janis', 'joplin')
        self.assertEquals(full_name, 'Janis Joplin')


unittest.main()
