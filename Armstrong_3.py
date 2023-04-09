def arm():
    for num in range(1, 1001):
        duplicate = num
        sum=0
        while(num>0):
            last = num%10
            sum += (last**3)
            num = num//10
        if(sum==duplicate):
            print(sum, end=" ")

#_main_
while(True):
    print("\nThe Armstrong numbers from 1 to 10000 are :- \n")
    arm()
    
    choice = int(input("\nWant to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue