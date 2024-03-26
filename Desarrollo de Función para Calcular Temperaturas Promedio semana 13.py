#Desarrolla una función en Python que c La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.

temperaturas = [
    [#GUAYAQUIL
        [#SEMANA 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 28},
            {"day": "Miercoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sabado", "temp": 30},
            {"day": "Domingo", "temp": 28}

        ],
        [#SEMANA 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 26},
            {"day": "Miercoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 26},
            {"day": "Sabado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [#SEMANA 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miercoles", "temp": 27},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sabado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [#SEMANA 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miercoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sabado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [# QUITO
        [#SEMANA 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 16},
            {"day": "Miercoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sabado", "temp": 7},
            {"day": "Domingo", "temp": 19}
        ],
        [#SEMANA 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 17},
            {"day": "Miercoles", "temp": 20},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sabado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ],
        [#SEMANA 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miercoles", "temp": 20},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sabado", "temp": 16},
            {"day": "Domingo", "temp": 18}
        ],
        [#SEMNA 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miercoles", "temp": 30},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sabado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [#RIOBAMBA
        [#SEMANA 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 14},
            {"day": "Miercoles", "temp": 10},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 15},
            {"day": "Sabado", "temp": 14},
            {"day": "Domingo", "temp": 16}
        ],
        [#SEMNA 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miercoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sabado", "temp": 16},
            {"day": "Domingo", "temp": 14}
        ],
        [#SEMANA 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 14},
            {"day": "Miercoles", "temp": 10},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 17},
            {"day": "Sabado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ],
        [#SEMANA 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miercoles", "temp": 20},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sabado", "temp": 15},
            {"day": "Domingo", "temp": 17}
        ]

    ]
]


ciudades = ["GUAYAQUIL", "QUITO", "RIOBAMBA"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
      suma_temperaturas = sum([dia["temp"]for dia in semana])
      promedio = suma_temperaturas / len(semana)
      print(f"Promedio de Temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
      promedio_mensual = round(promedio / len(semana), 1)
      print(f'PROMEDIO MENSUAL: {promedio_mensual}')