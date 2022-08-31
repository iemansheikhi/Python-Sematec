

number_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14',\
'15','16','17','18','19','20']

cont = int(len(number_list)/4)

quarter1 = number_list[:cont]
quarter2 = number_list[cont:(cont*2)]
quarter3 = number_list[(cont*2):(cont*3)]
quarter4 = number_list[(cont*3):]

num_dict = dict()
num_dict ['Quarter1'] = quarter1[0]
num_dict ['Quarter2'] = quarter2[0]
num_dict ['Quarter3'] = quarter3[0]
num_dict ['Quarter4'] = quarter4[0]

print(num_dict)
