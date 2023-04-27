def InsertionSort():
    for i in range(0, len(li)-1):
        if(li[i] > li[i+1]):
            li[i], li[i+1] = li[i+1], li[i]
            for j in range(i, 0, -1):
                if(li[j] < li[j-1]):
                    li[j], li[j-1] = li[j-1], li[j]
                else:
                    break

li = list(map(float, input("Enter your array = ").strip().split()))
InsertionSort()
print("Insertion sorted array =",li)