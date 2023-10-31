import unittest
from program import palindrome
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



if __name__ == "__main__":
    unittest.main()
