V_zag = 3.4
delta_p = 6.9 * 10**4
h_oc = 13/1000
w_oc = 57/100
rv = 5.87 * 10**10
R_fn = 4.1 * 10**9
x_ct = 28/100
v_np_p = 2.5 * 10**-3
tay_c2 = 19

ro_p = 998
ro_tv = 1225
μ = 1/1000
μ_np = 523.3 * 10**-6



ro_oc = ro_tv * ro_p / (ro_p + (ro_tv-ro_p) * w_oc)
print("2.1:", ro_oc)

x_o = x_ct * ro_p / (ro_oc * (1 - (w_oc - x_ct)))
print("2.2:", x_o)

x_v = x_ct * ro_p * (1 - w_oc) / (1 - (w_oc - x_ct))
print("2.3:", x_v)


h_oc_div_x_0 = (h_oc / x_o)
tay_f = ( μ * x_v * rv / (2 * delta_p) ) * h_oc_div_x_0**2 + μ * R_fn / delta_p * h_oc_div_x_0
print("3:", tay_f)

k = 1.1

tay_np = k * v_np_p * ro_oc * μ_np * rv * x_v * h_oc / (delta_p * x_o) * (h_oc + x_o * R_fn / (rv * x_v))
print("4:", tay_np)

φc1 = 60
φ0 = 25
φp = 24
φm = [4,5,14,5]

n_ = (360 - (φc1 + φ0 + φp + sum(φm))) / (360 * (tay_f + tay_np + tay_c2))
print("6:", n_)

tay_ = 1 / n_
print("8:", tay_)

v_f_pt = h_oc / x_o
print("9:", v_f_pt)

F_zag = V_zag * tay_ / (3600 * v_f_pt * 0.8)
print("10:", F_zag)


#Б020-2.6У
φf = 132
φpr_φc2 = 103
Ff = 20



n1 = φf / (360 * tay_f)
n2 = φpr_φc2 / (360 * (tay_np + tay_c2))
n = min(n1, n2)

print("12:", n1)
print("12:", n2)

φf_ = 360 * tay_f * n
print("13:", φf_)

tay_ц = 1 / n
print("14:", tay_ц)


Vf = v_f_pt * Ff * 0.8 * 3600 / tay_ц
print("15:", Vf)

print(V_zag < Vf)