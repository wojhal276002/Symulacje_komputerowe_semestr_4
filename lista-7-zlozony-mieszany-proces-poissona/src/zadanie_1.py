import matplotlib.pyplot as plt
import numpy as np
import scipy

n = 1000
ts = np.linspace(-5, 5, 1000)
# poisson
lambda_pois = 2
data1 = np.random.poisson(lambda_pois, n)
emp1 = [np.sum(np.exp(1j * t * data1)) / n for t in ts]

emp_pois_r, emp_pois_i = np.real(emp1), np.imag(emp1)

teo1 = np.exp(lambda_pois * (np.exp(1j * ts) - 1))
teo_pois_r, teo_pois_i = np.real(teo1), np.imag(teo1)

plt.title("Funkcja charakterystyczna dla Poisson(2)")
plt.scatter(emp_pois_r, emp_pois_i, label="empir Pois")
plt.scatter(teo_pois_r, teo_pois_i, label="teor Pois")
plt.legend()
plt.show()
plt.title("Funkcja charakterystyczna dla Poisson(2)")
plt.plot(ts, emp_pois_r, label="empir Pois real")
plt.plot(ts, teo_pois_r, label="teor Pois real")
plt.plot(ts, emp_pois_i, "--", label="empir Pois imag")
plt.plot(ts, teo_pois_i, "--", label="teor Pois imag")
plt.legend()
plt.show()
# norm
mi = 0
sigma = 1
data2 = np.random.normal(mi, sigma, n)
emp2 = [np.sum(np.exp(1j * t * data2)) / n for t in ts]

emp_nor_r, emp_nor_i = np.real(emp2), np.imag(emp2)

teo2 = np.exp(1j * ts * mi - 0.5 * (sigma**2) * ts**2)
teo_nor_r, teo_nor_i = np.real(teo2), np.imag(teo2)

plt.title("Funkcja charakterystyczna dla Normal(0,1)")
plt.plot(ts, emp2, label="empir Norm")
plt.plot(ts, teo2, label="teor Norm")
plt.legend()
plt.show()
plt.title("Funkcja charakterystyczna dla Normal(0,1)")
plt.plot(ts, emp_nor_r, label="empir Norm real")
plt.plot(ts, teo_nor_r, label="teor Norm imag")
plt.plot(ts, emp_nor_i, "--", label="empir Norm imag")
plt.plot(ts, teo_nor_i, "--", label="teor Norm imag")
plt.legend()
plt.show()
# exp
lamb = 1
data3 = np.random.exponential(lamb, n)
emp3 = [np.sum(np.exp(1j * t * data3)) / n for t in ts]

emp_exp_r, emp_exp_i = np.real(emp3), np.imag(emp3)

teo3 = (1 - ((1j * ts) / lamb)) ** (-1)
teo_exp_r, teo_exp_i = np.real(teo3), np.imag(teo3)

plt.title("Funkcja charakterystyczna dla Exponential(1)")
plt.scatter(emp_exp_r, emp_exp_i, label="empir Exp")
plt.scatter(teo_exp_r, teo_exp_i, label="teor Exp")
plt.legend()
plt.show()
plt.title("Funkcja charakterystyczna dla Exponential(1)")
plt.plot(ts, emp_exp_r, label="empir Exp real")
plt.plot(ts, teo_exp_r, label="teor Exp real")
plt.plot(ts, emp_exp_i, "--", label="empir Exp imag")
plt.plot(ts, teo_exp_i, "--", label="teor Exp imag")
plt.legend()
plt.show()
# cauchy
mi_c = 0
lamb_c = 1
data4 = np.random.standard_cauchy(n)
emp4 = [np.sum(np.exp(1j * t * data4)) / n for t in ts]

emp_c_r, emp_c_i = np.real(emp4), np.imag(emp4)

teo4 = np.exp(1j * ts * mi_c - np.abs(ts) / lamb_c)
teo_c_r, teo_c_i = np.real(teo4), np.imag(teo4)

plt.title("Funkcja charakterystyczna dla Cauchy(0,1)")
plt.plot(ts, emp4, label="empir Cauchy")
plt.plot(ts, teo4, label="teor Cauchy")
plt.legend()
plt.show()
plt.title("Funkcja charakterystyczna dla Cauchy(0,1)")
plt.plot(ts, emp_c_r, label="empir Cauchy real")
plt.plot(ts, teo_c_r, label="teor Cauchy real")
plt.plot(ts, emp_c_i, "--", label="empir Cauchy imag")
plt.plot(ts, teo_c_i, "--", label="teor Cauchy imag")
plt.legend()
plt.show()
# gamma
p = 2
lamb_g = 2
data5 = np.random.gamma(p, lamb_g, n)
emp5 = [np.sum(np.exp(1j * t * data5)) / n for t in ts]

emp_g_r, emp_g_i = np.real(emp5), np.imag(emp5)

teo5 = (1 - ((1j * ts) / lamb)) ** (-p)
teo_g_r, teo_g_i = np.real(teo5), np.imag(teo5)

plt.title("Funkcja charakterystyczna dla Gamma(2,2)")
plt.scatter(emp_g_r, emp_g_i, label="empir Gamma")
plt.scatter(teo_g_r, teo_g_i, label="teor Gamma")
plt.legend()
plt.show()
plt.title("Funkcja charakterystyczna dla Gamma(2,2)")
plt.plot(ts, emp_g_r, label="empir Gamma real")
plt.plot(ts, teo_g_r, label="teor Gamma real")
plt.plot(ts, emp_g_i, "--", label="empir Gamma imag")
plt.plot(ts, teo_g_i, "--", label="teor Gamma imag")
plt.legend()
plt.show()
