def gcd(a,b):
    for x in range(min(a,b), 0, -1):
        if (a%x == 0) and (b%x == 0): return x
    return 1

a = int(input("a= "))
b = int(input("\nb= "))
print("\nGCD= "+str(gcd(a,b)))

