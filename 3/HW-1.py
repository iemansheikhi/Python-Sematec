names = ['Ahmadreza', 'Faeze', 'Farnaz', 'Forough', 'Iman', 'Mina', 'Moein',\
'Mohammad', 'Mona', 'Parsa', 'Roghaye', 'Roxana', 'Sepide Ba', 'Sepide Bi',\
'Omid', 'Sepehr', 'Shahab', 'Shayan', 'Zohre', 'Vahid', 'Sogand']

name1 = input('esm aval ro vared kon: ')
if name1 in names:
    index1 = names.index(name1)
    name2 = input('esm dovom ro vared kon: ')
    if name1 != name2:
        if name2 in names:
            index2 = names.index(name2)
            if index1 < index2 :
                print(names[:index1] + names[index2+1:])
            else:
                index1 = index2
                index2 = names.index(name1)
                print(names[:index1] + names[index2+1:])
        else:
            print(f'"{name2}" too list nist!')
    else:
        print('2 ta esm nabayad yeki bashan!')
else:
    print(f'"{name1}" too list nist!')
