#Crea un nuevo archivo llamado my_notes.txt.

file_name = "my_notes.txt"
#modo de aperura para escritura
archivo_escritura = open(file_name, "w")
#Escribe al menos tres líneas de notas personales en el archivo.
archivo_escritura.write("linea 1: Deberes de ingles.\n")
archivo_escritura.write("linea 2: Tarea semana 15.\n")
archivo_escritura.write("linea 3: Examen final.\n")

# Cierre del archivo de escritura
archivo_escritura.close()

#modo de apertura para lectura
archivo_lectura = open(file_name, "r")

#Metodo readline: lee una linea a la vez
archivo_lectura.seek(0) #Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()

#Muestra en la consola cada línea leída.
print("\nMuestra del Contenido linea por linea():")
print(linea_1.strip())
print(linea_2.strip())
print(linea_3.strip())

#Cierre del archivo de lectura
archivo_lectura.close()



