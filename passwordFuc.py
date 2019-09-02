def password():
    import sys

    attempts = 3
    while attempts > 0:
        print('YOU HAVE ' + str(attempts) + ' REMAINING!')
        password = input('Enter password: ')
        if password == 'home':
            sys.exit('ACCESS GRANTED!')
        else:
            print('WRONG PASSWORD! TRY AGAIN')
            attempts = attempts - 1
            while attempts == 0:
                sys.exit('ACCOUNT BLOCKED!')


password()

