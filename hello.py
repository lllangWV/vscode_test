import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def integrateFunction(x):

    return x**2


result, error = quad(integrateFunction, 0, 1)
print("Integration result:", result, "Error:", error)

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
