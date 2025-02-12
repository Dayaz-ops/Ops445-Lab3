def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print('my number is ', number)  # This works because print() supports multiple arguments
print('my number is ' + str(number))  # This converts number to a string
print('my number is ' + str(return_number_value()))  # Direct conversion inside print

