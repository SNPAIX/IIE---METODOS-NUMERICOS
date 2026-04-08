import numpy as np
import matplotlib.pyplot as plt
def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("El método de bisección falló: f(a) y f(b) deben tener signos opuestos.")
        return None
    c = a
    iteraciones = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    print(f"Raíz encontrada en {c:.4f} después de {iteraciones} iteraciones.")
    return c
def graficar(f, a, b, raiz):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(0, color='black', linewidth=1) 
    if raiz is not None:
        plt.scatter([raiz], [0], color='red', zorder=5, label=f'Raíz aprox: {raiz:.4f}')
    plt.title("Visualización del Método de Bisección")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

#CONFIGURACION DE LA ECUACION
f_a = lambda x: (0.95*x**3 - 5.9*x**2 + 10.9*x-6)
raiz_a = biseccion(f_a, 3, 8, 0.01)  #se pone primero los intervalos, error
graficar(f_a, 3, 8, raiz_a) #se grafica la funcion hasta donde se encuentre la raiz