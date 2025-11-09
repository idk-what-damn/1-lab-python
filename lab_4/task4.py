from scipy.integrate import quad, dblquad
import numpy as np

def f1(x):
    return np.sin(x)

result1, _ = quad(f1, 0, np.pi)
print("Определённый интеграл ∫₀^π sin(x) dx =", round(result1, 4))

def f2(x, y):
    return x * y

result2, _ = dblquad(f2, 0, 1, lambda x: 0, lambda x: 1)
print("Двойной интеграл ∫₀^1 ∫₀^1 x*y dx dy =", round(result2, 4))
