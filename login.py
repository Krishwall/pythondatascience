while True:
    username=input('enter username')
    password=input('enter password')
    if username=='admin'and password=='password':
        print('login succesful')
        break
    else :
        print('login failed')
        