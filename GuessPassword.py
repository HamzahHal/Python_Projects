usernamekey = {
    'Rav': 'Test',
    'Hamzah': 'Key',
    'Galvin': 'Polar'

}

guess = ''
tries_count = 0
tries_limit = 1
tries_out = False

while guess in usernamekey['Rav']:
    guess = input("Enter Guess: ")
    if guess != usernamekey['Rav']:
        tries_count += 1
        if tries_count > tries_limit:
            tries_out = True
            print('Failed')
    elif guess == usernamekey['Rav']:
        print('Well Done')
        break


