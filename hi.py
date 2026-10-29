total = 0
while True:
    number = int(input("Enter an integer (0 to stop): ") )
    total += number
    if number == 0:
        print("total:", total)
        break;
