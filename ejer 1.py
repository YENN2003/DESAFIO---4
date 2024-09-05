import sympy as sp

# Definir la variable y la función
x = sp.symbols('x')
f = 25*x**3 - 6*x**2 + 7*x - 88

a = 1  # base de la expansión (punto alrededor del cual expandimos)
x_eval = 3  # valor en el que queremos evaluar la función

# Calcular las derivadas
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)
f_triple_prime = sp.diff(f_double_prime, x)

f_a = f.subs(x, a)
f_prime_a = f_prime.subs(x, a)
f_double_prime_a = f_double_prime.subs(x, a)
f_triple_prime_a = f_triple_prime.subs(x, a)

# Expansión de Taylor hasta tercer orden
taylor_approx = (
    f_a +
    f_prime_a * (x_eval - a) +
    (f_double_prime_a / 2) * (x_eval - a)**2 +
    (f_triple_prime_a / 6) * (x_eval - a)**3
)

# Calcular el valor real de f(3)
f_true = f.subs(x, x_eval)

# Calcular el error relativo porcentual verdadero
true_error = abs((f_true - taylor_approx) / f_true) * 100

# Mostrar resultados
print(f"f(1) = {f_a}")
print(f"f'(1) = {f_prime_a}")
print(f"f''(1) = {f_double_prime_a}")
print(f"f^{(3)}(1) = {f_triple_prime_a}")
print(f"Aproximación de Taylor de tercer orden en x=3: {taylor_approx}")
print(f"Valor real f(3): {f_true}")
print(f"Error relativo porcentual verdadero: {true_error} %")
