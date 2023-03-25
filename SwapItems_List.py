def change(li, pos1, pos2):
    li[pos1], li[pos2] = li[pos2], li[pos1]
    return li

#_main_
while(True):
    li = list(map(float, input("\nEnter the array items = ").strip().split()))
    pos1 = int(input("Enter the 1st index for swapping = "))
    pos2 = int(input("Enter the 2nd index for swapping = "))
    print("After swapping the final array = ", change(li, pos1, pos2))
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue