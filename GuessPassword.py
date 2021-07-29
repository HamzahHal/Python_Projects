usernamekey = {
    'Rav': 'Test',
    'Hamzah': 'Key',
    'Galvin': 'Polar'

}

guess = ''
tries_count = 0
tries_limit = 3
tries_out = False

while guess != usernamekey['Rav'] and not(tries_out):
    if tries_count < tries_limit:
        guess = input("Enter Guess: ")
        tries_count += 1
    else:
        tries_out = True

if tries_out:
    print('Out of tries')
else:
    print("You Win")


