# def splitStr(list_str):
#    count = len(list_str)-1
#    s_index = 0
#    while s_index < count:
#       if list_str[s_index] != list_str[count]:
#          list_str[s_index],list_str[count] = list_str[count],list_str[s_index]
#          s_index += 1
#          count -= 1
#       else:
#          s_index+=1
#          count-=1
#    return list_str
#
# str1=['1','2','3','4']
# print(splitStr(str1))


for i in range(0,7-7-1):
    print(i)


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, 6 - i-1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])