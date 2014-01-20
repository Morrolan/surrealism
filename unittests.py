import surrealism as s
import unittest

class SurrealismUnittests(unittest.TestCase):


    def test_getsentence_returns_a_unicode_string(self):
        sentence = s.getsentence()
        self.assertEqual(type(sentence), unicode)
        
        
    def test_getfault_returns_a_unicode_string(self):
        fault = s.getfault()
        self.assertEqual(type(fault), unicode)
        
        
    def test_getsentence_returns_a_unicode_string_with_integer_upper_limit(self):
        limits = s._gettablelimits()
        upper_limit = limits['sen_count']
        sentence = s.getsentence(upper_limit)
        self.assertEqual(type(sentence), unicode)
        
        
    def test_getsentence_returns_a_unicode_string_with_integer_lower_limit(self):
        lower_limit = 1
        sentence = s.getsentence(lower_limit)
        self.assertEqual(type(sentence), unicode)
        
    
    def test_getsentence_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s._gettablelimits()
        over_limit = limits['sen_count'] + 1
        #sentence = s.getsentence(over_limit)
        self.assertRaises(AttributeError, sentence = s.getsentence(over_limit)
        