def sum_natural():   
    x = int(input("Enter a number: "))
    sum = 0    
    for i in range(1, x+1):
     sum = sum + i
    print(f"sum is {sum}")
if __name__ == "__main__":
    sum_natural()


   