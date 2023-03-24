def lcm(num1, num2):
    i=1
    while(True):
        multiple = max(num1, num2)*i
        if(multiple%num1==0 and multiple%num2==0):
            return multiple
        i+=1

#_main_
while(True):
    num1 = int(input("\nEnter your 1st number = "))
    num2 = int(input("Enter your 2nd number = "))
    ans = lcm(num1, num2)
    print("LCM of {} and {} = {}".format(num1, num2, ans))

    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue