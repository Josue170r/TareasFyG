def is_anumber(number):
    numero = int(number)
    if type(numero) == int:
        return True
    else: 
        return False
    
def palindromo(number, line):
    
    n=0
    if(line == True):
        numero = str(number)
        numero2 = numero
        j = len(numero2)-1
        tam = j
        for i in range(j):
            if(numero[i] == numero2[j]):
                j -=1
                n +=1   
                print(f"i:{i}")
                print(f"j:{j}")
                print(f"n:{n}")
    else: 
        print("Error...Tipo de dato inválido")
    if(n == tam):
        return True
    else:
        return False
    
    
    

if __name__ == '__main__':
    number = input("Ingresa un número: ")
    line = is_anumber(number)
    if (palindromo(number, line) == True):
        print("El número es un palíndromo")
    else:
        print("El número no es un palíndromo")