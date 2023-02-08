# Операторы ввода-вывода

"""
var = input("Введите значение: ") # введенное значение будет являться строкой
print(var, ' - ', type(var))

var = int(input("Введите целочисленное число: ")) # введенное значение будет иметь тип int
print(var, ' - ', type(var))
"""

var = 'Hello'
print(var, end = ' ')
var = "World"
print(var)

var_1 = 5
var_2 = 3

result_var = var_1 + var_2

print(var_1, ' + ', var_2, ' = ', result_var, sep='') 
print(f"{var_1} + {var_2} = {result_var}")
print("{} + {} = {}".format(var_1, var_2, result_var))

result_var = var_1 / var_2
print(var_1, '/', var_2, '=', result_var)
print(var_1, '/', var_2, '=', round(result_var, 2))
print(var_1, '/', var_2, '=', round(result_var, 0))