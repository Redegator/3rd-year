

d0 = 5 / 1000
D_old = 2.4
w_r = 0.04

pi = 3.14
V_r = w_r * pi * D_old * D_old / 4
print("V_r:", V_r)

w_6 = 23
d_bv = (4 * V_r / (pi * w_6))**0.5
print("d_bv:", d_bv)
d_zovn = 0.114
d_bv = 0.102
print(f'Візьмемо трубу із зовн діаметорм {d_zovn}, її стінка 6мм, внутр діаметр 102мм')

D_cp = 6 * d_zovn
print("D_cp:", D_cp)

d_m = 0.71 #діаметр мішалки з ПР4
h6 = d_m / 4
print("h6:", h6)

ro_r = 993.6
ro_g = 1.143
w0 = 3.4 * (d_bv * ro_r / ro_g)**0.5
print("w0:", w0)

z0 = 4 * V_r / (pi * d0**2 * w0)
print("z0:", z0)
z0 = 288

t = pi * D_cp / z0
print("t:", t)
print("Ставимо у 2 ряди")

z01 = z0 / 2
print("z01:", z01)

t = pi * D_cp / z01
print("t:", t)

sin = 2**0.5 / 2
D0 = D_cp - d_zovn * sin
print("D0:", D0)

t2 = pi * D0 / z01
print("t2:", t2)


w0 = 20
n = 4 * V_r / (pi * d0**2 * w0)

print("n:", n)
n = 460

n_otv_r = n**0.5
print("n_otv_r:", n_otv_r)
n_otv_r = 22

R = D_old / 2
a = R * 2**0.5
print("a:", a)

t = (a - 2 * d0) / n_otv_r
print("t:", t)


print("----------------------------------------")

D = 11.5
H = 13
Vn = 1350
Vp = 460
q_n = 0.022
Dk = 2.25
Htp = 6
n = 265
d_tr = 90/1000

ro_r = 994.4 #При 34 градусах
p0 = 10**5
g = 9.81
Kz = Vp / Vn
Pp = p0 + 0.5 * H * ro_r * Kz * g
print("Pp:", Pp)

T = 273 + 34
q_r = Vp * q_n * (p0 * T)/(Pp * 273)
print("q_r:", q_r)


z = 8
S6 = z * n * 0.785 * d_tr**2
print("S6:", S6)

w_r = q_r / S6
print("w_r:", w_r)

S_4 = 0.785 * (D**2 - z * Dk**2)
print("S_4:", S_4)

Пц = pi * (D + z * Dk)
print("Пц:", Пц)

Пб = pi * z * n * d_tr
print("П6:", Пб)

y_4 = 0.6
y_r = 0.2
y = y_4 + y_r - y_4 * y_r
print("y:", y)

#ТУТ ЦЕ ВЕЛИКЕ СТРАШНЕ РІВНЯННЯ, ЯКЕ Я РОЗБИВ НА ЧАСТИНИ
d_1b = 0.5
d_2b = 1
λ_tp = 0.03
d_1u = 0.5
d_2u = 1
d_180 = 2.3

z1 = (d_1b + d_2b) / (2 * (1 - y)**2)
z2 = λ_tp / (8 * (1 - y)**1.75)
z3 = H * Пб / S6
z4 = (d_1u + d_2u) / (2 * (1-y_4)**2)
z5 = λ_tp / (8 * (1 - y_4)**1.75)
z6 = H * Пц / S_4
z7 = d_180 / ((1 - y)**2)

z_konya = z1 + z2*z3 + z4 + z5*z6 + z7
print("z_konya:", z_konya)

w_p = ((Htp * (y - y_4) * g)/z_konya)**0.5
print("w_p:", w_p)

y__r = w_r / (w_r + w_p + (0.35 + 2 * w_r) * (1 - y_r))
print("y__r:", y__r)

y__6 = y_4 + y__r - y_4 * y__r
print("y__6:", y__6)


print("-----------")
print("y__6:", y__6, "y:", y, " - різниця менше 5%")