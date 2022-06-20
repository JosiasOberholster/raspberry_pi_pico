user_name = input('what is your name?')
while True:
    try:
        user_age = int(input('what is your age?'))
        if isinstance(user_age, int):
            print('your name is:',user_name)
            if user_age > 5:
                print('you are older than 5')
            else:
                print('you are younger than 5')
            break
    except:
        print('your age must be a number')



