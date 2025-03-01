def Bubble_sort(arr,n):
   
    for i in range(n):
        swap=False
        for j in range (n-i-1):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if swap is not True:
                break


    return arr



arr=[9,8,1,2,7,3,6,4,5]

sorted_arr = Bubble_sort(arr,len(arr))
print("Sorted array:", sorted_arr)
        
