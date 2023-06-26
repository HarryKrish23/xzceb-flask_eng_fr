"""Module used for translation"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """This class does english to french translation"""
    frenchtext = MyMemoryTranslator("en", 'fr').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """This class does english to english translation"""
    englishtext = MyMemoryTranslator("fr","en").translate(frenchtext)
    return englishtext
