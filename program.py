
def fizzbizz(n):
    for i in range(1,n+1):
        if i%15==0:
            print('fizzbizz')
        elif i % 5 == 0:
            print('bizz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i) 
n=int(input("Enter the number: "))
fizzbizz(n)


def palindrome(s):
    s=s.lower()
    if s==s[::-1]:
    	print(True)
    else:
    	print(False)
s=input('Enter the string: ')
palindrome(s)


def panagram(s):
    alphabet =('abcdefghijklmnopqrstuvwxyz')
    for i in alphabet:   
        if i not in s:
            return False
    return True
s=input("Enter the string: ")
print(panagram(s))

