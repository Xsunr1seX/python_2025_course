#input nums1=[1,5,7,9] nums2=[2,3,5,6,7,8]
#output [1,2,3,6,8,9]


nums1 = [1, 5, 7, 9]
nums2 = [2, 3, 5, 6, 7, 8]

i1 = 0
i2 = 0
ans = []
while(i1<len(nums1) and i2<len(nums2)):
    if nums1[i1] == nums2[i2]:
        i1 += 1
        i2 += 1
    elif nums1[i1]<nums2[i2]:
        ans.append(nums1[i1])
        i1 += 1
    else:
        ans.append(nums2[i2])
        i2 += 1
while(i1<len(nums1)):
    ans.append(nums1[i1])
    i1 += 1
while(i2<len(nums2)):
    ans.append(nums2[i2])
    i2 += 1
print(ans)
