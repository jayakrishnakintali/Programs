# Assume that user types a multi digit integer that has no zero within it. Find out sum of factorial of non prime digits only..
def program_2():
    num = int(input("Enter Number: "))
    sum = 0
    while num > 0:
        temp = num % 10
        for d in range (2,(temp//2)+1):
           if temp % d == 0:
                 fact = 1
                 for n in range (2,temp + 1):
                     fact *= n
                 sum = sum + fact
           break
        else:
            pass
        num = num // 10

    print(f"Result is {sum}")
             
if __name__ == "__main__":
    program_2()