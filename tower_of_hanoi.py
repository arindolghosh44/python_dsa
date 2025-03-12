def tower_of_hanoi(n,source,destination,aux):
    if n==1:
        print(f" move disk 1 {source} to  {destination}")
        return

    tower_of_hanoi(n-1,source,aux,destination)
    print(f"move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1,aux,destination,source)




n=3
tower_of_hanoi(n,'A','C','B')
