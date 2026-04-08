import numpy as np
import matplotlib.pyplot as plt

def busqueda_incrementos(f, x_inicio, x_final, paso):
    print(f"{'Intervalo evaluado':<25} | {'Signo f(a)':<10} | {'Signo f(b)':<10} | {'¿Hay raíz?'}")
    print("-" * 70)
    intervalos_encontrados = []
    x_actual = x_inicio
    # apartado donde se mueve punto por punto
    while x_actual + paso <= x_final:
        a = x_actual
        b = x_actual + paso
        f_a = f(a)
        f_b = f(b)
        hay_raiz = f_a * f_b < 0
        status = "SÍ" if hay_raiz else "No"
        print(f"[{a:^7.2f}, {b:^7.2f}] | {np.sign(f_a):^10.0f} | {np.sign(f_b):^10.0f} | {status}")
        if hay_raiz:
            intervalos_encontrados.append((a, b))
        # Si f(b) es exactamente 0, encontramos la raíz exacta
        if f_b == 0:
            print(f"hay raiz en x = {b}") 
        x_actual = b
    return intervalos_encontrados
def graficar_busqueda(f, x_inicio, x_final, intervalos):
    x = np.linspace(x_inicio - 1, x_final + 1, 400)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)', color='blue', alpha=0.7)
    plt.axhline(0, color='black', linewidth=1)
    
    for i, (a, b) in enumerate(intervalos):
        plt.axvspan(a, b, color='green', alpha=0.3, label=f'Intervalo {i+1}' if i==0 else "")
        plt.scatter([a, b], [f(a), f(b)], color='red', s=30)
    plt.title("Método de Búsqueda por Incrementos")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()
    
#aqui se pone la funcion
f_ejemplo = lambda x: x**2 - 1

inicio = -3
fin = 3
tamaño_paso = 0.01 #el tamaño del paso

intervalos_con_raiz = busqueda_incrementos(f_ejemplo, inicio, fin, tamaño_paso)
if intervalos_con_raiz:
    print(f"\nSe encontraron {len(intervalos_con_raiz)} intervalos con raíces.")
    graficar_busqueda(f_ejemplo, inicio, fin, intervalos_con_raiz)
else:
    print("\nNo se detectaron cambios de signo.")