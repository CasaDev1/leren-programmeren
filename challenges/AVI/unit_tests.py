from functies import *


# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfCharacters(ALLOWED_IN_WORD) == 64:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
if getNumberOfCharacters('aapw') == 4:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog wat extra testen voor getNumberOfCharacters

# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).
if getNumberOfSentences("hallo ik ben nadir. ik ben 16 jaar oud.") == 2:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")


# test 3: getNumberOfWords
print(getNumberOfWords(getText('data\difficult1.txt')))
if getNumberOfWords(getText('data\difficult1.txt')) == 82:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('data\easy1.txt')) == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).
if getNumberOfWords("hallo doei hoi") == 3:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")