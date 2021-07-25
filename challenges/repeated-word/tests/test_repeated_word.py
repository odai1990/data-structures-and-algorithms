from repeated_word import __version__
from repeated_word.repeated_word import RepeatedWord
from repeated_word.hashtable import HashTable

def test_version():
    assert __version__ == '0.1.0'


def test_without_spical_char():
    ht = RepeatedWord(1024)
    assert ht.repeated_word('Once upon a time, there was a brave princess who...')=='a'

def test_without_spical_char_and_have_many_repeted_words():
    ht = RepeatedWord(1024)
    assert ht.repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...')=='it'

def test_with_spical_char():
    ht = RepeatedWord(1024)
    assert ht.repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')=='summer'


def test_with_no_repated():
    ht = RepeatedWord(1024)
    assert ht.repeated_word('It was a queer,')==None


