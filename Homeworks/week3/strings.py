#input
s2 = "ac#b#ac"
t2 = "abc##aa#b#c"

s3 = "a#####b"
t3 = "b"

s = s2
t = t2
# output = равны или нет

result1 = []
result2 = []

#
len1 = len(s)
len2 = len(t)

for i in range(len1):
    if s[i] != '#':
        result1.append(s[i])
    else:
        result1.pop()

for i in range(len2):
    if t[i] != '#':
        result2.append(t[i])
    else:
        result2.pop()

print(str(result1), str(result2))

if result1 == result2:
    print("YES")
else:
    print("NO")



