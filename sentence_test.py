import surrealism


def test():
    
    _counts = surrealism._gettablelimits()
    
    max_num = 98
    
    a = 0
    
    while a < max_num: 
    
        
        a = a + 1
        
        print "\nSentence ID:  " + str(a)
        _sentence = surrealism._get_sentence_by_id(a)
        
        if _sentence[0] == 'n':
            print "Sentence is DISABLED - ignoring..."
        
        if _sentence[0] == 'y':
            _result = surrealism._process_sentence(_sentence, _counts)
            print _result
    
test()