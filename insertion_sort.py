def insertion_sort(arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


arr=[6,1,7,4,2,9,8,5,3,0,-1,-8,0,6,6,89,-90]

ff=insertion_sort(arr)

print("sorted array:",ff)
    
