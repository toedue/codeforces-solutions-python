n = int(input())

for i in  range(-n , n+1):
    spaces = " " * (2 * abs(i))
    nums1 = [str(x) for x in range(n - abs(i) + 1)]
    nums2 = [str(x) for x in range(n - abs(i) -1,-1,-1)]

    row_content = " ".join(nums1 + nums2)

    print(spaces + row_content)

