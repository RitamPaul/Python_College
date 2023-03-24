def check(num):
    if(num & 1 == 1):
        return "Odd"
    return "Even"

#_main_
while(True):
    num = int(input("\nEnter your number = "))
    ans = check(num)
    print("You number is = ",ans)
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue