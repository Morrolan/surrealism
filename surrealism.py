#!/usr/bin/env python

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
# Ravenblack.net is based on...

#############################################################################

__all__ = ['show_faults', 'show_sentences', 'getfault', 'getsentence', 'version',
           'sentence_test', 'fault_test', 'show_sentences', 'show_faults']

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

#  EXTERNAL METHODS BELOW

def version():
    """Returns the current version of the Surrealism module."""

    return pkg_resources.require('surrealism')[0].version


def showfaults():
    """
    This exists for backwards compatibility
    :return:
    """
    output = show_faults()
    return output


def show_faults():
    """
    Return all valid/active faults ordered by ID to allow the user to pick and choose.

    :return:  List of Tuples where the Tuple elements are:  (fault id, fault template)
    """
    cursor = CONN.cursor()

    query = "select fau_id, fault from surfaults where fau_is_valid = 'y' order by fau_id asc"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def showsentences():
    """
    This exists for backwards compatibility
    :return:
    """
    output = show_sentences()
    return output


def show_sentences():
    """
    Return all valid/active sentences ordered by ID to allow the user to pick and choose.

    :return:  Dict containing the sentence ID as the key and the sentence structure as the value.
    """
    cursor = CONN.cursor()

    query = "select sen_id, sentence from sursentences where sen_is_valid = 'y' order by sen_id asc"
    cursor.execute(query)
    result = cursor.fetchall()

    response_dict = {}

    for row in result:
        response_dict[row[0]] = row[1]

    return response_dict


def faulttest():
    """
    This exists for backwards compatibility
    :return:
    """
    output = fault_test()
    return output


def fault_test():
    """Returns 1 instance of each programming fault for testing purposes."""

    counts = __get_table_limits()
    max_num = counts['max_fau']
    counter = 0
    list_of_tuples = []
    fault_result = None

    while counter < max_num:
        counter += 1
        fault = __get_fault(counts, fault_id=counter)
        fault_id = fault[1]

        if fault[0] == 'n':
            fault_result = "Fault is DISABLED - ignoring..."

        if fault[0] == 'y':
            fault_result = __process_sentence(fault, counts)

        list_of_tuples.append((fault_id, fault_result))
    return list_of_tuples


def sentencetest():
    """
    This exists for backwards compatibility
    :return:
    """
    output = sentence_test()
    return output


def sentence_test():
    """Return 1 random version of each sentence to test sentence structure."""

    counts = __get_table_limits()
    max_num = counts['max_sen']
    counter = 0
    list_of_tuples = []
    sentence_result = None

    while counter < max_num:
        counter += 1
        sentence = __get_sentence(counts, sentence_id=counter)
        sentence_id = sentence[1]

        if sentence[0] == 'n':
            sentence_result = "Sentence is DISABLED - ignoring..."

        if sentence[0] == 'y':
            sentence_result = __process_sentence(sentence, counts)

        list_of_tuples.append((sentence_id, sentence_result))
    return list_of_tuples


def getfault(fault_id=None):
    output = get_fault(fault_id)
    return output


def get_fault(fault_id=None):
    """Retrieve a randomly-generated error message as a unicode string.
    
    :param fault_id:
        
        Allows you to optionally specify an integer representing the fault_id 
        from the database table.  This allows you to retrieve a specific fault
        each time, albeit with different keywords."""

    counts = __get_table_limits()
    result = None
    id_ = 0

    try:
        if isinstance(fault_id, int):
            id_ = fault_id
        elif isinstance(fault_id, float):
            print("""ValueError:  Floating point number detected.
                  Rounding number to 0 decimal places.""")
            id_ = round(fault_id)
        else:
            id_ = random.randint(1, counts['max_fau'])

    except ValueError:
        print("ValueError:  Incorrect parameter type detected.")

    if id_ <= counts['max_fau']:
        fault = __get_fault(counts, fault_id=id_)
    else:
        print("""ValueError:  Parameter integer is too high.
              Maximum permitted value is {0}.""".format(str(counts['max_fau'])))
        id_ = counts['max_fau']
        fault = __get_fault(counts, fault_id=id_)

    if fault is not None:
        while fault[0] == 'n':
            if id_ is not None:
                fault = __get_fault(counts, None)
            else:
                fault = __get_fault(counts, id_)
        if fault[0] == 'y':
            result = __process_sentence(fault, counts)
        return result
    else:
        print('ValueError: _fault cannot be None.')


