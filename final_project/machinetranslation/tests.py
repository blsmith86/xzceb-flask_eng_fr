import unittest

from  translator import english_to_french, french_to_english


class TestE2FTranslator(unittest.TestCase):
    '''
        Class: TestE2FTranslator
        Purpose: Test class that verifies the englishToFrench
        translator method is working correctly.

    '''


    def test1(self):
        '''
            Purpose: Tests that a string in English gets translated
            to French text.
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        '''
             Purpose: Tests for Null input
        '''
        self.assertNotEqual(english_to_french(""), "Bonjour")

    

class TestF2ETranslator(unittest.TestCase):
    '''
        Class: TestF2ETranslator

        Purpose: Test class that verifies the frenchtoEnglish
        method translator is working correctly.
    '''

    def test1(self):
        '''
            Purpose: Tests that a string in French gets translated
            to English text.
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        '''
            Purpose:Tests For Null input
        '''
        self.assertNotEqual(french_to_english(""), "Bonjour")

unittest.main()
