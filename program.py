
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


def palindrome(s):
    return s == s[::-1]



def panagram(s):
    alphabet =('abcdefghijklmnopqrstuvwxyz')
    for i in alphabet:   
        if i not in s:
            return False
    return True


def freq(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
def main():
    print(fizzbizz(int(input("Enter the number: "))))
    print(palindrome(input('Enter the string: ')))
    print(panagram(input('Enter the string: ')))
    print(freq(input('Enter the string: ')))

if __name__=="__main__":
    main()
