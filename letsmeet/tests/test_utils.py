from unittest import TestCase
from letsmeet.utils import ShortenMethod, get_url_shortcut, LINK_LEN


class Test_url_shortener(TestCase):
    test_url1 = "aaBBcc123"
    test_url2 = "aABbcc123"
    test_url3 = "jklfskjdflksjljsdlkfjslkjlke32aABbcc123"

    def test_hash_shortener(self):
        self._test_shortener(ShortenMethod.HASH)

    def test_random_shortener(self):
        self._test_shortener(ShortenMethod.RANDOM)

    def _test_shortener(self, method: ShortenMethod):
        short1 = get_url_shortcut(self.test_url1, method)
        short2 = get_url_shortcut(self.test_url2, method)
        short3 = get_url_shortcut(self.test_url3, method)
        self.assertNotEqual(short1, short2)
        self.assertNotEqual(self.test_url1, short2)
        self.assertEqual(len(short1), LINK_LEN)
        self.assertEqual(len(short3), LINK_LEN)
