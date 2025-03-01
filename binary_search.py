#binary search with loop
"""
def binary_search(arr,target):

    left, right = 0, len(arr) - 1

    while left<=right:
        mid=left+(right-left)//2

        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1


arr=[1,2,3,4,5]

target=5

binary=binary_search(arr,target)

print(f"the indxe of:{binary+1}" if binary!=-1 else "element not found")

"""

#binary search with recursion

def binary_search (arr,left,right,target):

    if left>right:
        return -1

    mid=left+(right-left)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] <target:
        return binary_search(arr,mid+1,right,target)
    else:
         return binary_search(arr,left,mid-1,target)


arr=[1,2,3,4,5]

target=5

binary=binary_search(arr,0,len(arr)-1,target)

print(f"the indxe of:{binary+1}" if binary!=-1 else "element not found")
