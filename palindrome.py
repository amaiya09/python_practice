wrd= str(input("Enter an input\n"))
rvs= wrd[::-1]
if wrd==rvs:
    print('Input is a palindrome')
else:
    print('Input is not a palindrome')