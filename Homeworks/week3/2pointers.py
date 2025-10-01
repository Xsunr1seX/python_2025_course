nums1 = [1,5,7,9]
nums2 = [2,3,5,6,7,8]
result = []
p1 = 0
p2 = 0
while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] == nums2[p2]:
        p1 += 1
        p2 += 1
    elif nums1[p1] < nums2[p2]:
        result.append(nums1[p1])
        p1 += 1
    elif nums2[p2] < nums1[p1]:
        result.append(nums2[p2])
        p2 += 1
while(p1<len(nums1)):
    result.append(nums1[p1])
    p1 += 1
while(p2<len(nums2)):
    result.append(nums2[p2])
    p2 += 1
print(result)
