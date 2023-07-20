import numpy as np


t1_b = 25
t11_b = 32
time = 72 * 3600
t_c = 36

q = 92.72
ro_r = 993.6

q_vt = q * ro_r / time
print("q_vt:", q_vt)

Vp = 8
Nv = 1285
Q = (q_vt *1000 + Nv) * Vp
print("Q:", Q)

delta_t_b = t_c - t1_b
delta_t_m = t_c - t11_b

delta_t_cp = (delta_t_b - delta_t_m) / np.log(delta_t_b/delta_t_m)

print("delta_t_b:", delta_t_b)
print("delta_t_m:", delta_t_m)
print("delta_t_cp:", delta_t_cp)

Pr = 4.754
u_с = 715.8 * 10**-6

t_b = (t1_b + t11_b) / 2
t_st = (t_c + t_b) / 2
print("t_st:", t_st)

u_st = 770.9 * 10**-6
v = u_с / ro_r

print("v:", v)

n = 4.17
d = 0.71
Re = n * d*d / v
print("Re:", Re)

G_D = 3.38
G_D0 = 3
G_H = 2.225
G_H0 = 3
Nu = 0.76 * Re**0.76 * Pr**0.33 * (u_с/u_st)**0.14 * (G_D/G_D0)**-0.13 * (G_H/G_H0)**0.56
print("Nu:", Nu)

half_life_z = 0.6276
D = 2.4
alpha = Nu * half_life_z / D
print("alpha:", alpha)


h = 0.1 * D
b = 0.05

f = h * b
print("f:", f)

П = 2 * (h+b)
print("П:", П)

d_ekv = 4 * f / П
print("d_ekv:", d_ekv)

c_v = 4151.5
G_v = Q / (c_v * (32-25))
print("G_v:", G_v)

ro_v = 996.3
w_v = G_v / (f * ro_v)
print("w_v:", w_v)

v_v = 0.84 * 10**-6
Re2 = w_v * d_ekv / v_v
print("Re2:", Re2)

x = 1 + 3.54 * (d_ekv/D)
print("x:", x)

Pr_v = 5.66
Pr_st = 5.17
Nu2 = 0.021 * Re2**0.8 * Pr_v**0.4 * (Pr_v/Pr_st)**0.25 * x
print("Nu2:", Nu2)

half_life_z_v = 0.61515
alpha2 = Nu2 * half_life_z_v / d_ekv
print("alpha2:", alpha2)

d_st = 0.008
half_life_st = 17
K0 = 1 / (1/alpha + d_st/half_life_st + 1/alpha2)
print("K0:", K0)

K = 0.9 * K0
print("K:", K)

F = Q / (K * delta_t_cp)
print("F:", F)

Hp = F / (3.14 * D)
print("Hp:", Hp)


























