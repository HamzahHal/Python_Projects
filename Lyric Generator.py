
Songs = {

    '1': 'Baby by Bieber',
    '2': 'Hotline Bling by Drake',
    '3': 'Flawless by Beyonce',
    '4': 'Fall by Eminem'
}

Choice = ""
Selected = False
print(" 1: 'Baby by Bieber',")
print(" 2: 'Hotline Bling by Drake',")
print(" 3: 'Flawless by Beyonce',")
print(" 4: 'Fall by Eminem'")

while Choice != Songs.items() and not(Selected):
    # if Selected == False:
    Choice = input('Enter Song: ')

if Choice == Songs.keys([1]):
    print("Baby by Bieber")
    Selected = True#
elif Choice == Songs['Hotline Bling by Drake']:
    print("Hotline Bling")
    Selected = True
elif Choice == Songs['Flawless by Beyonce']:
    print("Flawless tings")
    Selected = True
elif Choice == Songs['Fall by Eminem']:
    print("Fall bitches with stitches")
    Selected = True


