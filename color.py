def  disp_color():
    color = int(input("Enter Color code: "))
    match color:
        case 0 :
            print("Red")
        case 1 :
            print("Green")
        case 2 :
            print("Blue")
        case _ :
            print("Invalid Code")
if __name__ == "__main__":
    disp_color()