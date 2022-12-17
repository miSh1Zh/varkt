import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants


m0 = 287000 + 4725 #сухая масса
m = 258000 # масса топлива
Ft = 3268861.02 # тк сами рассчитать не смогли, взяли среднее из интернета
Cf = 0.5
ro = 1.293 # воздух
S = constants.pi * ((10.3/2)**2)
g = constants.g
k = m/(11*60) #скорость расхода топлива (через 11 мин отсоединилась последняя ступень)


def A(t):
    return (Ft/(m0 - k*t))

def B(t):
    return ((Cf*ro*S)/(2*(m0 - k*t)))

def dv_dt(t, v):
    return (A(t) + B(t)*v - g) 

v0 = 0

t = np.linspace(0, 11*60, 11) 

solve = integrate.solve_ivp(dv_dt, t_span = (0, max(t)), y0 = [v0], t_eval = t)

print(solve.y[0])

x = solve.t
y = solve.y[0]

plt.figure(figsize=(10, 8))
plt.plot(x, y, '.-r', label="first", lw=5, mec='b', mew=2, ms=10)
plt.legend()
plt.grid(True)
plt.show()