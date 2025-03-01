#Linear search

def linear_Search(arr,target):

    n=len(arr)

    for i in range(n):

        if arr[i]==target:
            return i

    return -1


arr=[1,2,3,4,5]

target=5

binary=linear_Search(arr,target)

print(f"the indxe of:{binary+1}" if binary!=-1 else "element not found")

    
