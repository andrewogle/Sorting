# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a_index = 0
    b_index = 0
    # TO-DO
    for i in range(0,elements):
        # if no more elements in arrA then add elements from arrB
        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[i] = arrB[b_index]
            b_index +=1
    return merged_arr
print(merge([4, 1,3,2],[5,6,7,8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)
    return arr

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
