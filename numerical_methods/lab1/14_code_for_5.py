def newton_interpolation(x, y, target_x, round_digits=6):
    # Расчет разделенных разностей
    def divided_diff(x, y):
        n = len(y)
        coef = [0] * n
        coef[0] = y[0]

        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])

            coef[j] = round(y[j], round_digits)
            print(f"Разделенная разность {j}: {coef[j]}")

        return coef

    # Получение коэффициентов полинома Ньютона
    coef = divided_diff(x, y)
    print(f"Коэффициенты полинома Ньютона: {coef}\n")

    n = len(coef)

    # Вычисление полинома Ньютона
    result = coef[0]
    temp = 1

    for i in range(1, n):
        temp *= (target_x - x[i - 1])
        divider = f"(x - {x[i - 1]})"
        print(f"Промежуточный результат {i}: {coef[i]} * {divider} * temp")
        result += coef[i] * temp

    return round(result, round_digits)


x = [8, 8.2, 8.4, 8.6, 8.8]
y = [0, -4, -5, 5, 5]
target_x = 8.46

print("Входная таблица:")
for xi, yi in zip(x, y):
    print(f"x = {xi}, y = {yi}")

print(f"\nИнтерполяция для x = {target_x}\n")

result = newton_interpolation(x, y, target_x)
print(f"\nЗначение аппроксимированной функции в точке x = {target_x} равно f(x) = {result}")
