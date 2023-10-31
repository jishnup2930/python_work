import unittest
from program import palindrome
from program import freq

class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        sentence = "abba"
        self.assertTrue(palindrome(sentence))

    def testIsNotPalindrome(self):
        sentence = "not palindrome"
        self.assertFalse(palindrome(sentence))
    
    def testNullInput(self):
        ret = palindrome("")
        self.assertTrue(ret)

    def testSpecialcharactersInput(self):
        special_char='!@#$%^&.\;/<>,*'
        self.assertFalse(palindrome(special_char))


class TestFrequency(unittest.TestCase):
    def testIsFreq(self):
        sentence = "jishnu"
        self.assertTrue(freq(sentence))
    
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)

    def testSpecialcharactersInput(self):
        special_char='!@#$%^&.\;/<>,*'
        self.assertTrue(freq(special_char))

    def testNumberInput(self):
        numbers='1234567890'
        self.assertTrue(freq(numbers))



if __name__ == "__main__":
    unittest.main()
