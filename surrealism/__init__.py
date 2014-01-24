"""#!/usr/bin/env python

#############################################################################
#    surrealism.py - Surreal sentence and error message generator
#    Copyright (C) 2014  Ian Havelock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
#
# This is a derivative work (used with permission) from www.ravenblack.net
# Credit also goes to Kevan Davis on whose work the surrealism generator at
# Ravenblack.net is based on.
#
#############################################################################"""

__ALL__ = ['getfault', 'getsentence', 'version', 'sentencetest', 'faulttest']


# IMPORTS ###################################################################

import sqlite3
import random
import pkg_resources

# PARTICULAR IMPORTS ########################################################

from pkg_resources import resource_filename

# CONSTANTS #################################################################

CONN = sqlite3.connect(resource_filename(__name__, 'surrealism.sqlite'))


# VARIABLES #################################################################



# CLASSES ###################################################################



#############################################################################

# EXCEPTION CLASS HANDLER

#class SurrealError(Exception):
#    """Custom Exception handler so that I can raise real errors instead of just 
#    printing.  This allows other devs to silently bypass my errors if they wish 
#    to, rather than me forcing the code to exit."""
#    
#    def __init__(self, value):
#        self.value = value
#    def __str__(self):
#        return repr(self.value)
        

#  EXTERNAL METHODS BELOW

def version():
    """Returns the current version of the Surrealism module."""
    
    return pkg_resources.require('surrealism')[0].version
    
    
def sentencetest():
    """Return 1 random version of each sentence to test sentence structure."""
    
    _counts = _gettablelimits()
    max_num = _counts['sen_count']
    counter = 0
    
    while counter < max_num: 
        counter = counter + 1
        print("\nSentence ID:  " + str(counter))
        _sentence = _getsentence(counter)
        
        if _sentence[0] == 'n':
            print("Sentence is DISABLED - ignoring...")
        
        if _sentence[0] == 'y':
            _result = _process_sentence(_sentence, _counts)
            print(_result)
            
            
def faulttest():
    """Returns 1 instance of each programming fault for testing purposes."""
    
    _counts = _gettablelimits()
    max_num = _counts['fau_count']
    counter = 0
    
    while counter < max_num: 
        counter = counter + 1
        print("\nFault ID:  " + str(counter))
        _fault = _getfault(counter)
        
        if _fault[0] == 'n':
            print("Fault is DISABLED - ignoring...")
        
        if _fault[0] == 'y':
            _result = _process_sentence(_fault, _counts)
            print(_result)
    

def getfault(fault_id=None):
    """Retrieve a randomly-generated error message as a unicode string.
    
        getfault(fault_id=None)
        
        Allows you to optionally specify an integer representing the fault_id 
        from the database table.  This allows you to retrieve a specific fault 
        each time, albeit with different keywords."""
    
    _counts = _gettablelimits()
    _fault = None
    _id = 0
    

    try:
        if isinstance(fault_id, int):
            _id = fault_id
        elif isinstance(fault_id, float):
            print("""ValueError:  Floating point number detected.
                  Rounding number to 0 decimal places.""")
            _id = round(fault_id)
        else:
            _id = random.randint(1, _counts['fau_count'])
            
    except ValueError:
        print("ValueError:  Incorrect parameter type detected.")
    
    if _id <= _counts['fau_count']:
        _fault = _getfault(_counts, fault_id = _id)
    else:
        print("""ValueError:  Parameter integer is too high.
              Maximum permitted value is {0}.""".format(str(_counts['fau_count'])))
        _id = _counts['fau_count']
        _fault = _getfault(_counts, fault_id = _id)
    
    if _fault is not None:
        while _fault[0] == 'n':
            if _id is not None:
                _fault = _getfault(_counts, None)
            else:
                _fault = _getfault(_counts, _id)
        if _fault[0] == 'y':
            _result = _process_sentence(_fault, _counts)
        return _result
    else:
        print('ValueError: _fault cannot be None.')
    

def getsentence(sentence_id=None):
    """Retrieve a randomly-generated sentence as a unicode string.
    
        getsentence(sentence_id=None)
        
        Allows you to optionally specify an integer representing the sentence_id
        from the database table.  This allows you to retrieve a specific 
        sentence each time, albeit with different keywords."""
    
    _counts = _gettablelimits()
    _sentence = None
    _id = 0
    

    try:
        if isinstance(sentence_id, int):
            _id = sentence_id
        elif isinstance(sentence_id, float):
            print("""ValueError:  Floating point number detected.
                  Rounding number to 0 decimal places.""")
            _id = round(sentence_id)
        else:
            _id = random.randint(1, _counts['sen_count'])
            
    except ValueError:
        print("ValueError:  Incorrect parameter type detected.")
    
    if _id <= _counts['sen_count']:
        _sentence = _getsentence(_counts, sentence_id = _id)
    else:
        print("""ValueError:  Parameter integer is too high.
              Maximum permitted value is {0}.""".format(str(_counts['sen_count'])))
        _id = _counts['sen_count']
        _sentence = _getsentence(_counts, sentence_id = _id)
    
    if _sentence is not None:
        while _sentence[0] == 'n': 
            if _id is not None:
                _sentence = _getsentence(_counts, None)
            else:
                _sentence = _getsentence(_counts, _id)
        if _sentence[0] == 'y':
            _result = _process_sentence(_sentence, _counts)
        return _result
    else:
        print('ValueError: _sentence cannot be None.')

   
    
    
