import surrealism as s
import unittest
import random


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

    def test_getsentence_with_a_random_integer(self):
        limits = s._gettablelimits()
        upper_sentence_limit = limits['sen_count']
        sen_id = random.randint(1, upper_sentence_limit)
        sentence = s.getsentence(sen_id)
        var_types = (unicode, str)
        self.assertIsInstance(sentence, var_types)

    def test_getsentence_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s._gettablelimits()
        over_limit = limits['sen_count'] + 1
        self.assertRaises(TypeError, (s.getsentence(over_limit)))

    def test_getsentence_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello my name is bob'
        self.assertRaises(TypeError, (s.getsentence(_string)))

    def test_getsentence_returns_an_error_when_we_submit_a_number_as_a_string(self):
        _string = '64'
        self.assertRaises(TypeError, (s.getsentence(_string)))

    def test_getsentence_returns_an_error_when_we_submit_a_negative_number(self):
        _number = -1
        self.assertRaises(TypeError, (s.getsentence(_number)))

    def test_getsentence_handles_it_when_we_submit_a_float(self):
        _number = 98.9
        sentence = s.getsentence(_number)
        print(sentence)
        var_types = (unicode, str)
        self.assertIsInstance(sentence, var_types)

    def test_that_no_hashed_keywords_remain_in_sentence(self):
        keywords = ['#VERB', '#NOUN', '#ADJECTIVE', '#NAME', '#ADJECTIVE_MAYBE', '#AN', '#RANDOM', '#CAPITALISE',
                    '#CAPALL']
        sentence = s.getsentence()
        for keyword in keywords:
            self.assertNotIn(keyword, sentence)


    # noinspection PyStatementEffect
    """getfault() unit tests"""

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

    def test_getfault_with_a_random_integer(self):
        limits = s._gettablelimits()
        upper_fault_limit = limits['fau_count']
        fau_id = random.randint(1, upper_fault_limit)
        fault = s.getfault(fau_id)
        var_types = (unicode, str)
        self.assertIsInstance(fault, var_types)

    def test_getfault_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s._gettablelimits()
        over_limit = limits['fau_count'] + 1
        self.assertRaises(TypeError, (s.getsentence(over_limit)))

    def test_getfault_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello my name is bob'
        self.assertRaises(TypeError, (s.getfault(_string)))

    def test_getfault_returns_an_error_when_we_submit_a_number_as_a_string(self):
        _string = '64'
        self.assertRaises(TypeError, (s.getfault(_string)))

    def test_getfault_returns_an_error_when_we_submit_a_negative_number(self):
        _number = -1
        self.assertRaises(TypeError, (s.getfault(_number)))

    def test_getfault_handles_it_when_we_submit_a_float(self):
        _number = 98.9
        fault = s.getfault(_number)
        print(fault)
        var_types = (unicode, str)
        self.assertIsInstance(fault, var_types)

    def test_that_no_hashed_keywords_remain_in_fault(self):
        keywords = ['#VERB', '#NOUN', '#ADJECTIVE', '#NAME', '#ADJECTIVE_MAYBE', '#AN', '#RANDOM', '#CAPITALISE',
                    '#CAPALL', '#REPEAT']
        fault = s.getfault()
        for keyword in keywords:
            self.assertNotIn(keyword, fault) 