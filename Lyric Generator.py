
Songs = {

    'Baby by Bieber': '1',
}

Choice = ""
Selected = False
print(" 1: 'Baby by Bieber',")

while Choice != Songs['Baby by Bieber'] and not(Selected):
    Choice = input('Enter Song: ')

if Choice == Songs['Baby by Bieber']:
    print("Baby, Baby, Baby, Ooooo ")
    Selected = True


