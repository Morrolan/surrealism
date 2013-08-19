#!/usr/bin/env python

#############################################################################
#    surrealism.py - Surreal sentence generator
#    Copyright (C) 2013  Ian Havelock
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
#############################################################################

__ALL__ = ['getfault', 'getsentence', 'Surrealism']


# IMPORTS ###################################################################



# PARTICULAR IMPORTS ########################################################

import sqlite3
import random

# CONSTANTS #################################################################

CONN = sqlite3.connect('surrealism.sqlite')

# VARIABLES #################################################################



# CLASSES ###################################################################



#############################################################################

#  EXTERNAL METHODS BELOW


def getfault():
    """Retrieve a randomly-generated error message as a unicode string."""
    _counts = _gettablelimits()
    _sentence = _getfault(_counts)
    
    while _sentence[0] == 'n':
        _sentence = _getfault(_counts)
    if _sentence[0] == 'y':
        _result = _process_sentence(_sentence, _counts)
    return _result
    

def getsentence():
    """Retrieve a randomly-generated sentence as a unicode string."""
    _counts = _gettablelimits()
    _sentence = _getsentence(_counts)
    
    while _sentence[0] == 'n':
        _sentence = _getsentence(_counts)
    if _sentence[0] == 'y':
        _result = _process_sentence(_sentence, _counts)
    return _result 
    
    
    
#############################################################################

#  INTERNAL METHODS BELOW

def _getsentence(_counts):
    # Let's fetch the sentence that we then need to substitute bits of!
    cursor = CONN.cursor()
    _rand = random.randint(1,_counts['sen_count'])
    _query = """select * from sursentences where sen_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result
    
    
def _getfault(_counts):
    # Let's fetch the sentence that we then need to substitute bits of!
    cursor = CONN.cursor()
    _counts = _gettablelimits()
    _query = """select * from sursentences where sen_id = 46"""
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result


def _getverb(_counts):
    # Let's fetch a VERB
    cursor = CONN.cursor()
    _rand = random.randint(1,_counts['verb_count'])
    _query = """select * from surverbs where verb_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]


def _getnoun(_counts):
    # Let's fetch a NOUN
    cursor = CONN.cursor()
    _rand = random.randint(1,_counts['noun_count'])
    _query = """select * from surnouns where noun_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]
    
    
def _getadjective(_counts):
     # Let's fetch an ADJECTIVE
    cursor = CONN.cursor()
    _rand = random.randint(1,_counts['adj_count'])
    _query = """select * from suradjs where adj_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]
    

def _getname(_counts):
    # Let's fetch a NAME
    cursor = CONN.cursor()
    _rand = random.randint(1,_counts['name_count'])
    _query = """select * from surnames where name_id = {0}""".format(_rand)
    cursor.execute(_query)
    _result = cursor.fetchone()
    return _result[1]


def _gettablelimits():
    
    _table_counts = {
                    'adj_count' : None,
                    'name_count' : None,
                    'noun_count' : None,
                    'sen_count' : None,
                    'verb_count' : None        
                    }
    
    cursor = CONN.cursor()
    
    cursor.execute('select count(*) from suradjs')
    _table_counts['adj_count'] = cursor.fetchone()
    _table_counts['adj_count'] = _table_counts['adj_count'][0] -1

    cursor.execute('select count(*) from surnames')
    _table_counts['name_count'] = cursor.fetchone()
    _table_counts['name_count'] = _table_counts['name_count'][0] -1

    cursor.execute('select count(*) from surnouns')
    _table_counts['noun_count'] = cursor.fetchone()
    _table_counts['noun_count'] = _table_counts['noun_count'][0] -1

    cursor.execute('select count(*) from sursentences')
    _table_counts['sen_count'] = cursor.fetchone()
    _table_counts['sen_count'] = _table_counts['sen_count'][0] -1

    cursor.execute('select count(*) from surverbs')
    _table_counts['verb_count'] = cursor.fetchone()
    _table_counts['verb_count'] = _table_counts['verb_count'][0] -1

    return _table_counts


