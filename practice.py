n = float(input("Type a number: "))

op = input("Type either a '*' or a '+' to choose to multiply or add: ")

if (op == "+"):
    sum = 0
    i = 1
    while (i <= n):
        sum += i
        i += 1
    print(sum)
elif (op == "*"):
    product = 1
    i = 1
    while (i <= n):
        product *= i
        i += 1
    print(product)
else:
    print("Invalid operation")