#############################################################################

#  INTERNAL METHODS BELOW

    
def _getfault(_counts, fault_id=None):
    """Let's fetch a random fault that we then need to substitute bits of..."""
    
    cursor = CONN.cursor()
    
    if fault_id is not None:
        _id_to_fetch = fault_id
    else:
        _id_to_fetch = random.randint(1, _counts['fau_count'])
    
    _query = "select * from surfaults where fau_id = {0}".format(_id_to_fetch)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result
    

def _getsentence(_counts, sentence_id=None):
    """Let's fetch a random sentence that we then need to substitute bits 
    of..."""
    
    cursor = CONN.cursor()
    
    if sentence_id is not None:
        _id_to_fetch = sentence_id
    else:
        _id_to_fetch = random.randint(1, _counts['sen_count'])
    
    _query = ("""select * from sursentences where sen_id = {0}"""
                .format(_id_to_fetch))
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result


def _getverb(_counts):
    """Let's fetch a VERB"""
    
    cursor = CONN.cursor()
    _rand = random.randint(1, _counts['verb_count'])
    _query = """select * from surverbs where verb_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]


def _getnoun(_counts):
    """Let's fetch a NOUN from the database..."""
    
    cursor = CONN.cursor()
    _rand = random.randint(1, _counts['noun_count'])
    _query = """select * from surnouns where noun_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]
    
    
def _getadjective(_counts):
    """Let's fetch an ADJECTIVE from the database..."""
    
    cursor = CONN.cursor()
    _rand = random.randint(1, _counts['adj_count'])
    _query = """select * from suradjs where adj_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]
    

def _getname(_counts):
    """Let's fetch a NAME from the database..."""
    
    cursor = CONN.cursor()
    _rand = random.randint(1, _counts['name_count'])
    _query = """select * from surnames where name_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    
        
    return _result[1]


def _gettablelimits():
    """Here we simply take a count of each of the database tables so we know our
    upper limits for our random number calls then return a dictionary of them 
    to the calling function..."""
    
    _table_counts = {
                    'adj_count' : None,
                    'name_count' : None,
                    'noun_count' : None,
                    'sen_count' : None,
                    'fau_count' : None,
                    'verb_count' : None        
                    }
    
    cursor = CONN.cursor()
    
    cursor.execute('select count(*) from suradjs')
    _table_counts['adj_count'] = cursor.fetchone()
    _table_counts['adj_count'] = _table_counts['adj_count'][0]

    cursor.execute('select count(*) from surnames')
    _table_counts['name_count'] = cursor.fetchone()
    _table_counts['name_count'] = _table_counts['name_count'][0]

    cursor.execute('select count(*) from surnouns')
    _table_counts['noun_count'] = cursor.fetchone()
    _table_counts['noun_count'] = _table_counts['noun_count'][0]

    cursor.execute('select count(*) from sursentences')
    _table_counts['sen_count'] = cursor.fetchone()
    _table_counts['sen_count'] = _table_counts['sen_count'][0]
    
    cursor.execute('select count(*) from surfaults')
    _table_counts['fau_count'] = cursor.fetchone()
    _table_counts['fau_count'] = _table_counts['fau_count'][0]

    cursor.execute('select count(*) from surverbs')
    _table_counts['verb_count'] = cursor.fetchone()
    _table_counts['verb_count'] = _table_counts['verb_count'][0]

    return _table_counts


def _process_sentence(_sentence_tuple, _counts):
    """pull the actual sentence from the tuple (tuple contains additional 
    data such as ID)"""
        
    _sentence = _sentence_tuple[2]
    
    # now we start replacing words one type at a time...
    _sentence = _replace_verbs(_sentence, _counts)
        
    _sentence = _replace_nouns(_sentence, _counts)
        
    _sentence = _replace_adjective_maybe(_sentence, _counts)
        
    _sentence = _replace_adjectives(_sentence, _counts)
        
    _sentence = _replace_names(_sentence, _counts)
    
    # here we perform a check to see if we need to use A or AN depending on the 
    # first letter of the following word...
    _sentence = _replace_an(_sentence, _counts)
    
    # now we will read, choose and substitute each of the RANDOM sentence tuples
    _sentence = _replace_random(_sentence)
    
    # now we are going to choose whether to capitalize words/sentences or not
    ############
    #NOTE:  Buggy as hell, as it doesn't account for words that are already 
    # capitalized
    ############
    _sentence = _replace_capitalise(_sentence)
    
    # here we will choose whether to capitalize all words in the sentence
    ############
    #NOTE:  Buggy as hell, as it doesn't account for words that are already 
    # capitalized
    ############
    _sentence = _replace_capall(_sentence)
    
    return _sentence
    
    
def _replace_verbs(_sentence, _counts):
    """Lets find and replace all instances of #VERB"""
    
    if _sentence is not None:
        while _sentence.find('#VERB') != -1:
            _sentence = _sentence.replace('#VERB', str(_getverb(_counts)), 1)
            
            if _sentence.find('#VERB') == -1:
                return _sentence 
        return _sentence
    else:
        return _sentence
        
        
