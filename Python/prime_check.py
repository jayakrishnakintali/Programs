def prime_check():
    n = int(input("Enter an integer: "))
    for i in range(2,n//2+1):
        if n % i == 0:
            print("Not a Prime Number. ")
            break
    else:
        print("Prime Number.") 
if __name__ == "__main__":
    prime_check()