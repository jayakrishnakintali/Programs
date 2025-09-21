def arm_strong():
    num = int(input("Enter a Number: "))
    sum = 0
    temp = num
    while num > 0:
        sum = sum + (num%10)**3
        num //= 10
    #if sum == temp: print("Arm Strong Number. ") else  print("Not a Arm Strong Number. ")
    print("ArmStrong") if sum==temp else print("Not ArmString")

if __name__ == "__main__":
    arm_strong()