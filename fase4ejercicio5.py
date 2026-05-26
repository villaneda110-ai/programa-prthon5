trabajadores = [
    ["ana",8,8,8,8,15],
    ["pedro",3,4,8,7,8],
    ["julian",6,7,8,9,6],
    ["juana",7,7,7,7,7]
]

def calcular_jornada(trabajador):
    nombre = trabajador[0]
    horas_trabajadas = trabajador[1:]
    total = sum(horas_trabajadas)
    
    if total > 40:
        clasificacion = "jornada en sobretiempo"
    else:
        clasificacion = "jornada normal :)"
    
    return nombre, total, clasificacion

print("HORAS LABORADAS")
print("**" * 20)

for trabajador in trabajadores:
    nombre, total, clasificacion = calcular_jornada(trabajador)
    print(f"{nombre}")
    print(f"Total de horas trabajadas: {total}")
    print(f"Clasificación: {clasificacion}")    
    print("**" * 20)