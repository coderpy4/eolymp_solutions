a=int(input())
if a/10000 >= 1 or a/1000 < 1:
    print("вхідні дані не підходять")
else:
    print(a//1000 + a%10)