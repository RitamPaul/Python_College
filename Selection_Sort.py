def selection(li):
    n = len(li)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if(li[j] < li[min_index]):
                min_index = j
        li[min_index], li[i] = li[i], li[min_index]
    return

#_main_
while(True):
    li = list(map(float, input("\nEnter the array items = ").strip().split()))
    selection(li)
    print("Selection sorted array(ascending order) = ", li)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue