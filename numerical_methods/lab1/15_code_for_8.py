import numpy as np


def approximate_polynomial(x_values, y_values, round_digits=6):
    sum_x = round(sum(x_values), round_digits)
    sum_y = round(sum(y_values), round_digits)
    sum_x_squared = round(sum([x * x for x in x_values]), round_digits)
    sum_x_y = round(sum([x * y for x, y in zip(x_values, y_values)]), round_digits)

    print(f"sum_x: {sum_x}")
    print(f"sum_y: {sum_y}")
    print(f"sum_x_squared: {sum_x_squared}")
    print(f"sum_x_y: {sum_x_y}")
    print()

    # Задаем матрицу A и вектор B для системы линейных уравнений
    A = np.array([[sum_x_squared, sum_x], [sum_x, len(x_values)]])
    B = np.array([sum_x_y, sum_y])
    print(A, 'A')
    print(B, 'B')
    print()

    det_A = round(np.linalg.det(A), round_digits)
    print(f"det_A: {det_A}")
    print()

    # Вычисляем определители матриц A1 и A2, заменяя первый и второй столбец соответственно на вектор B
    det_A1 = round(np.linalg.det(np.column_stack((B, A[:, 1]))), round_digits)
    det_A2 = round(np.linalg.det(np.column_stack((A[:, 0], B))), round_digits)
    print(f"det_A1: {det_A1}")
    print(f"det_A2: {det_A2}")
    print()

    # Решаем систему линейных уравнений с использованием метода Крамера
    a = round(det_A1 / det_A, round_digits)
    b = round(det_A2 / det_A, round_digits)

    return a, b


def sqrt_error(y_values, y_appr_values, round_digits=6):
    return round((sum([(y - y_appr) ** 2 for y, y_appr in zip(y_values, y_appr_values)]) / len(y_values)) ** 0.5, round_digits)


x_values = [6.5, 6.5, 9.5, -10, 0.5, 7, -4, -9.5, 8, 0, 9]
y_values = [7.2, 7.7, -10, -0.2, 0, -8.8, -6.3, -0.4, -6.2, -9.7, -9.8]

a, b = approximate_polynomial(x_values, y_values)
y_approx_values = a * np.array(x_values) + b
error = sqrt_error(y_values, y_approx_values)

for i, (x, y, y_approx) in enumerate(zip(x_values, y_values, y_approx_values)):
    print(f"{i}) " "(x = {:.6f} \ty = {:.6f} \ty_approximate = {:.6f} \tdiff^2 = {:.6f})".format(
        x, y, y_approx, (y - y_approx) ** 2
    ))
print()

print(f"Приближающий полином первой степени: f(x) = {a}x + {b}")
print(f"Ошибка: {error}")
