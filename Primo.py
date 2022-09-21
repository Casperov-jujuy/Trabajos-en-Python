def primo (n):
    dev = 0
    for z in range (1,n+1):
            if n % z == 0:
             dev = dev +1;     
    return dev

def main ():
    n = int (input ("ingrese un numero: "))
    dev= primo (n)
    if  dev==2:
        print ('es primo')
    else:
        print ('no es primo')

main ()
