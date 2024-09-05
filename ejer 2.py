import math

# Valores iniciales
x0 = 1
x1 = 2.5
h = x1 - x0

# Derivadas en x0
f_0 = math.log(x0)  # ln(1) = 0
f_1 = 1/x0  # 1/x
f_2 = -1/(x0**2)  # -1/x^2
f_3 = 2/(x0**3)  # 2/x^3
f_4 = -6/(x0**4)  # -6/x^4

# Serie de Taylor hasta el cuarto orden
taylor_approx = f_0 + f_1*h + (f_2*(h**2))/2 + (f_3*(h**3))/6 + (f_4*(h**4))/24

# Valor verdadero
true_value = math.log(2.5)

# Error relativo porcentual
true_percent_error = abs((true_value - taylor_approx) / true_value) * 100

print("Aproximación de Taylor:", taylor_approx)
print("Error relativo porcentual:", true_percent_error)