def _process_sentence(_sentence_tuple, _counts):
    _sentence = _sentence_tuple[2]
    
    # This is where I think it's going wrong - I need to pass the output of each into the next
    # At the moment I'm simply passing in the ORIGINAL sentence to each function, rather than updating.
    _sentence = _replace_verbs(_sentence, _counts)
    _sentence = _replace_nouns(_sentence, _counts)
    _sentence = _replace_adjective_maybe(_sentence, _counts)
    _sentence = _replace_adjectives(_sentence, _counts)
    _sentence = _replace_names(_sentence, _counts)
    _sentence = _replace_an(_sentence, _counts)
    _sentence = _replace_random(_sentence)
    _sentence = _replace_capitalise(_sentence)
    
    return _sentence
    
    
def _replace_verbs(_sentence, _counts):
    # Lets find and replace all instances of #VERB
    
    if _sentence is not None:
        while _sentence.find('#VERB') != -1:
            _sentence = _sentence.replace('#VERB', str(_getverb(_counts)), 1)
            
            if _sentence.find('#VERB') == -1:
                return _sentence 
        return _sentence
    else:
        return _sentence
        
        
def _replace_nouns(_sentence, _counts):
    # Lets find and replace all instances of #NOUN
    
    if _sentence is not None:
        while _sentence.find('#NOUN') != -1:
            _sentence = _sentence.replace('#NOUN', str(_getnoun(_counts)), 1)
            
            if _sentence.find('#NOUN') == -1:
                return _sentence
            
        return _sentence
    else:
        return _sentence


def _replace_adjective_maybe(_sentence, _counts):
    
    _random_decision = random.randint(0, 1)
       
    if _sentence is not None:
        # Lets find and replace all instances of #ADJECTIVE_MAYBE
        while _sentence.find('#ADJECTIVE_MAYBE') != -1:
            
            if _random_decision % 2 == 0:
                _sentence = _sentence.replace('#ADJECTIVE_MAYBE', ' ' + str(_getadjective(_counts)), 1)
            elif _random_decision % 2 != 0:
                _sentence = _sentence.replace('#ADJECTIVE_MAYBE', '', 1)
            
            if _sentence.find('#ADJECTIVE_MAYBE') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence
    
    
def _replace_adjectives(_sentence, _counts):   
    
    if _sentence is not None:
        # Lets find and replace all instances of #ADJECTIVE
        while _sentence.find('#ADJECTIVE') != -1:
            _sentence = _sentence.replace('#ADJECTIVE', str(_getadjective(_counts)), 1)
            
            if _sentence.find('#ADJECTIVE') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence
    
    
def _replace_names(_sentence, _counts):
    
    if _sentence is not None:
        # Lets find and replace all instances of #NAME
        while _sentence.find('#NAME') != -1:
            _sentence = _sentence.replace('#NAME', str(_getname(_counts)), 1)
            
            if _sentence.find('#NAME') == -1:
                return _sentence
        return _sentence
    else:
        return _sentence


def _replace_an(_sentence, _counts):
    # Lets find and replace all instances of #AN
    # This is a little different, as this relies on the next word starting
    # with a vowel or a consonant.
    
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
    
    if _sentence is not None:
        # Lets find and replace all instances of #RANDOM
        while _sentence.find('#RANDOM') != -1:
            
            _random_index = _sentence.find('#RANDOM') 
            _start_index = _sentence.find('#RANDOM') + 8
            _end_index = _sentence.find(']')
            
            if _sentence.find('#RANDOM') is not None:
                
                _sub_list = _sentence[_start_index:_end_index].split(',')
                _choice = random.randint(1, int(_sub_list[0]))
                _sub_list[_choice]
            
            _to_be_replaced = _sentence[_random_index:_end_index + 1]
            _sentence = _sentence.replace(_to_be_replaced, _sub_list[_choice], 1)
                            
            if _sentence.find('#RANDOM') == -1:
                return _sentence
                  
        return _sentence
    else:
        return _sentence
    

def _replace_capitalise(_sentence):
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
