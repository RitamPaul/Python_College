#_main_
while(True):
    num = int(input("\nEnter your natural number = "))
    sum=0
    li=[]
    for i in range(1, num):
        if(num % i == 0):
            sum += i
            li.append(i)
    if(sum == num):
        print("Your Number is perfect Number")
        print("And its divisors =", li)
    else:
        print("Your number is not perfect number")
    
    choice = int(input("Want to continue? (1/0) = "))
    if(choice==0):
        print("---> Come again later <---")
        break
    continue