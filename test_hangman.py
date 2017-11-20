import unittest, ps3_hangman

class TestHangman(unittest.TestCase):
    def test_is_word_guessed(self):
        secretWord = "bonjour"
        true_lettersGuessed = ["b", "o", "n", "j", "o", "u", "r"]
        false_lettersGuessed = ["b", "o", "n", "j"]
        self.assertTrue(ps3_hangman.isWordGuessed(secretWord, true_lettersGuessed))
        self.assertFalse(ps3_hangman.isWordGuessed(secretWord, false_lettersGuessed))

    def test_getguessedword(self):
        secretWord = "bonjour"
        lettersGuessed = ["b", "o", "r"]
        guessed_word = ps3_hangman.getGuessedWord(secretWord, lettersGuessed)
        self.assertEqual(guessed_word, "bo__o_r")

    def test_getAvailableLetters(self):
        lettersGuessed = ["b", "o", "r"]
        self.assertEqual(ps3_hangman.getAvailableLetters(lettersGuessed), "acdefghijklmnpqstuvwxyz")

