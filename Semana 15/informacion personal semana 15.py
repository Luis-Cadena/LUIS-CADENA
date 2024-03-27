# Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion"

informacion_personal = {
                'nombre': 'Luis',
                'edad': 29,
                'ciudad': 'Quito',
                'provincia': 'Pichincha',
}
print('____________________')
print('Información Personal')
print('_____________________')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Quito'
informacion_personal['provincia'] = 'Pichincha'

# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.

informacion_personal['profesion'] = 'Militar'

# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0960879232'

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
# del informacion_personal['edad']
informacion_personal.pop('edad')

# Imprime el diccionario resultante después de realizar todas las operaciones.

print('______________________')
print('Diccionario Modificado')
print('______________________')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')
