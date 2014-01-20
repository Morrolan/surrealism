import surrealism as s
import unittest

class SurrealismUnittests(unittest.TestCase):

    def test_getsentence_returns_a_string(self):
        _sentence = s.getsentence()
        print _sentence
        print str(type(_sentence))
        var_types = (str, unicode)
        self.assertIsInstance(_sentence, var_types)