def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
z=fact(4)
print(z)
