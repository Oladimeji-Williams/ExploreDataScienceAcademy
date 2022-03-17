def merge_sort(num, start, end):
    if start<end:
        mid = (start + end)//2
        merge_sort(num, start, mid)
        merge_sort(num, mid, end+1)
        merge(num, start, mid, end+1)
        
def merge(num, start, mid, end):
    i = 0
    j = mid
    k = 0
    temp = list()
    while (i<=mid) and (j<=end):
        if num[i] <= num[j]:
            temp[k] = num[i]
            k += 1
            i += 1
        else:
            temp[k] = num[j]
            k += 1
            i += 1
    while i<=mid:
        temp[k] = num[i]
        k += 1
        i += 1
    while j<=mid:
        temp[k] = num[j]
        k += 1
        j += 1
    for i in range(start, end):
        num[i] = temp[i - start]
        
        
merge_sort([5, 2, 20, 4, 6], 0, 4)