def getsentence(sentence_id=None):
    output = get_sentence(sentence_id)
    return output


def get_sentence(sentence_id=None):
    """Retrieve a randomly-generated sentence as a unicode string.
    
    :param sentence_id:
        
        Allows you to optionally specify an integer representing the sentence_id
        from the database table.  This allows you to retrieve a specific
        sentence each time, albeit with different keywords."""

    counts = __get_table_limits()
    result = None
    id_ = 0

    try:
        if isinstance(sentence_id, int):
            id_ = sentence_id
        elif isinstance(sentence_id, float):
            print("""ValueError:  Floating point number detected.
                  Rounding number to 0 decimal places.""")
            id_ = round(sentence_id)
        else:
            id_ = random.randint(1, counts['max_sen'])

    except ValueError:
        print("ValueError:  Incorrect parameter type detected.")

    if id_ <= counts['max_sen']:
        sentence = __get_sentence(counts, sentence_id=id_)
    else:
        print("""ValueError:  Parameter integer is too high.
              Maximum permitted value is {0}.""".format(str(counts['max_sen'])))
        id_ = counts['max_sen']
        sentence = __get_sentence(counts, sentence_id=id_)

    if sentence is not None:
        while sentence[0] == 'n':
            if id_ is not None:
                # here we delibrately pass 'None' to __getsentence__ as it will
                sentence = __get_sentence(counts, None)
            else:
                sentence = __get_sentence(counts, id_)
        if sentence[0] == 'y':
            result = __process_sentence(sentence, counts)
        return result
    else:
        print('ValueError: _sentence cannot be None.')


#############################################################################

#  INTERNAL METHODS BELOW

def __get_fault(counts, fault_id=None):
    """Let's fetch a random fault that we then need to substitute bits of...
    :param counts:
    :param fault_id:
    """

    # First of all we need a cursor and a query to retrieve our ID's
    cursor = CONN.cursor()
    check_query = "select fau_id from surfaults"

    # Now we fetch the result of the query and save it into check_result
    cursor.execute(check_query)
    check_result = cursor.fetchall()

    # declare an empty list to be populated below
    id_list = []
    id_to_fetch = None

    for row in check_result:
        id_list.append(row[0])

    if fault_id is not None:
        if type(fault_id) is int:
            id_to_fetch = fault_id
    else:
        id_to_fetch = random.randint(1, counts['max_fau'])

        while id_to_fetch not in id_list:
            id_to_fetch = random.randint(1, counts['max_fau'])

    query = ("select * from surfaults where fau_id = {0}".format(id_to_fetch))
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result


def __get_sentence(counts, sentence_id=None):
    """Let's fetch a random sentence that we then need to substitute bits of...
    @
    :param counts:
    :param sentence_id:
    """

    # First of all we need a cursor and a query to retrieve our ID's
    cursor = CONN.cursor()
    check_query = "select sen_id from sursentences"

    # Now we fetch the result of the query and save it into check_result
    cursor.execute(check_query)
    check_result = cursor.fetchall()

    # declare an empty list to be populated below
    id_list = []
    id_to_fetch = None

    # Populate the id_list variable with all of the ID's we retrieved from the database query.
    for row in check_result:
        id_list.append(row[0])

    if sentence_id is not None:
        if type(sentence_id) is int:
            id_to_fetch = sentence_id
    else:
        id_to_fetch = random.randint(1, counts['max_sen'])

        while id_to_fetch not in id_list:
            id_to_fetch = random.randint(1, counts['max_sen'])

    query = ("select * from sursentences where sen_id = {0}".format(id_to_fetch))
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result


def __get_verb(counts):
    """Let's fetch a VERB
    :param counts:
    """

    cursor = CONN.cursor()
    check_query = "select verb_id from surverbs"

    cursor.execute(check_query)
    check_result = cursor.fetchall()

    id_list = []
    for row in check_result:
        id_list.append(row[0])

    rand = random.randint(1, counts['max_verb'])

    while rand not in id_list:
        rand = random.randint(1, counts['max_verb'])

    query = "select * from surverbs where verb_id = {0}".format(rand)
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result[1]


def __get_noun(counts):
    """Let's fetch a NOUN from the database...
    :param counts:
    """

    cursor = CONN.cursor()
    check_query = "select noun_id from surnouns"

    cursor.execute(check_query)
    check_result = cursor.fetchall()

    id_list = []
    for row in check_result:
        id_list.append(row[0])

    rand = random.randint(1, counts['max_nouns'])

    while rand not in id_list:
        rand = random.randint(1, counts['max_nouns'])

    query = "select * from surnouns where noun_id = {0}".format(rand)
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result[1]


def __get_adjective(counts):
    """Let's fetch an ADJECTIVE from the database...
    :param counts:
    """

    cursor = CONN.cursor()
    check_query = "select adj_id from suradjs"

    cursor.execute(check_query)
    check_result = cursor.fetchall()

    id_list = []
    for row in check_result:
        id_list.append(row[0])

    rand = random.randint(1, counts['max_adjectives'])

    while rand not in id_list:
        rand = random.randint(1, counts['max_adjectives'])

    query = "select * from suradjs where adj_id = {0}".format(rand)
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result[1]


def __get_name(counts):
    """Let's fetch a NAME from the database...
    :param counts:"""

    cursor = CONN.cursor()
    check_query = "select name_id from surnames"

    cursor.execute(check_query)
    check_result = cursor.fetchall()

    id_list = []
    for row in check_result:
        id_list.append(row[0])

    rand = random.randint(1, counts['max_names'])

    while rand not in id_list:
        rand = random.randint(1, counts['max_names'])

    query = "select * from surnames where name_id = {0}".format(rand)
    cursor.execute(query)
    result = cursor.fetchone()
    # cursor.close()

    return result[1]


def __get_table_limits():
    """Here we simply take a count of each of the database tables so we know our
    upper limits for our random number calls then return a dictionary of them 
    to the calling function..."""

    table_counts = {
        'max_adjectives': None,
        'max_names': None,
        'max_nouns': None,
        'max_sentences': None,
        'max_faults': None,
        'max_verbs': None
    }

    cursor = CONN.cursor()

    cursor.execute('SELECT count(*) FROM suradjs')
    table_counts['max_adjectives'] = cursor.fetchone()
    table_counts['max_adjectives'] = table_counts['max_adjectives'][0]

    cursor.execute('SELECT count(*) FROM surnames')
    table_counts['max_names'] = cursor.fetchone()
    table_counts['max_names'] = table_counts['max_names'][0]

    cursor.execute('SELECT count(*) FROM surnouns')
    table_counts['max_nouns'] = cursor.fetchone()
    table_counts['max_nouns'] = table_counts['max_nouns'][0]

    cursor.execute('SELECT count(*) FROM sursentences')
    table_counts['max_sen'] = cursor.fetchone()
    table_counts['max_sen'] = table_counts['max_sen'][0]

    cursor.execute('SELECT count(*) FROM surfaults')
    table_counts['max_fau'] = cursor.fetchone()
    table_counts['max_fau'] = table_counts['max_fau'][0]

    cursor.execute('SELECT count(*) FROM surverbs')
    table_counts['max_verb'] = cursor.fetchone()
    table_counts['max_verb'] = table_counts['max_verb'][0]

    return table_counts


def __process_sentence(sentence_tuple, counts):
    """pull the actual sentence from the tuple (tuple contains additional data such as ID)
    :param _sentence_tuple:
    :param counts:
    """

    sentence = sentence_tuple[2]

    # now we start replacing words one type at a time...
    sentence = __replace_verbs(sentence, counts)

    sentence = __replace_nouns(sentence, counts)

    sentence = ___replace_adjective_maybe(sentence, counts)

    sentence = __replace_adjective(sentence, counts)

    sentence = __replace_names(sentence, counts)

    # here we perform a check to see if we need to use A or AN depending on the 
    # first letter of the following word...
    sentence = __replace_an(sentence)

    # replace the new repeating segments
    sentence = __replace_repeat(sentence)

    # now we will read, choose and substitute each of the RANDOM sentence tuples
    sentence = __replace_random(sentence)

    # now we are going to choose whether to capitalize words/sentences or not
    sentence = __replace_capitalise(sentence)

    # here we will choose whether to capitalize all words in the sentence
    sentence = __replace_capall(sentence)

    # check for appropriate spaces in the correct places.
    sentence = __check_spaces(sentence)

    return sentence


def __replace_verbs(sentence, counts):
    """Lets find and replace all instances of #VERB
    :param _sentence:
    :param counts:
    """

    if sentence is not None:
        while sentence.find('#VERB') != -1:
            sentence = sentence.replace('#VERB', str(__get_verb(counts)), 1)

            if sentence.find('#VERB') == -1:
                return sentence
        return sentence
    else:
        return sentence


def __replace_nouns(sentence, counts):
    """Lets find and replace all instances of #NOUN
    :param _sentence:
    :param counts:
    """

    if sentence is not None:
        while sentence.find('#NOUN') != -1:
            sentence = sentence.replace('#NOUN', str(__get_noun(counts)), 1)

            if sentence.find('#NOUN') == -1:
                return sentence

        return sentence
    else:
        return sentence


def ___replace_adjective_maybe(sentence, counts):
    """Lets find and replace all instances of #ADJECTIVE_MAYBE
    :param _sentence:
    :param counts:
    """

    random_decision = random.randint(0, 1)

    if sentence is not None:

        while sentence.find('#ADJECTIVE_MAYBE') != -1:

            if random_decision % 2 == 0:
                sentence = sentence.replace('#ADJECTIVE_MAYBE',
                                              ' ' + str(__get_adjective(counts)), 1)
            elif random_decision % 2 != 0:
                sentence = sentence.replace('#ADJECTIVE_MAYBE', '', 1)

            if sentence.find('#ADJECTIVE_MAYBE') == -1:
                return sentence
        return sentence
    else:
        return sentence


def __replace_adjective(sentence, counts):
    """Lets find and replace all instances of #ADJECTIVE
    :param _sentence:
    :param counts:
    """

    if sentence is not None:

        while sentence.find('#ADJECTIVE') != -1:
            sentence = sentence.replace('#ADJECTIVE',
                                          str(__get_adjective(counts)), 1)

            if sentence.find('#ADJECTIVE') == -1:
                return sentence
        return sentence
    else:
        return sentence


def __replace_names(sentence, counts):
    """Lets find and replace all instances of #NAME
    :param _sentence:
    :param counts:
    """

    if sentence is not None:

        while sentence.find('#NAME') != -1:
            sentence = sentence.replace('#NAME', str(__get_name(counts)), 1)

            if sentence.find('#NAME') == -1:
                return sentence
        return sentence
    else:
        return sentence


def __replace_an(sentence):
    """Lets find and replace all instances of #AN
    This is a little different, as this depends on whether the next
    word starts with a vowel or a consonant.

    :param _sentence:
    """

    if sentence is not None:
        while sentence.find('#AN') != -1:
            an_index = sentence.find('#AN')

            if an_index > -1:
                an_index += 4

                if sentence[an_index] in 'aeiouAEIOU':
                    sentence = sentence.replace('#AN', str('an'), 1)
                else:
                    sentence = sentence.replace('#AN', str('a'), 1)

            if sentence.find('#AN') == -1:
                return sentence
        return sentence
    else:
        return sentence


