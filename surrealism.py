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

__ALL__ = ['test', 'getfault', 'getsentence', 'Surrealism']


# IMPORTS ###################################################################



# PARTICULAR IMPORTS ########################################################

import sqlite3
import random

# CONSTANTS #################################################################

CONN = sqlite3.connect('surrealism.sqlite')

# VARIABLES #################################################################



# CLASSES ###################################################################

class Surrealism(object):
     
    def __init__(self):
        pass

#############################################################################

#  EXTERNAL METHODS BELOW

    def test(self):
        pass
    
    
    def getfault(self):
        _counts = self._gettablelimits()
        _sentence = self._getfault(_counts)
        #print _sentence
        
        while _sentence[0] == 'n':
            #print _sentence
            _sentence = self._getfault(_counts)
        
        if _sentence[0] == 'y':
            #print _sentence
            self._process_sentence(_sentence, _counts)
        
        return _sentence 
        
    
    def getsentence(self):
        _counts = self._gettablelimits()
        _sentence = self._getsentence(_counts)
        #print _sentence
        
        while _sentence[0] == 'n':
            #print _sentence
            _sentence = self._getsentence(_counts)
        
        if _sentence[0] == 'y':
            #print _sentence
            _result = self._process_sentence(_sentence, _counts)
        
        return _result 
        
        
        
#############################################################################

#  INTERNAL METHODS BELOW

    def _getsentence(self, _counts):
        # Let's fetch the sentence that we then need to substitute bits of!
        cursor = CONN.cursor()
        #_counts = self._gettablelimits()
        _rand = random.randint(1,_counts['sen_count'])
        _query = """select * from sursentences where sen_id = {0}""".format(_rand)
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result
        return _result
        
        
    def _getfault(self, _counts):
        # Let's fetch the sentence that we then need to substitute bits of!
        cursor = CONN.cursor()
        _counts = self._gettablelimits()
        _query = """select * from sursentences where sen_id = 46"""
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result
        return _result
    
    
    def _getverb(self, _counts):
        # Let's fetch a VERB
        cursor = CONN.cursor()
        #_counts = self._gettablelimits()
        _rand = random.randint(1,_counts['verb_count'])
        _query = """select * from surverbs where verb_id = {0}""".format(_rand)
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result[1]
        return _result[1]
    
    
    def _getnoun(self, _counts):
        # Let's fetch a NOUN
        cursor = CONN.cursor()
        #_counts = self._gettablelimits()
        _rand = random.randint(1,_counts['noun_count'])
        _query = """select * from surnouns where noun_id = {0}""".format(_rand)
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result[1]
        return _result[1]
        
        
    def _getadjective(self, _counts):
         # Let's fetch an ADJECTIVE
        cursor = CONN.cursor()
        #_counts = self._gettablelimits()
        _rand = random.randint(1,_counts['adj_count'])
        _query = """select * from suradjs where adj_id = {0}""".format(_rand)
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result[1]
        return _result[1]
        
    
    def _getname(self, _counts):
        # Let's fetch a NAME
        cursor = CONN.cursor()
        #_counts = self._gettablelimits()
        _rand = random.randint(1,_counts['name_count'])
        _query = """select * from surnames where name_id = {0}""".format(_rand)
        cursor.execute(_query)
        _result = cursor.fetchone()
        #print _result[1]
        return _result[1]
    
    
    def _gettablelimits(self):
        
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
  
    
    def _process_sentence(self, _sentence_tuple, _counts):
        _sentence = _sentence_tuple[2]
        
        #print "\n\nSentence ID:  {0}".format(str(_sentence_tuple[1]))
        #print "\nVanilla sentence:"
        #print _sentence
        
        # This is where I think it's going wrong - I need to pass the output of each into the next
        # At the moment I'm simply passing in the ORIGINAL sentence to each function, rather than updating.
        _sentence = self._replace_verbs(_sentence, _counts)
        _sentence = self._replace_nouns(_sentence, _counts)
        _sentence = self._replace_adjective_maybe(_sentence, _counts)
        _sentence = self._replace_adjectives(_sentence, _counts)
        _sentence = self._replace_names(_sentence, _counts)
        _sentence = self._replace_an(_sentence, _counts)
        _sentence = self._replace_random(_sentence)
        _sentence = self._replace_capitalise(_sentence)
        #print _sentence
        
        return _sentence
        
        
    def _replace_verbs(self, _sentence, _counts):
        # Lets find and replace all instances of #VERB
        #print "\nReplacing VERBS:  "
        
        if _sentence is not None:
            while _sentence.find('#VERB') != -1:
                _sentence = _sentence.replace('#VERB', str(self._getverb(_counts)), 1)
                #print _sentence
                
                if _sentence.find('#VERB') == -1:
                    return _sentence
                
            return _sentence
        else:
            return _sentence
            
            
    def _replace_nouns(self, _sentence, _counts):
        # Lets find and replace all instances of #NOUN
        #print "\nReplacing NOUNS:  "
        
        #print "1"
        
        if _sentence is not None:
            while _sentence.find('#NOUN') != -1:
                _sentence = _sentence.replace('#NOUN', str(self._getnoun(_counts)), 1)
                #print _sentence
                
                if _sentence.find('#NOUN') == -1:
                    return _sentence
                
            return _sentence
        else:
            #print _sentence
            return _sentence
    
    
    def _replace_adjective_maybe(self, _sentence, _counts):
        
        #print "\nReplacing ADJECTIVE_MAYBE:  "
        _random_decision = random.randint(0, 1)
           
        if _sentence is not None:
            # Lets find and replace all instances of #ADJECTIVE_MAYBE
            while _sentence.find('#ADJECTIVE_MAYBE') != -1:
                
                if _random_decision % 2 == 0:
                    _sentence = _sentence.replace('#ADJECTIVE_MAYBE', ' ' + str(self._getadjective(_counts)), 1)
                   # print 'REPLACE ADJ: {0}'.format(_sentence)
                    #del _random_decision
                    #print _sentence
                elif _random_decision % 2 != 0:
                    _sentence = _sentence.replace('#ADJECTIVE_MAYBE', '', 1)
                    #print 'DON\'T REPLACE ADJ: {0}'.format(_sentence)
                    #del _random_decision
                    #print _sentence
                
                if _sentence.find('#ADJECTIVE_MAYBE') == -1:
                    return _sentence
           
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence
        
        
    def _replace_adjectives(self, _sentence, _counts):   
        
        #print "\nReplacing ADJECTIVES:  "
        
        if _sentence is not None:
            # Lets find and replace all instances of #ADJECTIVE
            while _sentence.find('#ADJECTIVE') != -1:
                _sentence = _sentence.replace('#ADJECTIVE', str(self._getadjective(_counts)), 1)
                #print _sentence
                
                if _sentence.find('#ADJECTIVE') == -1:
                    return _sentence
            
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence
        
        
    def _replace_names(self, _sentence, _counts):
        #print "\nReplacing NAMES:  "
        
        if _sentence is not None:
            # Lets find and replace all instances of #NAME
            while _sentence.find('#NAME') != -1:
                _sentence = _sentence.replace('#NAME', str(self._getname(_counts)), 1)
                #print _sentence
                
                if _sentence.find('#NAME') == -1:
                    return _sentence
            
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence


    def _replace_an(self, _sentence, _counts):
        #print "\nReplacing AN:  "
        # Lets find and replace all instances of #AN
        # This is a little different, as this relies on the next word starting
        # with a vowel or a consonant.
        
        if _sentence is not None:
            while _sentence.find('#AN') != -1:
                _an_index = _sentence.find('#AN')
                #print _an_index
                
                if _an_index > -1:
                    _an_index = _an_index + 4
                    #print _an_index
                    
                    if _sentence[_an_index] in 'aeiouAEIOU':
                        _sentence = _sentence.replace('#AN', str('an'), 1)
                    else:
                        _sentence = _sentence.replace('#AN', str('a'), 1)
                    
                
                if _sentence.find('#AN') == -1:
                    #print _sentence
                    return _sentence
                    
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence
    
    
    def _replace_random(self, _sentence):
        #print "\nReplacing RANDOM:  "
        
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
                #print _to_be_replaced
                
                _sentence = _sentence.replace(_to_be_replaced, _sub_list[_choice], 1)
                #print str(_sentence)
                                
                if _sentence.find('#RANDOM') == -1:
                    #print _sentence
                    return _sentence
                      
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence
    

    def _replace_capitalise(self, _sentence):
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
            
            #print _sentence
            return _sentence
        else:
            #print _sentence
            return _sentence


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
