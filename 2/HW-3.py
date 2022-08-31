A = float(input('zel-e aval ro vared kon: '))
B = float(input('zel-e dovom ro vared kon: '))
C = float(input('zel-e sevom ro vared kon: '))

if A+B>C and A+C>B and B+C>A:
    if  A**2+B**2==C**2  or  A**2+C**2==B**2  or  C**2+B**2==A**2 :
        print('Mosalas Ghaemolzavieh Hast.')
    else:
        print('Mosalas Ghaemolzavieh Nist!')
else:
    print('Ba Ina Nemishe Mosalas Sakht.')
