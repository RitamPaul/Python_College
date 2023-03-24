def right(row):
    for i in range(1, row+1):
        for j in range(i):
            print("*", end=" ")
        print()
    return

#_main_
while(True):
    row = int(input("\nEnter the no. of rows of Right Angled Triangle pattern = "))
    right(row)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue