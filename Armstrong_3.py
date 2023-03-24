def arm(num):
    duplicate = num
    sum=0
    while(num>0):
        last = num%10
        sum += (last**3)
        num = num//10
    return sum==duplicate

#_main_
while(True):
    num = int(input("\nEnter your integer number = "))
    ans = arm(num)
    if(ans):
        print("Yes, your number is armstrong number")
    else:
        print("Your number is not armstrong number")
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue