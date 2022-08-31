names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')

input = input('Esm ro Vared Kon:\n')
A = int(len(names) / 2)

if input in names[0:A:1] :
    print(f'{input} Jozve Shagerd Avalast!')
elif input in names[A::1] :
    print(f'{input} Jozve Shagerd Tanbalast!')
else:
    print(f'{input} nadarim!')
