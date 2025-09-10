"""
WAP to calculate tax based on slabs given below
INCOME:
0 - $10000 - 10%
$10001 - $20000 - 20% on rest amount
> $20000 - 30% on rest amount
"""

def cal_salltax():
    tax = 0
    salary = int(input("Enter the salary: "))
    if salary > 0 and salary <= 10000:
      tax = tax + (salary * 0.1)
    elif salary <= 20000:
      tax = tax + 1000 + ((salary -10000)*0.2)
    else:
      tax = tax + 3000 +((salary -20000)*0.3)
    print(f"Salary:${salary}, Tax:${tax}")
if __name__=="__main__":
    cal_salltax()
   
    
     