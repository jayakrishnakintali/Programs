def pattern_6():
    for i in range(1,6):
        for j in range(1,6):
            print("1",end = ' ') if i%2==1 else print("0",end = ' ')
        print()
pattern_6()
