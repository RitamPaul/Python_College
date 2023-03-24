def bubble(li):
    n = len(li)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if(li[j] > li[j+1]):
                li[j], li[j+1] = li[j+1], li[j]
    return

#_main_
while(True):
    li = list(map(int, input("\nEnter the array items = ").strip().split()))
    bubble(li)
    print("Bubble sorted array(ascending order) = ", li)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue