
def lagrange_interpolation(x, y, target_x, round_digits=6):
    # Расчет базисных полиномов Лагранжа для данной точки i
    def lagrange_basis(i, x, target_x):
        basis = 1
        for j in range(len(x)):
            if i != j:
                basis *= (target_x - x[j]) / (x[i] - x[j])
        return basis

    result = 0

    # Вычисление полинома интерполяции Лагранжа
    for i in range(len(x)):
        basis = lagrange_basis(i, x, target_x)
        print(f"Базис Лагранжа L_{i}(x): {round(basis, round_digits)}")
        term = y[i] * basis
        print(f"Промежуточный результат {i}: y_{i} * L_{i}(x) = {y[i]} * {round(basis, round_digits)} = {round(term, round_digits)}")
        result += term

    return round(result, round_digits)


x = [-4, -3.8, -3.6, -3.4, -3.2]
y = [9, 5, 8, -2, 5]
target_x = -3.52

print("Входная таблица:")
for xi, yi in zip(x, y):
    print(f"x = {xi}, y = {yi}")

print(f"\nИнтерполяция для x = {target_x}\n")

result = lagrange_interpolation(x, y, target_x)
print(f"\nЗначение аппроксимированной функции в точке x = {target_x} равно f(x) = {result}")