def __replace_random(sentence):
    """Lets find and replace all instances of #RANDOM
    :param _sentence:
    """

    sub_list = None
    choice = None

    if sentence is not None:

        while sentence.find('#RANDOM') != -1:

            random_index = sentence.find('#RANDOM')
            start_index = sentence.find('#RANDOM') + 8
            end_index = sentence.find(']')

            if sentence.find('#RANDOM') is not None:
                sub_list = sentence[start_index:end_index].split(',')

                choice = random.randint(1, int(sub_list[0]))
                # _sub_list[_choice]

            to_be_replaced = sentence[random_index:end_index + 1]
            sentence = sentence.replace(to_be_replaced, sub_list[choice], 1)

            if sentence.find('#RANDOM') == -1:
                return sentence

        return sentence
    else:
        return sentence


def __replace_repeat(sentence):
    """
    Allows the use of repeating random-elements such as in the 'Ten green bottles' type sentences.

    :param sentence:
    """

    ######### USE SENTENCE_ID 47 for testing!

    repeat_dict = {}

    if sentence is not None:

        while sentence.find('#DEFINE_REPEAT') != -1:
            begin_index = sentence.find('#DEFINE_REPEAT')
            start_index = begin_index + 15
            end_index = sentence.find(']')

            if sentence.find('#DEFINE_REPEAT') is not None:
                sub_list = sentence[start_index:end_index].split(',')
                choice = sub_list[0]
                repeat_text = sub_list[1]
                repeat_dict[choice] = repeat_text
                sentence = sentence.replace(sentence[begin_index:end_index + 1], '', 1)

        while sentence.find('#REPEAT') != -1:
            if sentence.find('#REPEAT') is not None:
                repeat_begin_index = sentence.find('#REPEAT')
                repeat_start_index = repeat_begin_index + 8
                # by searching from repeat_index below we don't encounter dodgy bracket-matching errors.
                repeat_end_index = sentence.find(']', repeat_start_index)
                repeat_index = sentence[repeat_start_index:repeat_end_index]

                if repeat_index in repeat_dict:
                    sentence = sentence.replace(sentence[repeat_begin_index:repeat_end_index + 1],
                                                  str(repeat_dict[repeat_index]))

        if sentence.find('#REPEAT') == -1:
            return sentence
        return sentence
    else:
        return sentence


def __replace_capitalise(sentence):
    """here we replace all instances of #CAPITALISE and cap the next word.
    ############

    #NOTE:  Buggy as hell, as it doesn't account for words that are already
    #capitalized
    ############

    :param _sentence:
    """

    if sentence is not None:
        while sentence.find('#CAPITALISE') != -1:

            cap_index = _sentence.find('#CAPITALISE')
            part1 = sentence[:cap_index]
            part2 = sentence[cap_index + 12:cap_index + 13]
            part3 = sentence[cap_index + 13:]

            if part2 in "abcdefghijklmnopqrstuvwxyz":
                sentence = part1 + part2.capitalize() + part3
            else:
                sentence = part1 + part2 + part3

        if sentence.find('#CAPITALISE') == -1:
            return sentence
    else:
        return sentence


def __replace_capall(sentence):
    """here we replace all instances of #CAPALL and cap the entire sentence.
    Don't believe that CAPALL is buggy anymore as it forces all uppercase OK?

    :param _sentence:
        """

    # print "\nReplacing CAPITALISE:  "

    if sentence is not None:
        while sentence.find('#CAPALL') != -1:
            # _cap_index = _sentence.find('#CAPALL')
            sentence = sentence.upper()
            sentence = sentence.replace('#CAPALL ', '', 1)

        if sentence.find('#CAPALL') == -1:
            return sentence
    else:
        return sentence


def __check_spaces(sentence):
    """
    Here we check to see that we have the correct number of spaces in the correct locations.

    :param _sentence:
    :return:
    """
    # We have to run the process multiple times:
    #   Once to search for all spaces, and check if there are adjoining spaces;
    #   The second time to check for 2 spaces after sentence-ending characters such as . and ! and ?

    if sentence is not None:

        words = sentence.split()

        new_sentence = ''

        for (i, word) in enumerate(words):

            if word[-1] in set('.!?'):
                word += ' '
            new_word = ''.join(word)
            new_sentence += ' ' + new_word

        # remove any trailing whitespace
        new_sentence = new_sentence.strip()

    return new_sentence
