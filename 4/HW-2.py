#2-1
# def divisible(num):
#
#     if (num % 2) == 0 and (num % 3) == 0 :
#         print('in adad bar 6 bakhsh pazir ast.')
#     else:
#         print('bar 6 bakhsh pazir nist!')
#
# divisible(5)


# 2-2
# def ghaem(zel1, zel2, zel3):
#
#     if zel1+zel2>zel3 and zel1+zel3>zel2 and zel2+zel3>zel1:
#         if  zel1**2+zel2**2==zel3**2  or  zel1**2+zel3**2==zel2**2  or  zel3**2+zel2**2==zel1**2 :
#             print('Mosalas Ghaemolzavieh Hast.')
#         else:
#             print('Mosalas Ghaemolzavieh Nist!')
#     else:
#         print('Ba Ina Nemishe Mosalas Sakht.')
#
# ghaem(3,5,7)



# 2-3
# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# def namesfunc(some_tuple):
#
#     A = int(len(some_tuple) / 2)
#     print(names[A::])
#
# namesfunc(names)



#2-4

# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# def TaeenSath(some_tuple, some_name):
#
#     A = int(len(some_tuple) / 2)
#     if some_name in some_tuple[0:A] :
#         print(f'{some_name} Jozve Shagerd Avalast!')
#     elif some_name in some_tuple[A:] :
#         print(f'{some_name} Jozve Shagerd Tanbalast!')
#     else:
#         print(f'{some_name} nadarim!')
#
# TaeenSath(names, 'pegah')



#2-5

# names = ('iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti')
#
# def ListMaker(JAYGAH, TEDAD):
#
#     if JAYGAH == 'Aval' :
#         if 0<TEDAD<13 :
#             print(names[0:TEDAD:1])
#         else:
#             print('adad voroudi bayad beine 1 ta 12 bashe.')
#     elif JAYGAH == 'Akhar' :
#         if 0<TEDAD<13 :
#             print(names[int(len(names))-TEDAD:])
#         else:
#             print('adad voroudi bayad beine 1 ta 12 bashe.')
#     else:
#         print('"Aval" ya "Akhar" ra dorost vared nakardid!')
#
# ListMaker('Akhar', 3)



#3-1

# names = ['Ahmadreza', 'Faeze', 'Farnaz', 'Forough', 'Iman', 'Mina', 'Moein',\
# 'Mohammad', 'Mona', 'Parsa', 'Roghaye', 'Roxana', 'Sepide Ba', 'Sepide Bi',\
# 'Omid', 'Sepehr', 'Shahab', 'Shayan', 'Zohre', 'Vahid', 'Sogand']
#
# def ListMaker(some_list, name1, name2):
#
#     if name1 in some_list:
#         index1 = some_list.index(name1)
#         if name1 != name2:
#             if name2 in some_list:
#                 index2 = some_list.index(name2)
#                 if index1 < index2 :
#                     print(some_list[:index1] + some_list[index2+1:])
#                 else:
#                     index1 = index2
#                     index2 = some_list.index(name1)
#                     print(some_list[:index1] + some_list[index2+1:])
#             else:
#                 print(f'"{name2}" too list nist!')
#         else:
#             print('2 ta esm nabayad yeki bashan!')
#     else:
#         print(f'"{name1}" too list nist!')
#
# ListMaker(names, 'Vahid', 'Faeze')



#3-2

# number_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14',\
# '15','16','17','18','19','20']
#
# def quarterdict(some_list):
#
#     cont = int(len(number_list)/4)
#
#     quarter1 = some_list[:cont]
#     quarter2 = some_list[cont:(cont*2)]
#     quarter3 = some_list[(cont*2):(cont*3)]
#     quarter4 = some_list[(cont*3):]
#
#     num_dict = dict()
#     num_dict ['Quarter1'] = quarter1[0]
#     num_dict ['Quarter2'] = quarter2[0]
#     num_dict ['Quarter3'] = quarter3[0]
#     num_dict ['Quarter4'] = quarter4[0]
#
#     print(num_dict)
#
# quarterdict(number_list)




#3-3

# number_list = [100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#
# def maxmin(some_list):
#
#     some_list.sort()
#     min = some_list[0]
#     max = some_list[-1]
#     print('Ekhtelafe min va max liste ma : ', (max-min))
#
# maxmin(number_list)


#3-4
#
# def BMI():
#
#     ghad = float(input('Ghade Shoma Chande? (bar hasbe metr) \n'))
#     vazn = float(input('Vazne Shoma Chande ? (bar hasbe kg) \n'))
#
#     BMI = vazn/(ghad**2)
#     bmi_dict = dict()
#
#     if BMI < 18.5:
#         bmi_dict [BMI] = 'Kamboode Vazn'
#         print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Kamboode\
#      Vazn Darid.')
#
#     elif BMI >= 18.5 and BMI < 25:
#         bmi_dict [BMI] = 'Normal'
#         print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Normal\
#      Hastid.')
#
#     elif BMI >= 25 and BMI < 30:
#         bmi_dict [BMI] = 'Ezafe Vazn'
#         print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Ezafeh\
#      Vazn Darid!')
#
#     elif BMI >= 30 and BMI < 35:
#         bmi_dict [BMI] = 'Chagh'
#         print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Chagh\
#      Mahsoob Mishavid!')
#
#     elif BMI > 35:
#         bmi_dict [BMI] = 'Kheili Chagh'
#         print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Kheili\
#      Chagh Mahsoob Mishavid!')
#
# BMI()
