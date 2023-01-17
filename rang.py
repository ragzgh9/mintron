down = 0
up = 100
for i in range(1,10):
    guessed_age = int((up + down) / 2)
    answer = input('Are You '+str(guessed_age)+' Years Old' )
    if answer == 'correct':
        print("Nice")
        break
    elif answer == 'less':
         up = guessed_age
    elif answer == 'More':
        down = guessed_age
    else:
        print('Wrong Answer!')