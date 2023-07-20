import numpy as np

"""ПОЧАТКУ НЕМА, СОРІ, Я РОБИВ В ЧУЖОМУ ЕКСЕЛІ"""
D = 2.4

w = 0.066
w0 = 0.45
# Nv = 1.5 - 5
Nv = 1.8
ro_r = 993.6
sigma = 0.703


phi = (w/w0*0.5)**0.5 + 3.42*10**(-2) * Nv**0.4 * ro_r**0.2 / sigma**0.6 * (w/w0*0.5)**0.5

Kv = 0.106
Nv2 = (Kv / (0.171 * phi**0.67))**(1/0.44)
print(Nv2)

print(phi)

Vp = 8
N_pr = Nv2 * Vp
print("N_pr:", N_pr)

W_r = 0.3
n = 250 / 60
Eu_m = 6
N_pr = N_pr * 1000

d_m = ((N_pr * W_r**0.25)/(0.695 * (Eu_m * ro_r)**0.9 * n**3.15))**(1/5.85)
print("d_m:", d_m)

G_D = 2.4 / 0.71
print("G_D:", G_D)

H = 1.58
G_H = H / 0.71
print("G_H:", G_H)

G_B = 0.1*2.4 / 0.71
print("G_B:", G_B)

Eu = Eu_m * (G_D/3)**(-1/3) * (2.225/3)*0.5 * (0.338/0.3)**0.3
print("Eu:", Eu)

Zn = 4
d = 8.4
b = 0.142
Zm = 1
O_z = (2 * G_D * Zn * H) / (d * D * Zm) * np.log(D/(D-2*b))
print("O_z:", O_z)

Km = 0.12
Eu_m = 4 * d * Zm * Km
print("Eu_m:", Eu_m)

N_pr = 0.695 * (Eu_m * ro_r)**0.9 * n**3.15 * d_m**5.85 / W_r**0.25
print("N_pr:", N_pr)

Nv = N_pr/Vp
print("Nv:", Nv)

Ne = N_pr/0.9
print("Ne:", Ne)

