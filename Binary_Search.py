def BinarySearch(li, item):
    i, j, mid = 0, len(li)-1, 0
    while(i<=j):
        mid = (i+j)//2
        if(li[mid] == item):
            return mid
        elif(li[mid] > item):
            j = mid-1
        elif(li[mid] < item):
            i = mid+1
    return -1

#_main_
while(True):
    li = list(map(float, input("\nEnter the sorted unique array items = ").strip().split()))
    item = float(input("Enter the element to be searched for = "))
    ans = BinarySearch(li, item)
    if(ans == -1):
        print("The searched element is not found")
    else:
        print("The searched element is found at array index = ", ans)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue