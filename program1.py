import unittest
from program import palindrome,freq

class TestPalindrome(unittest.TestCase):
    def test_IsPalindrome(self):
        sentence = "abba"
        self.assertTrue(palindrome(sentence))

    def test_IsNotPalindrome(self):
        sentence = "not palindrome"
        self.assertFalse(palindrome(sentence))
    
    def test_NullInput(self):
        ret = palindrome("")
        self.assertTrue(ret)

    def test_SpecialcharactersInput(self):
        special_char='!@#$%^&.\;/<>,*'
        self.assertFalse(palindrome(special_char))


class TestFrequency(unittest.TestCase):
    def testIsFreq(self):
        sentence = "jishnu ji"
        d={'j':2,'i':2,'s':1,'h':1,'n':1,'u':1}
        self.assertTrue(freq(sentence))
    
    def testNullInput(self):
        ret = freq("")
        self.assertFalse(ret)

    def testSpecialcharactersInput(self):
        special_char='!@#'
        d={'!':1,'@':1,'#':1}
        self.assertTrue(freq(special_char))

    def testNumberInput(self):
        numbers='1234567890'
        d={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,0:1}
        self.assertTrue(freq(numbers))



if __name__ == "__main__":
    unittest.main()
