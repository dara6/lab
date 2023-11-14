
def approximate_polynomial(x, y, round_digits=6):
    return round(sum(y) / len(y), round_digits)


def sqrt_error(x, y, approximating_polynomial, round_digits=6):
    return round((sum([(y_ - approximating_polynomial) ** 2 for y_ in y]) / len(y)) ** 0.5, round_digits)


x = [6.5, 6.5, 9.5, -10, 0.5, 7, -4, -9.5, 8, 0, 9]
y = [7.2, 7.7, -10, -0.2, 0, -8.8, -6.3, -0.4, -6.2, -9.7, -9.8]

approximating_polynomial = approximate_polynomial(x, y)
error = sqrt_error(x, y, approximating_polynomial)

for i, (x_, y_) in enumerate(zip(x, y)):
    print(f"{i}) " "(x = {:.6f} \ty = {:.6f} \ty_approximate = {:.6f} \tdiff^2 = {:.6f})".format(
        x_, y_, approximating_polynomial, (y_ - approximating_polynomial) ** 2
    ))

print(f"\nПриближающий полином нулевой степени: f(x) = {approximating_polynomial}")
print(f"Ошибка: {error}")
