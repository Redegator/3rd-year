

gal = "13; 15; 22; 16; 21; 14; 18; 21; 25; 13; 12; 13; 17; 14; 15; 17; 20;20; 16; 17; 21; 28; 21; 21; 24; 19; 21; 20; 14; 13; 14; 16; 20; 15; 14; 20; 20; 16;20; 13; 16; 20; 18; 12; 12; 11; 17; 13; 14; 20; 16; 15; 14; 17; 15; 21; 15; 12; 8;21; 21; 13; 16; 16; 12; 19; 13; 21; 14; 18; 14; 13; 15; 17; 19; 18; 15;"
lis = "15; 13; 21; 21; 10; 14; 13; 13; 16; 17; 13; 21; 21; 19; 14; 18; 12; 27;21; 13; 8; 11; 17; 13; 14; 20; 16; 15; 14; 17; 15; 21; 15; 12; 8; 21; 21; 13; 16; 16;12; 19; 13; 21; 14; 18; 14; 13; 15; 17; 19; 18; 15; 17; 13; 11; 15; 16; 14; 13; 13;20; 13; 13; 12; 13; 13; 13; 10; 21; 18; 17; 17; 21; 20; 13; 10; 13; 14; 13; 14; 16; 12;"


lis = lis.replace(";", ",")
gal = gal.replace(";", ",")
galyavina = gal.split(",")
liiiis = lis.split(",")



#
#
# for i in galyavina:
#     print(i)
#
# print(len(galyavina)-1)

# n1 = 77
# n2 = 83
#
# import math
#
# k1 = 1 + 3.3* math.log(n1, 10)
# k2 = 1 + 3.3* math.log(n2, 10)
#
# print(k1)
# print(k2)

######### ШУКАЮ КЛАСОВІ МЕЖІ
min = 7-1
l = 3
for i in range(7):
    print(f'Класова межа {i+1}: {min+i*l+1}-{min+(i+1)*l}')

######### РАХУЮ Х''
print()
print("X'':")
for i in range(7):
    print(f'x_{i+1}: {min+i*l+1+(l/2)}')


print()

######### РАХУЮ f
new_galyavina = [item.lstrip() for item in galyavina]
new_liiiis = [item.lstrip() for item in liiiis]
# print(new_galyavina)
# print(new_liiiis)

#   ВИВЕСТИ f
print("Галявина:")
for i in range(7):
    res = 0
    for j in range(min+i*l+1, min+(i+1)*l+1):

        x = new_galyavina.count(str(j))
        res += x
    print(f'f{i+1}: {res}')

print()
print("Сухий луг:")
for i in range(7):
    res = 0
    for j in range(min+i*l+1, min+(i+1)*l+1):

        x = new_liiiis.count(str(j))
        res += x
    print(f'f{i+1}: {res}')

''''''
"РАНЖОВАНИЙ РЯД ЧЕРЕЗ ; (ОБЕРЕЖНО ЗІ ЗНАЧЕННЯМИ, В ЯКИХ ІНША КІЛЬКІСТЬ ЦИФР, ТАМ ВОНИ МОЖУТЬ БУТИ В КІНЦІ/НА ПОЧАТКУ ДЕЯКІ)"
"І ВЗАГАЛІ БУВАЮТЬ БАГИ, КРАЩЕ ПЕРЕВІРИТИ"
''''''
new_galyavina.sort()
count = -1 #не їбу чому тут -1, але так працює
for i in new_galyavina:
    i = i + ";"
    count += 1
    new_galyavina[count] = i

new_liiiis.sort()
count = -1
for i in new_liiiis:
    i = i + ";"
    count += 1
    new_liiiis[count] = i


print("Ранжований галявина:")
print(*new_galyavina)

print("Ранжований луг:")
print(*new_liiiis)