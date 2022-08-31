# names = ['iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
# 'soosan' , 'mina' , 'pegah' , 'simin' , 'giti']
#
# name = input('esm ro vared kon: ')
#
# if name in names:
#     print('vojood dare')
# else:
#     names.append(name)
#     print(f'"{name}" ezafe shod.')
# print(names)


# names = ['iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
#  'soosan' , 'mina' , 'pegah' , 'simin' , 'giti']
#
# name = input('esm ro vared kon: ')
#
# if name in names:
#     names.remove(name)
#     print('vojood dasht va hazf shod','\n',names)
# else:
#     names.append(name)
#     print(f'"{name}" ezafe shod.','\n',names)
#



# names = ['iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
#  'soosan' , 'mina' , 'pegah' , 'simin' , 'giti']
# del names[::2]
# print(names)


#
# names = ['iman' , 'ali' , 'reza' , 'hossein' , 'farid' , 'sasan' , 'sara' ,\
#  'soosan' , 'mina' , 'pegah' , 'simin' , 'giti']
#
# name1 = input('esm aval ro vared kon: ')
# if name1 in names:
#     index1 = names.index(name1)
#     name2 = input('esm dovom ro vared kon: ')
#     if name2 in names:
#         index2 = names.index(name2)
#         print(names[index1+1:index2])
#     else:
#         print(f'{name2} nadarim!')
# else:
#     print(f'{name1} nadarim!')


# ********home work 1
# names = ['Ahmadreza', 'Faeze', 'Farnaz', 'Forough', 'Iman', 'Mina', 'Moein',\
# 'Mohammad', 'Mona', 'Parsa', 'Roghaye', 'Roxana', 'Sepide Ba', 'Sepide Bi',\
# 'Omid', 'Sepehr', 'Shahab', 'Shayan', 'Zohre', 'Vahid', 'Sogand']
#
# name1 = input('esm aval ro vared kon: ')
# if name1 in names:
#     index1 = names.index(name1)
#     name2 = input('esm dovom ro vared kon: ')
#     if name1 != name2:
#         if name2 in names:
#             index2 = names.index(name2)
#             if index1 < index2 :
#                 print(names[:index1] + names[index2+1:])
#             else:
#                 index1 = index2
#                 index2 = names.index(name1)
#                 print(names[:index1] + names[index2+1:])
#         else:
#             print(f'"{name2}" too list nist!')
#     else:
#         print('2 ta esm nabayad yeki bashan!')
# else:
#     print(f'"{name1}" too list nist!')
# ******
#https://paste.ubuntu.ir/ivggp


# names = ['Ahmadreza', 'Faeze', 'Farnaz', 'Forough', 'Iman', 'Mina', 'Moein',\
# 'Mohammad', 'Mona', 'Parsa', 'Roghaye', 'Roxana', 'Sepide Ba', 'Sepide Bi',\
# 'Omid', 'Sepehr', 'Shahab', 'Shayan', 'Zohre', 'Vahid', 'Sogand', 'Iman']
# set = set(names)
# tedad = len(set)
# print(tedad)



# my_info = {'name':'Iman', 'age':'31', 'job':'DevOps'}
# print(my_info['job'])



# *******home work 4
# number_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14',\
# '15','16','17','18','19','20']
#
# cont = int(len(number_list)/4)
#
# quarter1 = number_list[:cont]
# quarter2 = number_list[cont:(cont*2)]
# quarter3 = number_list[(cont*2):(cont*3)]
# quarter4 = number_list[(cont*3):]
#
# num_dict = dict()
# num_dict ['Quarter1'] = quarter1[0]
# num_dict ['Quarter2'] = quarter2[0]
# num_dict ['Quarter3'] = quarter3[0]
# num_dict ['Quarter4'] = quarter4[0]
#
# print(num_dict)
# *********************
#https://paste.ubuntu.ir/kzwqf



# ***********************home work 5
# number_list = [100,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# number_list.sort()
# min = number_list[0]
# max = number_list[-1]
# print('Ekhtelafe min va max liste ma : ', (max-min))
# *************************************
#https://paste.ubuntu.ir/bsbng




#********************home work 6
ghad = float(input('Ghade Shoma Chande? (bar hasbe metr) \n'))
vazn = float(input('Vazne Shoma Chande ? (bar hasbe kg) \n'))

BMI = vazn/(ghad**2)
bmi_dict = dict()

if BMI < 18.5:
    bmi_dict [BMI] = 'Kamboode Vazn'
    print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Kamboode\
 Vazn Darid.')

elif BMI >= 18.5 and BMI < 25:
    bmi_dict [BMI] = 'Normal'
    print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Normal\
 Hastid.')

elif BMI >= 25 and BMI < 30:
    bmi_dict [BMI] = 'Ezafe Vazn'
    print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Ezafeh\
 Vazn Darid!')

elif BMI >= 30 and BMI < 35:
    bmi_dict [BMI] = 'Chagh'
    print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Chagh\
 Mahsoob Mishavid!')

elif BMI > 35:
    bmi_dict [BMI] = 'Kheili Chagh'
    print(bmi_dict, '\nYani Shakhese BMI Shoma Barabar Ast Ba:', BMI, 'Va Kheili\
 Chagh Mahsoob Mishavid!')

 #https://paste.ubuntu.ir/uqtwl
