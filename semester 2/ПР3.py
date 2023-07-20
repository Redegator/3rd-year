from math import tan, sin, cos

cv = 3/100
t = 20
n = 85
d = 4 / 10**6
r_max = 162 / 1000
r_min = 64 / 1000
h = 0.8 * 10**-3
a = 50
zr = 68

pi = 3.14

w = 2 * pi * n
μ = 10**-3
r = r_max
delta_ro = 100
ro_r = 998

d_kr = 2.62 * ( μ * μ / (w * w * r * delta_ro * ro_r))**(1/3)
print("d_kr:", d_kr)

r_gr = 2.6 * 10**-6 * (293 / (w * w * r * delta_ro))**0.25
print("r_gr:", r_gr)

dick = 0.7
ctg = 1/ tan(a * 3.14 / 180)


Q_ct = dick * 2/3 * pi * w**2 * zr * ctg * (r_max**3 - r_min**3) * delta_ro / (18 * μ) * d**2
print("Q_ct:", Q_ct)

sin = sin(a * 3.14 / 180)
cos = cos(a * 3.14 / 180)
f = 0.15
ka = 1.2
v_0 = d**2 * delta_ro / (18 * μ) * w**2 * r * (sin - f * cos) * ka
print("v_0:", v_0)


e0 = 0.7
r_ser = (r_max+r_min)/2
v2 = (Q_ct * cv * (1-e0)) / (0.1 * pi * r_ser * h * zr)
print("v2:", v2)