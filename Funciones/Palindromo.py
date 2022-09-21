def palindromo (palabra):
    palabra = palabra.replace (' ','')
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    


def main ():
    palabra = input ('ingrese una palabra: ')
    es_palindromo = palindromo(palabra)
    
    if es_palindromo :
        print  ('Es palindromo')
    else:
        print ("no es palidromo")

# punto de entrada de la aplicacion
if __name__ == '__main__':
    main()