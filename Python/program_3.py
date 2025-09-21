def program_3():
    num = int(input("Enter the number: "))
    sum = 0
    num//=10
    while num > 9:
        sum = sum + num % 10
        num = num // 10

    print(sum)
if __name__ == "__main__":
    program_3()