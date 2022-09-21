def Factorial(n):
    print ('valor inicial => ',n)

    if n>1:
        n= n* Factorial(n-1)
    print ('valor final => ',n)
    return n


z = int (input('ingrese un numero: '))
f= Factorial (z)
print ('su factorial es: ',f)
