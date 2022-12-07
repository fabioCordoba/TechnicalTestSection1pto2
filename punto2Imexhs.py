#Respesta 2:

#test de prueba

#https://github.com/fabioCordoba/TechnicalTestSection1pto2-.git

entrada = []

#este metodo se encarga de sumar los valores de cada sub-array
def sumaArreglo(arr):
    suma = 0
    for x in arr:
        suma = suma + x
    return suma

def subArreglo(entrada):
    print('\ninput: {} \n'.format(entrada))
    long = len(entrada)
    #Variable long, almacena la longitud de la matriz de entrada
    mitad = int(long / 2)
    #Variable mitad divide la longitud del array de entrada para definir el tamaño de casa sub-array
    iteraciones = 0

    arrIzq = entrada[:mitad]
    #arrIzq almacena el sub-array izquierdo, que son los valores desde la posicion inicial del array entrada
    #hasta la posicion media de este usando la variable mitad
    
    arrCent = entrada[mitad-1:mitad*2-1]
    #arrCent almacena el sub-array central, conformado por los valores que
    #estan desde la posicion media -1 hasta la posicion media multiplicaa por dos -1
    
    arrDer = entrada[mitad+1:]
    #arrDer almacena el sub-array Derecho, conformado por los valores que estan desde la posicion media +1 hasta la ultima posicion

    #print('arrIzq : {} \narrCent: {} \narrDer : {}\n'.format(arrIzq, arrCent, arrDer))
    #este print anterion muestra los 3 sub arrays
    
    suma = 0
    array = []
    
    for x in range(3):
        #mediante este for selecciono cada sub-array y comparo la suma total de sus valores y asi quedarme con el mayor resultado
        iteraciones = iteraciones + 1
        if(iteraciones == 1):
            #la primer iterecion empieza sumando los valores del primer sub array
            #y se almacenan en variables suma y array 
            suma = sumaArreglo(arrIzq)
            array = arrIzq
        elif(iteraciones == 2):
            #con la segunda iteracion valido si la suma de los valores del sub-array central (temp)
            #es mayor a la variable suma, de ser cierto los nuevos valores de suma y array corresponderan a los del sub-array central
            temp = sumaArreglo(arrCent)
            if(temp > suma):
                suma = temp
                array = arrCent
        else:
            #con la tercera y ultima iteracion valido si la suma de los valores del sub-array Derecho(temp)
            #es mayor a la variable suma, de ser cierto los nuevos valores de suma y array corresponderan a los del sub-array Derecho
            temp = sumaArreglo(arrDer)
            if(temp > suma):
                suma = temp
                array = arrCent
    #imprime el resultado
    print('{} tiene la mayor suma = {}'.format(array, suma))
       

n=int(input("long del array: "))
#pide al usuario una longitud para el array de entrada

for x in range(n):
    v=int(input("ingrese valor: "))
    #pide al usuario que ingrese los valores para el array
    entrada.append(v)

subArreglo(entrada)
#metodo para calcuar los sub-arrays


