#paso 1: declaracion de variables
Frase = ["Elizabeth" , "resendiz" , "amaro"] #Lista palabra en orden correcto
lista_desordenada= []#Lista desordenada 
lista_ordenada=[] #Lista ordenada

#paso 2: manipulacion de archivos
archivo= open("frase.txt", "r") #Lectura y mandas a traer el archivo

# paso 3: Vamos a leer los datos del txt
for linea in archivo.readlines():
    lista_desordenada.append(linea)

print("----------------------Aqui esta la frase del txt-----------------------------")
print(lista_desordenada)
print("*************************************************************")

#paso 4: procesos de datos
#vamos a comparar la lista que esta bien y la lista que este bien
for lista in Frase:
    for lista2 in lista_desordenada:
        if lista in lista2:
            lista_ordenada.append(lista)

#paso 5: Imprimos los resultados (Lista ordenada) 

print("----------------------------------Frase ordenada-------------------------")
print(lista_ordenada)
print("**************************************************************************")


