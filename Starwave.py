b = int(input("How wide do you want it: "))
c = int(input("How many waves: "))


count = 1
while(c >= count):
    print(count)
    print(b)
    print(c)
    count += 1
    while(b >= count):
        count += 1
        print("*" * count)
    while(count > 0):
        count -= 1
        print("*" * count)
