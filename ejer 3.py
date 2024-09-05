import sympy as sp

# Definir las variables
B, H, n, S = sp.symbols('B H n S')

# Fórmula de Manning para Q
Q = (1/n) * ((B * H)**(5/3)) / ((B + 2*H)**(2/3)) * sp.sqrt(S)

# Derivadas parciales de Q con respecto a n y S
dQ_dn = sp.diff(Q, n)
dQ_dS = sp.diff(Q, S)

# Valores nominales
B_val = 20  # metros
H_val = 0.3  # metros
n_val = 0.03  # rugosidad
S_val = 0.0003  # pendiente

dQ_dn_val = dQ_dn.subs({B: B_val, H: H_val, n: n_val, S: S_val})
dQ_dS_val = dQ_dS.subs({B: B_val, H: H_val, n: n_val, S: S_val})

# Mostrar los resultados numéricos
print("Sensibilidad con respecto a n:", dQ_dn_val)
print("Sensibilidad con respecto a S:", dQ_dS_val)
