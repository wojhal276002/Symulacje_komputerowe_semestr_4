import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def matrix_2x2(a, b, c, d):
    if a * c > b * d:
        mat_cov = np.matrix([[a, b], [c, d]])
        mat_mean = np.matrix([0, 0]).reshape(2, 1)
        return mat_cov, mat_mean
    else:
        raise ValueError("Wyznacznik musi być wiekszy niz zero")


cov2x2, mean2x2 = matrix_2x2(6, 1, 1, 1)


def wektor_norm(n, mat_cov, mat_mean):
    A = np.linalg.cholesky(mat_cov)
    Z = np.random.normal(loc=0, scale=1, size=2 * n).reshape(2, n)
    X = (mat_mean + A * Z).reshape(n, 2)
    return X


X = wektor_norm(1000, cov2x2, mean2x2)
x, y = [X[:, 0]], [X[:, 1]]
plt.title("Wektory normalne dla macierzy kowariancji 2x2")
plt.scatter(x, y)
plt.xlabel("Wartości X wektorów")
plt.ylabel("Wartości Y wektorów")
plt.show()


mat_cov_3x3 = np.matrix([[4, -1, 0], [-1, 5, 2], [0, 2, 6]])
mat_mean_3x3 = np.matrix([0, 0, 0]).reshape(3, 1)
n = 1000
if_pos = np.all(np.linalg.eigvals(mat_cov_3x3) > 0)
print(np.linalg.det(mat_cov_3x3))
if if_pos:
    A = np.linalg.cholesky(mat_cov_3x3)
    Z = np.random.normal(loc=0, scale=1, size=3 * n).reshape(3, n)
    X = (mat_mean_3x3 + A * Z).reshape(n, 3)
    x, y, z = [X[:, 0]], [X[:, 1]], [X[:, 2]]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_title("Wektory normalne dla macierzy kowariancji 3x3")
    ax.scatter(x, y, z)
    ax.set_xlabel("Wartości X wektorów")
    ax.set_ylabel("Wartości Y wektorów")
    ax.set_zlabel("Wartości Z wektorów")
    plt.show()
