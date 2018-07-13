def Addition():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    sum = a + b
    print(sum)

def Subtraction():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    difference = a - b
    print(difference)

def Multiplication():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    c = 0
    count = 0
    while(count < b):
        count += 1
        c += a
    product = c
    print(product)

def Division():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    count = 0
    while(a >= b):
        count += 1
        a -= b
    quotient = count
    print(quotient)

def Exponent():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    c = 1
    count = 0
    while(count < b):
        count += 1
        c *= a
    power = c
    print(power)

def Modulo():
    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))
    count = 0
    while(a >= b):
        count += 1
        a -= b
    remainder = a
    print(remainder)

def Minmax():
    lst = []
    active = True
    while active == True:
        i = int(input("Enter numbers: "))
        h = input("To stop adding enter 'stop'. To continue enter 'continue'.")
        lst.append(i)
        if h == 'stop':
            active = False
        elif h == 'continue':
            active = True
    sort = sorted(lst)
    print(sort)
    print("The minimum number of this list is " + str(sort[0]))
    print("The maximum number of this list is " + str(sort[-1]))

def Bintodec():
    count = 0
    ans = 0
    i = int(input("Enter binary: "))
    while i > 0:
        length = len(str(i)) - 1
        num1 = 10 ** length
        i -= num1
        ans += 2 ** length
        count += 1
    print(ans)

def Bintooc():
    number = input("Enter Binary: ")
    [left, right] = number.split(".")

    output = ""
    output2 = ""

    if len(left) % 3 == 1:
        left = "00" + left
    elif len(left) % 3 == 2:
        left = "0" + left

    if len(right) % 3 == 1:
        right = right + "00"
    elif len(right) % 3 == 2:
        right = right + "0"

    for value in range(0, len(left), 3):
        cur_group = left[value: value + 3]
        if cur_group == "000":
            output = output + "0"
        elif cur_group == "001":
            output = output + "1"
        elif cur_group == "010":
            output = output + "2"
        elif cur_group == "011":
            output = output + "3"
        elif cur_group == "100":
            output = output + "4"
        elif cur_group == "101":
            output = output + "5"
        elif cur_group == "110":
            output = output + "6"
        elif cur_group == "111":
            output = output + "7"

    for value in range(0, len(right), 3):
        cur_group = right[value: value + 3]
        if cur_group == "000":
            output2 = output2 + "0"
        elif cur_group == "001":
            output2 = output2 + "1"
        elif cur_group == "010":
            output2 = output2 + "2"
        elif cur_group == "011":
            output2 = output2 + "3"
        elif cur_group == "100":
            output2 = output2 + "4"
        elif cur_group == "101":
            output2 = output2 + "5"
        elif cur_group == "110":
            output2 = output2 + "6"
        elif cur_group == "111":
            output2 = output2 + "7"

    print(output + "." + output2)

def Bintohex():
    number = input("Enter Binary: ")
    [left, right] = number.split(".")
    output = ""
    output2 = ""

    if len(left) % 4 == 1:
        left = "000" + left
    elif len(left) % 4 == 2:
        left = "00" + left
    elif len(left) % 4 == 3:
        left = "0" + left

    if len(right) % 4 == 1:
        right = right + "000"
    elif len(right) % 4 == 2:
        right = right + "00"
    elif len(right) % 4 == 3:
        right = "0" + right

    for value in range(0, len(left), 4):
        cur_group = left[value: value + 4]
        if cur_group == "0000":
            output = output + "0"
        elif cur_group == "0001":
            output = output + "1"
        elif cur_group == "0010":
            output = output + "2"
        elif cur_group == "0011":
            output = output + "3"
        elif cur_group == "0100":
            output = output + "4"
        elif cur_group == "0101":
            output = output + "5"
        elif cur_group == "0110":
            output = output + "6"
        elif cur_group == "0111":
            output = output + "7"
        elif cur_group == "1000":
            output = output + "8"
        elif cur_group == "1001":
            output = output + "9"
        elif cur_group == "1010":
            output = output + "A"
        elif cur_group == "1011":
            output = output + "B"
        elif cur_group == "1100":
            output = output + "C"
        elif cur_group == "1101":
            output = output + "D"
        elif cur_group == "1110":
            output = output + "E"
        elif  cur_group == "1111":
            output = output + "F"


    for value in range(0, len(right), 4):
        cur_group = right[value: value + 4]
        if cur_group == "0000":
            output2 = output2 + "0"
        elif cur_group == "0001":
            output2 = output2 + "1"
        elif cur_group == "0010":
            output2 = output2 + "2"
        elif cur_group == "0011":
            output2 = output2 + "3"
        elif cur_group == "0100":
            output2 = output2 + "4"
        elif cur_group == "0101":
            output2 = output2 + "5"
        elif cur_group == "0110":
            output2 = output2 + "6"
        elif cur_group == "0111":
            output2 = output2 + "7"
        elif cur_group == "1000":
            output2 = output2 + "8"
        elif cur_group == "1001":
            output2 = output2 + "9"
        elif cur_group == "1010":
            output2 = output2 + "A"
        elif cur_group == "1011":
            output2 = output2 + "B"
        elif cur_group == "1100":
            output2 = output2 + "C"
        elif cur_group == "1101":
            output2 = output2 + "D"
        elif cur_group == "1110":
            output2 = output2 + "E"
        elif  cur_group == "1111":
            output2 = output2 + "F"

    print(output + "." + output2)


Operator = input("1.Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Exponent, 6.Modulo, 7.Minmax, 8.BintoDecimal, 9.BintoOctal, 10.BinarytoHex: ")
if Operator == "1":
    Addition()
elif Operator == "2":
    Subtraction()
elif Operator == "3":
    Multiplication()
elif Operator == "4":
    Division()
elif Operator == "5":
    Exponent()
elif Operator == "6":
    Modulo()
elif Operator == "7":
    Minmax()
elif Operator == "8":
    Bintodec()
elif Operator == "9":
    Bintooc()
elif Operator == "10":
    Bintohex()
