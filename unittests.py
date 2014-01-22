import surrealism as s
import unittest

class SurrealismUnittests(unittest.TestCase):
    """getsentence() unititests"""

    def test_getsentence_returns_a_unicode_string(self):
        sentence = s.getsentence()
        var_types = (unicode, str)
        self.assertIsInstance(sentence, var_types)
        
        
    def test_getsentence_returns_a_unicode_string_with_integer_upper_limit(self):
        limits = s._gettablelimits()
        upper_limit = limits['sen_count']
        sentence = s.getsentence(upper_limit)
        var_types = (unicode, str)
        self.assertIsInstance(sentence, var_types)
        
        
    def test_getsentence_returns_a_unicode_string_with_integer_lower_limit(self):
        lower_limit = 1
        sentence = s.getsentence(lower_limit)
        var_types = (unicode, str)
        self.assertIsInstance(sentence, var_types)
        
    
    def test_getsentence_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s._gettablelimits()
        over_limit = limits['sen_count'] + 1
        self.assertRaises(TypeError, (s.getsentence(over_limit)))
        
        
    def test_getsentence_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello'
        self.assertRaises(TypeError, (s.getsentence(_string)))
        
        
        
        
        
    """getfault unit tests"""
        
    def test_getfault_returns_a_unicode_string(self):
        fault = s.getfault()
        var_types = (unicode, str)
        self.assertIsInstance(fault, var_types)
        
            
    def test_getfault_returns_a_unicode_string_with_integer_upper_limit(self):
        limits = s._gettablelimits()
        upper_limit = limits['fau_count']
        fault = s.getfault(upper_limit)
        var_types = (unicode, str)
        self.assertIsInstance(fault, var_types)
        
        
    def test_getfault_returns_a_unicode_string_with_integer_lower_limit(self):
        lower_limit = 1
        fault = s.getfault(lower_limit)
        var_types = (unicode, str)
        self.assertIsInstance(fault, var_types)
        
    
    def test_getfault_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s._gettablelimits()
        over_limit = limits['fau_count'] + 1
        self.assertRaises(TypeError, (s.getfault(over_limit)))
        
        
    def test_getfault_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello'
        self.assertRaises(TypeError, (s.getfault(_string)))
        
        
        
        
        
        
        