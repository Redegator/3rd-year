import numpy as np


v1 = 0.2
v2 = 0.1
ro1 = 1000
ro2 = 1500
t1_start = 25
t1_end = 45
t2_start = 95
c1 = 4000
c2 = 2000

# "ЗЛАТИ:"
# v1 = 0.1
# v2 = 0.05
# ro1 = 1000
# ro2 = 1500
# t1_start = 20
# t1_end = 40
# t2_start = 95
# c1 = 4000
# c2 = 2000


d_t_m = t1_end - t1_start
d_t_b = (v1 * ro1 * c1 * d_t_m)/(v2 * ro2 * c2)

d_t_ser = (d_t_b - d_t_m) / np.log(d_t_b / d_t_m)


print(d_t_m)
print(d_t_b)
print(d_t_ser)