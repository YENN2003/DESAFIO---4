import sympy as sp

# Definir las constantes y variables
A, e, T = sp.symbols('A e T')
sigma = 5.67 * 10**(-8)  # Constante de Stefan-Boltzmann (W m^-2 K^-4)

# Fórmula de Stefan-Boltzmann para H
H = A * e * sigma * T**4

# Derivadas parciales de H con respecto a A, e, y T
dH_dA = sp.diff(H, A)
dH_de = sp.diff(H, e)
dH_dT = sp.diff(H, T)

# Valores nominales
A_val = 0.15  # metros cuadrados
e_val = 0.90  # emisividad
T_val = 650  # Kelvin
delta_A = 0  # no se menciona error en el área
delta_e = 0  # no se menciona error en la emisividad
delta_T = 20  # error en la temperatura

# Evaluar H nominal
H_val = H.subs({A: A_val, e: e_val, T: T_val})

# Evaluar las derivadas parciales en los valores nominales
dH_dA_val = dH_dA.subs({A: A_val, e: e_val, T: T_val})
dH_de_val = dH_de.subs({A: A_val, e: e_val, T: T_val})
dH_dT_val = dH_dT.subs({A: A_val, e: e_val, T: T_val})

# Error en H debido a T (el único con error mencionado)
delta_H = abs(dH_dT_val * delta_T)

# Mostrar los resultados numéricos
print("H nominal:", H_val)
print("Error en H debido a la temperatura:", delta_H)
