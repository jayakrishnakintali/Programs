def pattern_8():
    for i in range(1,6):
        for j in range(1,6):
            if i == j:
                print("1",end = ' ')
            else:
                print("0",end = ' ')
        print()
pattern_8()