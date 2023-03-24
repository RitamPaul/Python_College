def hcf(num1, num2):
    divisor = min(num1, num2)
    dividend = max(num1, num2)
    rem=0
    while(True):
        rem = dividend % divisor
        if(rem == 0):
            break
        else:
            dividend = divisor
            divisor = rem
    return divisor

#_main_
while(True):
    num1 = int(input("\nEnter your 1st number = "))
    num2 = int(input("Enter your 2nd number = "))
    ans = hcf(num1, num2)
    print("GCD of {} and {} = {}".format(num1, num2, ans))

    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue