import numpy as np


def approximate_polynomial(x_values, y_values, round_digits=6):
    sum_x = round(sum(x_values), round_digits)
    sum_y = round(sum(y_values), round_digits)
    sum_x2 = round(sum([x * x for x in x_values]), round_digits)
    sum_x3 = round(sum([x * x * x for x in x_values]), round_digits)
    sum_x4 = round(sum([x * x * x * x for x in x_values]), round_digits)
    sum_x_y = round(sum([x * y for x, y in zip(x_values, y_values)]), round_digits)
    sum_x2_y = round(sum([x * x * y for x, y in zip(x_values, y_values)]), round_digits)
    print(f"sum_x: {sum_x}")
    print(f"sum_y: {sum_y}")
    print(f"sum_x2: {sum_x2}")
    print(f"sum_x3: {sum_x3}")
    print(f"sum_x4: {sum_x4}")
    print(f"sum_x_y: {sum_x_y}")
    print(f"sum_x2_y: {sum_x2_y}")
    print()

    # Задаем матрицу A и вектор B для системы линейных уравнений
    A = np.array([[sum_x4, sum_x3, sum_x2], [sum_x3, sum_x2, sum_x], [sum_x2, sum_x, len(x_values)]])
    B = np.array([sum_x2_y, sum_x_y, sum_y])
    print(A, "A")
    print(B, "B")
    print()

    # Решаем систему линейных уравнений с использованием метода квадратного корня
    L = np.linalg.cholesky(A)
    y = np.linalg.solve(L, B)
    coefficients = np.linalg.solve(L.T, y)
    print(L, "L")
    print()

    a, b, c = coefficients

    return round(a, round_digits), round(b, round_digits), round(c, round_digits)


def sqrt_error(y_values, y_appr_values, round_digits=6):
    return round((sum([(y - y_appr) ** 2 for y, y_appr in zip(y_values, y_appr_values)]) / len(y_values)) ** 0.5, round_digits)


x_values = [6.5, 6.5, 9.5, -10, 0.5, 7, -4, -9.5, 8, 0, 9]
y_values = [7.2, 7.7, -10, -0.2, 0, -8.8, -6.3, -0.4, -6.2, -9.7, -9.8]

a, b, c = approximate_polynomial(x_values, y_values)
np_x_values = np.array(x_values)
y_approx_values = a * np_x_values ** 2 + b * np_x_values + c
error = sqrt_error(y_values, y_approx_values)

for i, (x, y, y_approx) in enumerate(zip(x_values, y_values, y_approx_values)):
    print(f"{i}) " "(x = {:.6f} \ty = {:.6f} \ty_approximate = {:.6f} \tdiff^2 = {:.6f})".format(
        x, y, y_approx, (y - y_approx) ** 2
    ))
print()

print(f"Приближающий полином второй степени: f(x) = {a}x^2 + {b}x + {c}")
print(f"Ошибка: {error}")
