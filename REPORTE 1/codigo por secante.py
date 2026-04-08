import numpy as np
import matplotlib.pyplot as plt

def metodo_secante(f, x0, x1, tol_porcentaje, max_iter=100):
    error_relativo = 100
    iteraciones = 0
    
    print(f"{'Iter':<5} | {'xi-1':<8} | {'xi':<8} | {'xi+1':<8} | {'Ea (%)':<8}")
    print("-" * 55)
    while error_relativo > tol_porcentaje and iteraciones < max_iter:
        denominador = f(x1) - f(x0)
        if denominador == 0:
            print("Error: División por cero (las f(x) son iguales).")
            return None
        
        # --- FÓRMULA DE LA SECANTE ---
        # Es la misma que Falsa Posición, pero sin importar los signos
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))        
        if x2 != 0:
            error_relativo = abs((x2 - x1) / x2) * 100
        
        iteraciones += 1
        
        ea_str = f"{error_relativo:.4f}%" if iteraciones > 1 else "---"
        print(f"{iteraciones:<5} | {x0:.4f} | {x1:.4f} | {x2:.4f} | {ea_str}")
        x0 = x1
        x1 = x2

        if error_relativo < tol_porcentaje:
            break

    print("-" * 55)
    print(f"Raíz encontrada en {x1:.4f} con un error de {error_relativo:.4f}%")
    return x1

def graficar_secante(f, x_start, x_end, raiz):
    x = np.linspace(x_start - 1, x_end + 1, 400)
    y = f(x)
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='f(x)', color='purple')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    if raiz is not None:
        plt.scatter([raiz], [0], color='red', zorder=5, label=f'Raíz aprox: {raiz:.4f}')
    plt.title("Visualización: Método de la Secante (Método Abierto)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

# --- CONFIGURACIÓN ---
f_ejercicio = lambda x: np.arctan(x) + x - 1

# En la secante, x0 y x1 son solo "puntos de partida"
x_inicial_0 = 0.4
x_inicial_1 = 0.6
tolerancia = 0.01 # 1%

raiz_secante = metodo_secante(f_ejercicio, x_inicial_0, x_inicial_1, tolerancia)

if raiz_secante is not None:
    graficar_secante(f_ejercicio, x_inicial_0, x_inicial_1, raiz_secante)