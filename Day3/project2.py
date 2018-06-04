dane = input('podaj liczbe: ')
if dane.isdigit():
    dane=int(dane)
    if dane % 2:
        print('nieparzysta')
    else:
        print('parzysta')
else:
    print('musisz podac liczbe')
