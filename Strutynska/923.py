a=int(input())
if a>12:
    print("вхідні дані не підходять")
else:
    if a == 1 or a == 2 or a == 12:
        print("Winter")
    elif a == 3 or a == 4 or a == 5:
        print("Spring")
    elif a == 6 or a == 7 or a == 8:
        print("Summer")
    else:
        print("Autumn")