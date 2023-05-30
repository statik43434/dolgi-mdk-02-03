import numpy as np


roots = int(input("Введите количество неизвестных>>"))
constraint = int(input("Введите количество ограничений>>"))


coefficients = [[0] * roots for i in range(constraint)]
sign = [0 for i in range(constraint)]
right = [0 for i in range(constraint)]
function_coefficients = [0 for i in range(roots)]

for i in range(constraint):
    for j in range(roots):
        coefficients[i][j] = float(input("Введите значение " + str(j + 1)
                                         + " коэффицента " + str(i + 1) + " ограничения: "))

for i in range(constraint):
    sign[i] = input("Введите знак равенства / неравенства ограничений>>")

for i in range(constraint):
    right[i] = input("Введите правую часть ограничений>>")

for i in range(roots):
    function_coefficients[i] = float(input("Введите " + str(i + 1) + " коэффицента функции: "))

constraint_inequality = [0 for i in range(0)]
constraint_equality = [0 for i in range(0)]
for i in range(constraint):
    if sign[i] != "==":
        constraint_inequality.append(i)
    else:
        constraint_equality.append(i)


n = 0
for i in range(len(constraint_inequality)):
    for j in range(len(constraint_inequality)):
        n = i
        if n == j:
            if sign[constraint_inequality[i]] == "<=":
                coefficients[constraint_inequality[i]].insert(roots + j, float(1))
                n -= 1
            else:
                coefficients[constraint_inequality[i]].insert(roots + j, float(-1))
                n -= 1
        else:
            coefficients[constraint_inequality[i]].insert(roots + j, float(0))


for i in range(len(constraint_equality)):
    for j in range(len(constraint_inequality)):
        coefficients[constraint_equality[i]].insert(roots + j, float(0))


for i in range(roots):
    function_coefficients[i] *= -1

for i in range(len(constraint_inequality) + 1):
    function_coefficients.append(float(0))


print(np.row_stack([np.column_stack([coefficients, right]), function_coefficients]))