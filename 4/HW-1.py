def BMI():
    weight = float(input('VAZN ra vared konid: '))
    height = float(input('GHAD ra vared konid: '))

    if weight < 500 and height < 5 :
        calculate = weight / (height ** 2)
        print('Your BMI is : ', calculate)

    elif  weight < 500 and height > 5 :
        calculate = weight / ((height/100) ** 2)
        print('Your BMI is : ', calculate)

    elif  weight > 500 and height < 5 :
        calculate = (weight/1000) / (height ** 2)
        print('Your BMI is : ', calculate)

    else :
        calculate = (weight/1000) / ((height/100) ** 2)
        print('Your BMI is : ', calculate)


BMI()
