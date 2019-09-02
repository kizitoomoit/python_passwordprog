import sys

while True:
    answer = input('Do you want to login?')
    if answer== 'yes':
        from passwordFuc.py import password
        password()
    else:
        sys.exit('GOODBYE!')

