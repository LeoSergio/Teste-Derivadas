import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def teorema_rolle(func, a, b):
    x = sp.symbols('x')
    f = sp.sympify(func)

    # Verificação das condições
    f_a = f.subs(x, a)
    f_b = f.subs(x, b)
    continuidade = sp.is_continuous(f, x)
    diferenciabilidade = sp.diff(f, x) is not None

    if f_a == f_b and continuidade and diferenciabilidade:
        # Encontrar c tal que f'(c) = 0
        f_prime = sp.diff(f, x)
        c_values = sp.solveset(f_prime, x, domain=sp.Interval(a, b))
        c_values = [c.evalf() for c in c_values if a < c < b]
        return c_values
    return None


def teorema_valor_medio(func, a, b):
    x = sp.symbols('x')
    f = sp.sympify(func)
    f_prime = sp.diff(f, x)

    # Calcular f'(c) = (f(b) - f(a)) / (b - a)
    mean_value = (f.subs(x, b) - f.subs(x, a)) / (b - a)
    c_values = sp.solveset(sp.Eq(f_prime, mean_value), x, domain=sp.Interval(a, b))
    c_values = [c.evalf() for c in c_values if a < c < b]
    return mean_value, c_values


def plot_graficos(func, a, b, rolle_c=None, tvm_c=None, mean_value=None):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(func), 'numpy')

    # Gerar pontos para o gráfico
    x_vals = np.linspace(a - 1, b + 1, 1000)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))

    # Gráfico da função
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(a, color='green', linestyle='--', label=f'a = {a}')
    plt.axvline(b, color='red', linestyle='--', label=f'b = {b}')

    # Pontos para Rolle
    if rolle_c:
        rolle_y = f(np.array(rolle_c))
        plt.scatter(rolle_c, rolle_y, color='orange', label="Ponto de Rolle (f'(c)=0)")

    # Pontos para TVM
    if tvm_c and mean_value is not None:
        secante = lambda x: mean_value * (x - a) + f(a)
        secante_vals = secante(x_vals)
        plt.plot(x_vals, secante_vals, color='purple', linestyle='--', label='Reta Secante')

        tangente = lambda x: mean_value * (x - tvm_c[0]) + f(tvm_c[0])
        tangente_vals = tangente(x_vals)
        plt.plot(x_vals, tangente_vals, color='brown', linestyle='--', label='Reta Tangente')

        tvm_y = f(np.array(tvm_c))
        plt.scatter(tvm_c, tvm_y, color='magenta', label="Ponto de TVM")

    plt.legend()
    plt.title("Gráfico da Função e Teoremas")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()


# Função principal
if __name__ == "__main__":
    # Entrada de dados
    func = input("Digite a função f(x): ")
    a = float(input("Digite o limite inferior do intervalo [a, b]: "))
    b = float(input("Digite o limite superior do intervalo [a, b]: "))

    if a >= b:
        print("O valor de 'a' deve ser menor que 'b'.")
    else:
        # Teorema de Rolle
        rolle_c = teorema_rolle(func, a, b)
        if rolle_c:
            print(f"Teorema de Rolle é aplicável. Valores de c encontrados: {rolle_c}")
        else:
            print("Teorema de Rolle não é aplicável.")

        # Teorema do Valor Médio
        mean_value, tvm_c = teorema_valor_medio(func, a, b)
        if tvm_c:
            print(f"Teorema do Valor Médio: f'(c) = {mean_value}. Valores de c encontrados: {tvm_c}")
        else:
            print("Não foi possível encontrar valores de c para o Teorema do Valor Médio.")

        # Plotar gráficos
        plot_graficos(func, a, b, rolle_c, tvm_c, mean_value)
