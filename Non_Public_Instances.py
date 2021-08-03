from External_Instance import External
class abc():
    __a = input("Enter Value: ")
    def disp(self):
        ahf = input('Enter External Object Value: ')
        print(self.__a)
        print(ahf)
        # Preset variable from an external class
        print(External.Test)

# this allows the values to be shown from within the disp function as well as the values which are imported from the External Class & Method
obj=abc()
obj.disp()



