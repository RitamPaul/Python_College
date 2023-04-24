#_main_
while(True):
    li = list(map(float, input("\nEnter the sorted unique array items = ").strip().split()))
    i, j = 0, 0
    while(i < len(li)-1):
        j=i+1
        dupli = False
        while(j < len(li)):
            if(li[i] == li[j]):
                dupli = True
                li.pop(j)
                continue
            j+=1
        if(dupli == False):
            i+=1
    print("Your new list after removing duplicates = ", li)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue
