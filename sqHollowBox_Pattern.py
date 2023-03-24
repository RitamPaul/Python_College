def hollow_box(row, pat='$'):
    for i in range(row):
        if(i==0 or i==row-1):
            for design in range(row):
                print(pat, end=" ")
            print()
        else:
            for j in range(row):
                if(j==0 or j==row-1):
                    print(pat, end=" ")
                else:
                    print(" "*len(pat), end=" ")
            print()
    return

#_main_
while(True):
    row = int(input("\nEnter side length of Hollow Square pattern = "))
    pat = str(input("Enter anything to be filled in pattern = "))
    if(pat!=""):
        hollow_box(row, pat)
    else:
        hollow_box(row)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue