list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = list_a + list_b
print(list_c)
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_d = [list_a[0], list_b[0], list_a[1], list_b[1], list_a[2], list_b[2],
          list_a[3], list_b[3], list_a[4], list_b[4]]
print(list_d)
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c_a = []
list_c_b = []
for i in range(2, 5, 2):
    list_c_a.append(i)
    continue
for i in range(7, 10, 2):
    list_c_b.append(i)
    continue
print(list_c_a, list_c_b)
list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_c.reverse()
list_d = list_c
print(list_d)
list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [10, 9, 8, 7, 6]
b = [1, 2, 3, 4, 5]
res = ([a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]]) * 2
print(res)
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
list_f.sort()
list_f.remove(0)
list_f.append(10)
res1 = list_f[:]
list_f.reverse()
res2 = list_f[:]
print(res1, res2)
res1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = [tuple(tup) for tup in zip(res1, res2)]
print(res)
