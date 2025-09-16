def pattern_12():
    for i in range(1,6):
        for j in range(1,6):
            if(i == j or i == j - 1 or i == j + 1):
                print(1,end = ' ')
            else:
                print(0,end = ' ')
        print()
pattern_12()
