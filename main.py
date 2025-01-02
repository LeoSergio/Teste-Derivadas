import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Entrada da função e intervalo
f_expr = input("Digite a função f(x): ")  # Exemplo: "x**3 - 3*x"
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
x = sp.symbols('x')
f = sp.sympify(f_expr)

# Derivada da função
f_prime = sp.diff(f, x)

# Verificar Teorema de Rolle
if sp.N(f.subs(x, a)) == sp.N(f.subs(x, b)):
    crit_points = sp.solve(f_prime, x)  # Encontrar c tal que f'(c) = 0
    crit_points = [c for c in crit_points if a < c < b]
    if crit_points:
        print("Teorema de Rolle aplicável. Pontos c encontrados:")
        print(crit_points)
    else:
        print("Teorema de Rolle não aplicável: f'(c) = 0 não encontrado no intervalo.")
else:
    print("Teorema de Rolle não aplicável: f(a) != f(b).")

# Verificar Teorema do Valor Médio
avg_rate = (f.subs(x, b) - f.subs(x, a)) / (b - a)
c_tvm = sp.solve(f_prime - avg_rate, x)
c_tvm = [c for c in c_tvm if a < c < b]
if c_tvm:
    print("Teorema do Valor Médio aplicável. Valor c encontrado:")
    print(c_tvm[0])
else:
    print("Teorema do Valor Médio não aplicável.")

# Plotagem gráfica
x_vals = np.linspace(a - 1, b + 1, 500)
f_vals = [sp.N(f.subs(x, val)) for val in x_vals]

plt.plot(x_vals, f_vals, label='f(x)')
plt.axvline(x=a, color='gray', linestyle='--', label='a')
plt.axvline(x=b, color='gray', linestyle='--', label='b')

# Destaques gráficos para Rolle e TVM
if crit_points:
    for c in crit_points:
        plt.scatter([c], [sp.N(f.subs(x, c))], color='red', label=f"c (Rolle)")

if c_tvm:
    c_val = c_tvm[0]
    plt.scatter([c_val], [sp.N(f.subs(x, c_val))], color='green', label="c (TVM)")
    secant_line = avg_rate * (x_vals - a) + sp.N(f.subs(x, a))
    plt.plot(x_vals, secant_line, linestyle='--', color='purple', label='Secante (TVM)')

plt.legend()
plt.title("Teoremas de Rolle e Valor Médio")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
