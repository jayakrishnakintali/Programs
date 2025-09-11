""" 
WAP to display grade of a student based on input mark as given below
0 - 29 : F Grade
30 - 49 : D Grade
50 - 69 : C Grade
70 - 89 : B Grade
90 - 100 : A Grade 
"""


def show_grade():
    mark  = int(input("Enter Mark: "))
    if(mark >= 0) and (mark<30):
        print("F Grade")
    elif(mark < 50):
        print("D Grade")
    elif(mark < 70):
        print("C Grade")
    elif(mark < 90):
        print("B Grade")
    elif(mark<=100):
        print("A Grade")
    else:
        print("Invalid Mark")
        #if user types 105,-20

if __name__=="__main__":
        show_grade()
