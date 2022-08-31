A = float(input('zel-e aval ro vared kon: '))
B = float(input('zel-e dovom ro vared kon: '))
C = float(input('zel-e sevom ro vared kon: '))

if A+B>C and A+C>B and B+C>A:
    if A==B or A==C or B==C :
        print('motasaviol saghein hast.')
    elif A==B and B==C :
        print('motasaviol azlaast ke khodesh yek now motasaviol sagheine!')
else:
    print('ba ina nemishe mosalas sakht.')
