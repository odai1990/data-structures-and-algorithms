from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_version():
    assert __version__ == '0.1.0'



def test_one():
    '''
    Testing string -->  {}
    '''
    assert multi_bracket_validation('{}')==True 



def test_two():
    '''
    Testing string -->  {}(){}
    '''
    assert multi_bracket_validation('{}(){}')==True 



def test_three():
    '''
    Testing string -->  ()[[Extra Characters]]
    '''
    assert multi_bracket_validation('()[[Extra Characters]]')==True 



def test_four():
    '''
    Testing string -->  (){}[[]]
    '''
    assert multi_bracket_validation('(){}[[]]')==True 



def test_five():
    '''
    Testing string -->  {}{Code}[Fellows](())
    '''
    assert multi_bracket_validation('{}{Code}[Fellows](())')==True 




def test_six():
    '''
    Testing string -->  [({}]
    '''
    assert multi_bracket_validation('[({}]')==False 




def test_seven():
    '''
    Testing string -->  (](
    '''
    assert multi_bracket_validation('(](')==False 




def test_eight():
    '''
    Testing string -->  {(})
    '''
    assert multi_bracket_validation('{(})')==False 




def test_nine():
    '''
    Testing string -->  {
    '''
    
    assert multi_bracket_validation('{')==False 
