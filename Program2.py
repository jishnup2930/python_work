def palindrome(s):
    s=s.lower()
    if s==s[::-1]:
    	print(True)
    else:
    	print(False)
s=input('Enter the string: ')
palindrome(s)
