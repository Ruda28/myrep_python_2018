ADMIN_USERNAME = 'Piotr'
name=input('Podaj imie')

name_capitalized=name.lower().capitalize()

if name_capitalized==ADMIN_USERNAME:
    print('hey',name)
else:
    print ('hey poklikasz?')