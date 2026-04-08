import numpy as np
import matplotlib.pyplot as plt

def punto_fijo(g, x0, tol_porcentaje, max_iter=100):
    error_relativo = 100
    iteraciones = 0
    xr = x0
    
    print(f"{'Iter':<5} | {'xi':<10} | {'g(xi)':<10} | {'Ea (%)':<10}")
    print("-" * 50)

    while error_relativo > tol_porcentaje and iteraciones < max_iter:
        xr_anterior = xr
        xr = g(xr_anterior)
        iteraciones += 1
        if xr != 0:
            error_relativo = abs((xr - xr_anterior) / xr) * 100
        ea_str = f"{error_relativo:.4f}%" if iteraciones > 1 else "---"
        print(f"{iteraciones:<5} | {xr_anterior:<10.4f} | {xr:<10.4f} | {ea_str}")
        if error_relativo < tol_porcentaje:
            break
            
    print("-" * 50)
    print(f"Raíz encontrada en {xr:.4f} después de {iteraciones} iteraciones.")
    return xr

def graficar_punto_fijo(g, raiz):
    x = np.linspace(0, 1, 400)
    y_g = g(x)
    y_linea = x # La recta y = x
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_g, label='$g(x) = 1 - \\tan^{-1}(x)$', color='green')
    plt.plot(x, y_linea, label='$y = x$', color='orange', linestyle='--')
    
    if raiz is not None:
        plt.scatter([raiz], [raiz], color='red', zorder=5, label=f'Punto fijo: {raiz:.4f}')
    
    plt.title("Método de Punto Fijo ($x = g(x)$)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()

# --- CONFIGURACIÓN ---
# g(x) despejada de: arctan(x) + x - 1 = 0
g_x = lambda x: 1 - np.arctan(x)

x_inicial = 0.5
tolerancia = 1.0 #valor en porcentaje

raiz_pf = punto_fijo(g_x, x_inicial, tolerancia)

if raiz_pf is not None:
    graficar_punto_fijo(g_x, raiz_pf)