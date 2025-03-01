def selection_sort(arr,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr




arr=[9,1,8,2,7,3,6,4,5,-7,0]

sorted_arr = selection_sort(arr,len(arr))
print("Sorted array:", sorted_arr)
