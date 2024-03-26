# Crear una matriz 3D que represente los datos de temperatures diaries en varias ciudades.
# en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.)
# en la tercera dimensión, semanas.

print("Temperaturas mes de Febrero")

temperaturas = [ # Temperaturas mes de Febrero

  [ #GUAYAQUIL
    [ #semana1
      {"day":"lunes", "temp": 28},
      {"day": "Martes", "temp": 29},
      {"day": "Miércoles", "temp": 30},
      {"day": "Jueves", "temp": 28},
      {"day": "Viernes", "temp": 27},
      {"day": "Sábado", "temp": 30},
      {"day": "Domingo", "temp": 32}
    ],
    [# seman 2
      {"day": "Lunes", "temp": 32},
      {"day": "Martes", "temp": 28},
      {"day": "Miércoles", "temp": 29},
      {"day": "Jueves", "temp": 27},
      {"day": "Viernes", "temp": 26},
      {"day": "Sábado", "temp": 28},
      {"day": "Domingo", "temp": 32}
    ],
    [#semana 3
      {"day": "Lunes", "temp": 28},
      {"day": "Martes", "temp": 27},
      {"day": "Miércoles", "temp": 30},
      {"day": "Jueves", "temp": 29},
      {"day": "Viernes", "temp": 27},
      {"day": "Sábado", "temp": 28},
      {"day": "Domingo", "temp": 29}
    ],
    [ # Semana 4
      {"day": "Lunes", "temp": 28},
      {"day": "Martes", "temp": 30},
      {"day": "Miércoles", "temp": 32},
      {"day": "Jueves", "temp": 31},
      {"day": "Viernes", "temp": 29},
      {"day": "Sábado", "temp": 30},
      {"day": "Domingo", "temp": 31}
    ]
  ],
  [ # QUITO
    [# semana 1
      {"day": "Lunes", "temp": 16},
      {"day": "Martes", "temp": 18},
      {"day": "Miércoles", "temp": 16},
      {"day": "Jueves", "temp": 19},
      {"day": "Viernes", "temp": 17},
      {"day": "Sábado", "temp": 18},
      {"day": "Domingo", "temp": 19}
    ],
    [ # semana 2
      {"day": "Lunes", "temp": 19},
      {"day": "Martes", "temp": 18},
      {"day": "Miércoles", "temp": 17},
      {"day": "Jueves", "temp": 19},
      {"day": "Viernes", "temp": 18},
      {"day": "Sábado", "temp": 18},
      {"day": "Domingo", "temp": 19}
    ],
    [  # Semana 3
      {"day": "Lunes", "temp": 18},
      {"day": "Martes", "temp": 19},
      {"day": "Miércoles", "temp": 16},
      {"day": "Jueves", "temp": 15},
      {"day": "Viernes", "temp": 17},
      {"day": "Sábado", "temp": 18},
      {"day": "Domingo", "temp": 19}
    ],
    [ # Semana 4
      {"day": "Lunes", "temp": 17},
      {"day": "Martes", "temp": 18},
      {"day": "Miércoles", "temp": 16},
      {"day": "Jueves", "temp": 17},
      {"day": "Viernes", "temp": 16},
      {"day": "Sábado", "temp": 17},
      {"day": "Domingo", "temp": 16}
    ]
  ],
  [ # CUENCA
    [ # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
    ],
    [   # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
    ],
    [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 18}
    ],
    [ # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
    ]
  ]
]

# calcular el promedio de temperaturas para una ciudad por cada una de las semanas

ciudades = ["GUAYAQUIL", "QUITO", "CUENCA"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
      suma_temperaturas = sum([dia["temp"]for dia in semana])
      promedio = suma_temperaturas / len(semana)
      print(f"Promedio de Temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")