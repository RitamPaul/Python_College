def diamond(row, check=0, pat='*'):
    full, space = 0, 0
    if(check==1):
    #Everything starting from 1 as row is odd
        #Full Diamond inside single iteration of rows
        for i in range(check, row+1):
            if(i < row//2 +1):
                for sp in range(i, row//2 +1):
                    print(" "*len(pat), end=" ")
                for design in range((2*i)-1):
                    print(pat, end=" ")
                print()
            elif(i == row//2 +1):
                full = (2*i)-1
                for design in range(full):
                    print(pat, end=" ")
                print()
            else:
                space += 1
                full -= 2
                for sp in range(space):
                    print(" "*len(pat), end=" ")
                for design in range(full):
                    print(pat, end=" ")
                print()
    else:
    #Everything starting from 0 as row is even
        #Up_Triangle
        for i in range(check, row//2):
            for sp in range(i, row//2 -1):
                print(" "*len(pat), end=" ")
            for design in range((2*i)+1):
                print(pat, end=" ")
            print()
        #Down_Triangle
        full = (2*(row//2))-1
        for i in range(check, row//2):
            for sp in range(i):
                print(" "*len(pat), end=" ")
            for design in range(full):
                print(pat, end=" ")
            full -= 2
            print()
    return

#_main_
while(True):
    row = int(input("\nEnter the no. of rows of Diamond pattern = "))
    pat = str(input("Enter anything to be filled in pattern = "))
    if(pat!=""):
        diamond(row, row&1, pat)
        #Sending row is either odd/even by 'row & 1'
    else:
        diamond(row, row&1)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue