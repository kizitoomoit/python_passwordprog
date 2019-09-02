import sys

attempts = 3
while attempts > 0:
    #print('Enter password')
    print('*' *30)
    print('YOU HAVE '+ str(attempts) +' ATTEMPTS!')
    password = input('Enter password: ')
    print('*' *30)
    #attempts = attempts + 1
    if password == 'home':
        sys.exit('ACCESS GRANTED!')
    else:
        print('Wrong password! try again!')
        attempts = attempts - 1
        while attempts == 0:
            sys.exit('ACCOUNT BLOCKED!')
    
