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
