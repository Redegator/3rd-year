
h = 45/1000
d = 1.8
D = 4800

v = 4
t = 84.4
T = t + 273.15

ro1 = 0.972 - (t-80)*(0.972-0.965)/10
print("ro1:", ro1)

ro2 = 0.733 - (t-80)*(0.733-0.722)/10
print("ro2:", ro2)

M1 = 18
M2 = 46

V1 = M1/ro1   #ВОДА
V2 = M2/ro2   #СПИРТ
print("V1:", V1)
print("V2:", V2)

p = 1
i_3 = 1/3
O = (0.0043*T**1.5)/(p * (V1**i_3 + V2**i_3)**2) * (1/M1 + 1/M2)**0.5

print("O:", O, "см2/с")
O = O / 10**4
print("O:", O, "м2/с")


ro_D = 804
M_D = M2 / 1000

G = (D * 0.01 * ro_D * (v+1))/(24 * 3600 * M_D)
print("G:", G, "моль/с")
G_ = G / 1000
print("G:", G_, "кмоль/с")


ro_G = 1.12
M_G = 32/1000
w = (4 * G * M_G)/(ro_G * 3.14 * d**2)
print("w:", w, "m/s")

w_0 = w/(0.8 * 0.08)
print("w_0:", w_0, "m/s")

ro_r = 883
M_r = 29.5/1000

V_r = (G * M_r * v)/((v+1)*ro_r)
print("V_r:", V_r)

П = 1.35
delta_h = (V_r/(0.92 * П))**(2/3)
print("??? delta_h:", delta_h)

g = 9.81
delta_p = (h + delta_h) * ro_r * g
print("??? delta_p:", delta_p)

u_G = 11.5 / 10**6
Re_G = w * h * ro_G / u_G
print("Re_G:", Re_G)

Pr_G = u_G / (O * ro_G)
print("Pr_G:", Pr_G)

K = delta_p / (ro_G * w**2)
print("K:", K)

Nu = 0.0603 * Re_G**1.1 * Pr_G**0.5 * K**0.3
print("Nu:", Nu)


K_y = Nu * O / h
print("K_y:", K_y)