def _replace_nouns(_sentence, _counts):
    """Lets find and replace all instances of #NOUN"""
    
    if _sentence is not None:
        while _sentence.find('#NOUN') != -1:
            _sentence = _sentence.replace('#NOUN', str(_getnoun(_counts)), 1)
            
            if _sentence.find('#NOUN') == -1:
                return _sentence
            
        return _sentence
    else:
        return _sentence


def _replace_adjective_maybe(_sentence, _counts):
    """Lets find and replace all instances of #ADJECTIVE_MAYBE"""
    
    _random_decision = random.randint(0, 1)
       
    if _sentence is not None:
        
        while _sentence.find('#ADJECTIVE_MAYBE') != -1:
            
            if _random_decision % 2 == 0:
                _sentence = _sentence.replace('#ADJECTIVE_MAYBE', 
                                        ' ' + str(_getadjective(_counts)), 1)
            elif _random_decision % 2 != 0:
                _sentence = _sentence.replace('#ADJECTIVE_MAYBE', '', 1)
            
            if _sentence.find('#ADJECTIVE_MAYBE') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence
    
    
def _replace_adjectives(_sentence, _counts):   
    """Lets find and replace all instances of #ADJECTIVE"""
    
    if _sentence is not None:
        
        while _sentence.find('#ADJECTIVE') != -1:
            _sentence = _sentence.replace('#ADJECTIVE', 
                                        str(_getadjective(_counts)), 1)
            
            if _sentence.find('#ADJECTIVE') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence
    
    
def _replace_names(_sentence, _counts):
    """Lets find and replace all instances of #NAME"""
    
    if _sentence is not None:
        
        while _sentence.find('#NAME') != -1:
            _sentence = _sentence.replace('#NAME', str(_getname(_counts)), 1)
            
            if _sentence.find('#NAME') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence


def _replace_an(_sentence, _counts):
    """Lets find and replace all instances of #AN
    This is a little different, as this depends on whether the next 
    word starts with a vowel or a consonant."""
    
    if _sentence is not None:
        while _sentence.find('#AN') != -1:
            _an_index = _sentence.find('#AN')
            
            if _an_index > -1:
                _an_index = _an_index + 4
                
                if _sentence[_an_index] in 'aeiouAEIOU':
                    _sentence = _sentence.replace('#AN', str('an'), 1)
                else:
                    _sentence = _sentence.replace('#AN', str('a'), 1)
                
            if _sentence.find('#AN') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence


def _replace_random(_sentence):
    """Lets find and replace all instances of #RANDOM"""
    
    if _sentence is not None:
        
        while _sentence.find('#RANDOM') != -1:
            
            _random_index = _sentence.find('#RANDOM') 
            _start_index = _sentence.find('#RANDOM') + 8
            _end_index = _sentence.find(']')
            
            if _sentence.find('#RANDOM') is not None:
                
                _sub_list = _sentence[_start_index:_end_index].split(',')

                
                _choice = random.randint(1, int(_sub_list[0]))
                #_sub_list[_choice]
            
            _to_be_replaced = _sentence[_random_index:_end_index + 1]
            _sentence = _sentence.replace(_to_be_replaced, 
                                            _sub_list[_choice], 1)
                            
            if _sentence.find('#RANDOM') == -1:
                return _sentence
                  
        return _sentence
    else:
        return _sentence
    

def _replace_capitalise(_sentence):
    """here we replace all instances of #CAPITALISE and cap the next word.
    ############
    #NOTE:  Buggy as hell, as it doesn't account for words that are already 
    #capitalized
    ############"""
    
    #print "\nReplacing CAPITALISE:  "
    
    if _sentence is not None:
        while _sentence.find('#CAPITALISE') != -1:
            _cap_index = _sentence.find('#CAPITALISE')
            _part1 = _sentence[:_cap_index]
            _part2 = _sentence[_cap_index+12:]
            _sentence = _part1 + _part2.capitalize()    
            _sentence = _sentence.replace('#CAPITALISE ', '', 1)
                
        if _sentence.find('#CAPITALISE') == -1:
            return _sentence
        return _sentence
    else:
        return _sentence
        

def _replace_capall(_sentence):
    """here we replace all instances of #CAPALL and cap the entire sentence.
    ############
    #NOTE:  Buggy as hell, as it doesn't account for words that are already 
    #capitalized
    ############"""
    
    #print "\nReplacing CAPITALISE:  "
    
    if _sentence is not None:
        while _sentence.find('#CAPALL') != -1:
            _cap_index = _sentence.find('#CAPALL')
            _sentence = _sentence.upper()    
            _sentence = _sentence.replace('#CAPALL ', '', 1)
                
        if _sentence.find('#CAPALL') == -1:
            return _sentence
        return _sentence
    else:
        return _sentence
