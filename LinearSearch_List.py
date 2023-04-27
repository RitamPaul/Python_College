def find(num):
    for i in range(0, len(li)):
        if(li[i]==num):
            print("Your searched item is found at index =",i)
            return
    print("Your searched item is not found")

li = list(map(float, input("Enter your array = ").strip().split()))
num = float(input("Enter the number to be searched = "))
find(num)