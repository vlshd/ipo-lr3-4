import math
x = float(input("Введите значение x: ")) # Ввод х
if x < 0: # если х меньше 0
    f_x = x ** 2 # х возводится в квадрат
else:
    f_x = math.sqrt(x) # если х больше 0, то корень х
print(f"Значение функции при x = {x} равно {f_x}") # выводится результат