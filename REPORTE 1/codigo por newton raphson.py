import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, tol_porcentaje, max_iter=100):
    error_relativo = 100
    iteraciones = 0
    xi = x0
    
    print(f"{'Iter':<5} | {'xi':<10} | {'f(xi)':<10} | {'f_prime(xi)':<12} | {'Ea (%)':<10}")
    print("-" * 65)

    while error_relativo > tol_porcentaje and iteraciones < max_iter:
        xi_anterior = xi        
        f_xi = f(xi)
        df_xi = df(xi)        
        if df_xi == 0:
            print("Error: La derivada es cero. El método no puede continuar.")
            return None
        
        # --- FÓRMULA DE NEWTON-RAPHSON ---
        # xi+1 = xi - f(xi) / f'(xi)
        xi = xi_anterior - (f_xi / df_xi)
        
        iteraciones += 1        
        if xi != 0:
            error_relativo = abs((xi - xi_anterior) / xi) * 100
        ea_str = f"{error_relativo:.4f}%" if iteraciones > 1 else "---"
        print(f"{iteraciones:<5} | {xi_anterior:<10.4f} | {f_xi:<10.4f} | {df_xi:<12.4f} | {ea_str}")

        if error_relativo < tol_porcentaje:
            break
    print("-" * 65)
    print(f"Raíz encontrada en {xi:.4f} en solo {iteraciones} iteraciones.")
    return xi

def graficar_newton(f, raiz):
    x = np.linspace(-1, 2, 400)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='$f(x) = \\tan^{-1}(x) + x - 1$', color='crimson')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    if raiz is not None:
        plt.scatter([raiz], [0], color='blue', zorder=5, label=f'Raíz Newton: {raiz:.4f}')
        plt.title(f"Método de Newton-Raphson (Raíz: {raiz:.4f})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()

# --- CONFIGURACIÓN ---
f_x = lambda x: np.arctan(x) + x - 1
# Derivada: 1/(1+x^2) + 1
df_x = lambda x: (1 / (1 + x**2)) + 1
x_inicial = 0.0  # Punto de partida
tolerancia = 0.001 # 0.001%
raiz_nr = newton_raphson(f_x, df_x, x_inicial, tolerancia)
if raiz_nr is not None:
    graficar_newton(f_x, raiz_nr)