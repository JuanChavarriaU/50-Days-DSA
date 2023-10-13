def findPair(numberList, target):
    conjunto = set()
    for i in numberList: 
      complemento = target - i
      if complemento in conjunto:
         return (i, complemento)
      conjunto.add(i)
    else:
        return -1
        
''' 
Para resolver este problema utilizamos un enfoque basado en conjuntos
en el cual creamos un conjunto para poder ir guardando los numeros 
que vemos en el recorrido. 
en la variable complemento agregamos el valor que haria falta encontrar
para completar el par de numeros. 

Digamos que tenemos un arreglo con [1,4,5,7,9,2] y un target de 3, 
en la primera pasada donde i=0
complemento = 3-1
complemento = 2
complemento(2) esta en conjunto(empty)? false
conjunto.add(1)

segunda vuelta i=1
complemento = 3-4
complemento = -1
complemento(-1) esta en conjunto(1)? false
conjunto.add(4)

...

ultima vuelta i=5
complemento = 3-2
complemento = 1
complemento(1) esta en conjunto(1,4,5,7,9)? true
    retonar (i=2, complemento=1 )

'''    

print(findPair([4,2,3,0,4,6,9,8,20],8))   

