x=input('Enter a number')
x=int(x)
a= range(2,x)
for b in a:
    if x%b == 0:
        print(b)
print('Done')