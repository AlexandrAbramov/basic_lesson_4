tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print(tuple_d)
tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)
res = []
for i in tuple_d:
    if tuple_d.count(i) > 1:
        res.append((i, tuple_d.count(i)))
print(tuple(res))
