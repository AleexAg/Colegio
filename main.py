#Funcion para obtener el asistente y el profesor
def compañeros_clase(num):
    #Creamos la matriz que almacenara a los alumnos presentes
    compañeros = []

    #Recorremos la cantidad de alumnos presente
    for i in range(num):
        #Guardamos los datos de los alumnos presente
        nombre = input('Ingrese el nombre del alumno: ')
        edad = int(input('Ingrese la edad: '))

        #Cramos una variable que guarde los datos del nombre y la edad y los agregamos a la matriz
        compañero = (nombre, edad)
        compañeros.append(compañero)
    
    #Ordenamos la matriz utilizando la funcion lambda
    compañeros.sort(key=lambda x:x[1]) # ORDENA LA MATRIZ

    #Segun lo indicado la primer posicion es del asistente y la ultima es del profesor entonces se guarda en variables
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    # Por ultimos retornamos la informacion
    return asistente, profesor


def principal():
    print('-' * 50)
    print('|  Bienvenido al programa del colegio de los pibes  |')
    print('-> Debe ingresar primero el nombre del asistente\n'
          '-> Por ultimo debe ingresarse el nombre del profesor')
    print('-' * 50)
    cantidad = int(input('Ingrese la cantidad de alumnos que fueron a clases: '))
    asistente, profesor = compañeros_clase(cantidad)

    print('El asistente de la clase es:', asistente)
    print('El profesor de la clase es:', profesor)

if __name__ == '__main__':
    principal()
