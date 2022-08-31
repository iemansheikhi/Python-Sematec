# name = input('esmet chie?\n')
#
# if name != 'ali':
#     print(f'salam {name}.')



# name = input('esmet chie?\n')
# age = int(input('esmet chie?\n'))
#
# if age >= 18 :
#     print(f'salam {name} Jaan.')
#
# if age < 18 :
#     print(f'salam {name} koochooloo.')


# num1 = float(input('zavieh aval ro vared kon: '))
# num2 = float(input('zavieh dovom ro vared kon: '))
# num3 = float(input('zavieh sevom ro vared kon: '))
#
# if num1 + num2 + num3 == 180 :
#     print('mishe mosalas sakht.')
# else :
#     print('nemishe!')



# name = input('esmet chie? \n')
#
# if name != 'Ali' :
#     if name == 'shahab' :
#         print('shahab taghalob naresoon')
#     else:
#         print(f'salaaamm {name}.')



# age = float(input('chand salete? '))
#
# if age > 18 :
#     print('bye')
# elif age < 12 :
#     print('bye')
# else:
#     print('befarmaeed dakhel!')


# age = float(input('chand salete? '))
#
# if age < 18 and age > 12 :
#     print('befarmaeed')
# else :
#     print('bye')


# num1 = float(input('adade aval ro vared kon: '))
# num2 = float(input('adade dovom ro vared kon: '))
# num3 = float(input('adade sevom ro vared kon: '))
#
# if num1 > num2 and num1 > num3 :
#     print(f'{num1} bozorgtar az hamst!')
# elif num2 > num1 and num2 > num3 :
#     print(f'{num2} bozorgtar az hamst!')
# elif num3 > num2 and num3 > num1 :
#     print(f'{num3} bozorgtar az hamst!')
# else:
#     print('barabarand!')



########## num1 = float(input('zel-e aval ro vared kon: '))
# num2 = float(input('zel-e dovom ro vared kon: '))
# num3 = float(input('zel-e sevom ro vared kon: '))
#
# if num1 == num2 and num1 != num3 :
#     print('okeye!')
# elif num2 == num3 and num2 != num1 :
#     print('okeye!')
# elif num1 == num3 and num1 != num2 :
#     print('okeye!')
# else:
#     print('2 zel-e mosavi varde nakardi!')




# A = float(input('zel-e aval ro vared kon: '))
# B = float(input('zel-e dovom ro vared kon: '))
# C = float(input('zel-e sevom ro vared kon: '))
#
# if A+B>C and A+C>B and B+C>A:
#     if A==B or A==C or B==C :
#         print('motasaviol saghein hast.')
#     elif A==B and B==C :
#         print('motasaviol azlaast ke baz ham yek no motasaviol sagheine.')
# else:
#     print('ba ina nemishe mosalas sakht.')



# num = int(input('Yek Adad Vared Kon: '))
#
# if (num % 2) == 0 and (num % 3) == 0 :
#     print('in adad bar 6 bakhsh pazir ast.')
# else:
#     print('bar 6 bakhsh pazir nist!')




# A = float(input('zel-e aval ro vared kon: '))
# B = float(input('zel-e dovom ro vared kon: '))
# C = float(input('zel-e sevom ro vared kon: '))
#
# if A+B>C and A+C>B and B+C>A:
#     if  A**2+B**2==C**2  or  A**2+C**2==B**2  or  C**2+B**2==A**2 :
#         print('Mosalas Ghaemolzavieh Hast.')
#     else:
#         print('Mosalas Ghaemolzavieh Nist!')
# else:
#     print('Ba Ina Nemishe Mosalas Sakht.')


#
# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# A = int(len(names) / 2)
# print(names[A::1])


# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# input = input('Esm ro Vared Kon:\n')
# A = int(len(names) / 2)
#
# if input in names[0:A:1] :
#     print(f'{input} Jozve Shagerd Avalast!')
# elif input in names[A::1] :
#     print(f'{input} Jozve Shagerd Tanbalast!')
# else:
#     print(f'{input} nadarim!')






# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# JAYGAH = input('Jaye Morede Nazar ro Vared Kon:\n "Aval" ya "Akhar"? ')
# TEDAD = int(input('Tedade Morede Nazar ro Vared Kon: '))
#
# if JAYGAH == 'Aval' :
#     if 0<TEDAD<13 :
#         print(names[0:TEDAD:1])
#     else:
#         print('adad voroudi bayad beine 1 ta 12 bashe.')
# elif JAYGAH == 'Akhar' :
#     if 0<TEDAD<13 :
#         print(names[-1:-(TEDAD+1):-1])
#     else:
#         print('adad voroudi bayad beine 1 ta 12 bashe.')
# else:
#     print('"Aval" ya "Akhar" ra dorost vared nakardid!')




# https://paste.ubuntu.ir/jnunl
# https://paste.ubuntu.ir/tvpxp
# https://paste.ubuntu.ir/smidk
# https://paste.ubuntu.ir/qamgf
# https://paste.ubuntu.ir/mvgek
# https://paste.ubuntu.ir/fzgxw



a = int(input('first:'))
b = int(input('second:'))
c = int(input('third:'))

d=a+b+c

if a+b >c and a+c>b and b+c>a:
    if a == b:
        print('mosalas motasaviol saqein hast')
    elif a==c:
        print('mosalas motasaviol saqein hast')
    elif b==c:
        print('mosalas motasaviol saqein hast')
    elif b==c and c==a:
        print('mosalas motasaviol azla hast')
else :
    print('dont mosalas')
