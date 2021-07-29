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
    if guess != usernamekey['Rav']:
        guess = input("Enter Guess: ")
        tries_count += 1
        print('Failed')
    elif guess == usernamekey['Rav']:
        print('Well Done')
        break


