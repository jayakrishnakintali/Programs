def pattern_11():
    for i in range(1,6):
        for j in range(1,6):
            if (i==j) or (i+j==6):
                print("1",end = ' ')
            else:
                print("0",end = ' ')
        print()
pattern_11()