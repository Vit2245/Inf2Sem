from math import sin,tan, cos, exp, log, fabs, pow,sqrt

def integrate_left_rect(func, a, b, n):
    """Интегрирование методом левых прямоугольников."""
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x_i = a + i * h
        integral_sum += func(x_i)
    return integral_sum * h

def integrate_right_rect(func, a, b, n):
    """Интегрирование методом правых прямоугольников."""
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x_i = a + (i + 1) * h
        integral_sum += func(x_i)
    return integral_sum * h

def integrate_trapezoid(func, a, b, n):
    """Интегрирование методом трапеций."""
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x_i = a + i * h
        x_i_plus_1 = a + (i + 1) * h
        integral_sum += (func(x_i) + func(x_i_plus_1)) / 2
    return integral_sum * h


def integrate_simpson(func, a, b, n):
    """Интегрирование методом Симпсона."""
    if n % 2 != 0:
        raise ValueError("n должно быть четным для метода Симпсона")

    h = (b - a) / n
    integral_sum = func(a) + func(b)

    for i in range(1, n, 2):  # Нечетные индексы
        x_i = a + i * h
        integral_sum += 4 * func(x_i)

    for i in range(2, n - 1, 2):  # Четные индексы
        x_i = a + i * h
        integral_sum += 2 * func(x_i)

    return integral_sum * h / 3

def ctg(x):
    return (1/tan(x))

# --- Пример использования ---
def my_function(x):
  return ctg(2*x)/pow(sin(2*x),2)

a = 0.8
b = 1.2
n = round((b-a)/0.05)

print("Левые прямоугольники:", integrate_left_rect(my_function, a, b, n))
print("Правые прямоугольники:", integrate_right_rect(my_function, a, b, n))
print("Метод трапеций:", integrate_trapezoid(my_function, a, b, n))
print("Метод Симпсона:", integrate_simpson(my_function, a, b, n))