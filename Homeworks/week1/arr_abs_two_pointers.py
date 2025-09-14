# input
a = [-3, -2, 0, 1, 3, 5]
#     |               |
# result [0, 1, 2, 3, 3, 5]

a = [abs(i) for i in a]

p1 = 0
p2 = len(a) - 1

final_arr = []

while (p1 <= p2):
    if p1 == p2:
        final_arr.append(a[p1])
        break
    if a[p1] >= a[p2]:
        final_arr.append(a[p1])
        p1 += 1
    else:
        final_arr.append(a[p2])
        p2 -= 1

print(f"{final_arr[::-1]=}")
