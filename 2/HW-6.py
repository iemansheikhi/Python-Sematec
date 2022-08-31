names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')

JAYGAH = input('Jaye Morede Nazar ro Vared Kon:\n "Aval" ya "Akhar"? ')
TEDAD = int(input('Tedade Morede Nazar ro Vared Kon: '))

if JAYGAH == 'Aval' :
    if 0<TEDAD<13 :
        print(names[0:TEDAD:1])
    else:
        print('adad voroudi bayad beine 1 ta 12 bashe.')
elif JAYGAH == 'Akhar' :
    if 0<TEDAD<13 :
        print(names[-1:-(TEDAD+1):-1])
    else:
        print('adad voroudi bayad beine 1 ta 12 bashe.')
else:
    print('"Aval" ya "Akhar" ra dorost vared nakardid!')
