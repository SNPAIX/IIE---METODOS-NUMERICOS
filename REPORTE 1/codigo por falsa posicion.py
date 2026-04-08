import numpy as np
import matplotlib.pyplot as plt
def falsa_posicion(f, a, b, tol_porcentaje):
    if f(a) * f(b) >= 0:
        print("El método falló: f(a) y f(b) deben tener signos opuestos.")
        return None
    c = a
    c_anterior = 0
    error_relativo = 100
    iteraciones = 0
    print(f"{'Iter':<5} | {'a':<8} | {'b':<8} | {'c (raiz)':<8} | {'Ea (%)':<8}")
    print("-" * 55)
    # El bucle continúa mientras el error sea mayor a la tolerancia (1%)
    while error_relativo > tol_porcentaje:
        c_anterior = c
        #formula de falsa posicion
        # c = b - (f(b) * (a - b)) / (f(a) - f(b))
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        if c != 0:
            error_relativo = abs((c - c_anterior) / c) * 100
        iteraciones += 1
        ea_str = f"{error_relativo:.4f}%" if iteraciones > 1 else "---"
        print(f"{iteraciones:<5} | {a:.4f} | {b:.4f} | {c:.4f} | {ea_str}")
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("-" * 55)
    print(f"Raíz encontrada en {c:.4f} con un error de {error_relativo:.4f}%")
    return c
def graficar(f, a, b, raiz):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(0, color='black', linewidth=1) 
    if raiz is not None:
        plt.scatter([raiz], [0], color='red', zorder=5, label=f'Raíz aprox: {raiz:.4f}')   
    plt.title("Visualización: Método de Falsa Posición")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

#recordatorio que funciones se colocan como np XD
f_ejercicio = lambda x: x**2 -1

# parametros:función, intervalo a, intervalo b, tolerancia en %
raiz = falsa_posicion(f_ejercicio, 0, 2, 1.0) 
if raiz is not None:
    graficar(f_ejercicio, 0, 2, raiz)
else: #namas para ver la grafica no tiene raices
        print("No se grafico nada porque no existe una raiz en ese intervalo")
        graficar(f_ejercicio, 1, 3, None)