import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def task2():
    x = np.linspace(-10, 10, 1000)
    x = x[~np.isclose(x, -3, atol=0.1)]
    x = x[~np.isclose(x, 3, atol=0.1)]

    f_x = 5 / (x**2 - 9)

    plt.figure(figsize=(10, 6))
    plt.plot(x, f_x, 'g-', linewidth=2, label='f(x) = 5/(x²-9)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x) = 5/(x²-9)')
    plt.grid(True, alpha=0.3)
    plt.ylim(-20, 20)
    plt.axvline(x=-3, color='red', linestyle='--', alpha=0.5, label='Вертикальные асимптоты')
    plt.axvline(x=3, color='red', linestyle='--', alpha=0.5)
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print(f"NumPy version: {np.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    task2()