name=input('Please enter your name')
print()
print('Welcome, ',name,', to the Quadratic Formula Calculator',sep=(''))
input('Press ENTER to continue')
print()
a=float(input('Please enter the value of a:'))
b=float(input('Please enter the value of b:'))
c=float(input('Please enter the value of c:'))
dd = (b**2) - (4*a*c)
d = dd**0.5
solo=(-b-(d))/(2*a)
solt=(-b+(d))/(2*a)
print()
print('Calculating all possibilities...')
print()
print('''The possible solutions are either
    '''  ,format(solo,'10.2f'),'''
            or
    ''',format(solt,'10.2f'))
