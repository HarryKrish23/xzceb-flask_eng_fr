import unittest
import machinetranslation 
from translator import englishtofrench,frenchtoenglish

class Testtranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertEqual(englishtofrench("welcome"),"Bienvenue")
        self.assertNotEqual(englishtofrench("welcome"),"Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")    
        self.assertEqual(frenchtoenglish("Bienvenue"),"Welcome")
        self.assertNotEqual(englishtofrench("Bonjour"),"welcome")
        
unittest.main()