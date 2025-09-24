# input
a = [-3, -2, 0, 1, 3, 5]

#     |               |

# result [0, 1, 2, 3, 3, 5]

b = [abs(i) for i in a]
c = sorted(b)

p1 = 0
p2 = len(a) - 1

d = []
while True:
    if p1 == p2:
        d.append(abs(a[p1]))
        break
    if abs(a[p1]) >= abs(a[p2]):
        d.append(abs(a[p1]))
        p1 += 1
    else:
        d.append(abs(a[p2]))
        p2 -= 1


print(f"{d[::-1]=}")
