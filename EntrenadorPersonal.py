import random

# Proyecto de entrenamiento personal
# Autora: Carla González Mina


def pedirinformacion():
    print("Hola, soy tu entrenador personal")
    print("¿Cuál es tu nombre?")
    nombre = input()
    print("¿Cuál es tu edad?")
    edad = input()
    print("¿Cuál es tu peso?")
    peso = input()
    print("¿Cuál es tu estatura?")
    estatura = input()
    print("¿Cuál es tu objetivo?")
    objetivo = input()
    print("¿Cuántas veces a la semana haces ejercicio?")
    ejercicio = input()
    print("¿Cuántas horas duermes?")
    horas = input()
    print("¿Cuántos vasos de agua tomas al día?")
    agua = input()
    print("¿Cuántas comidas haces al día?")
    comidas = input()
    print("¿Cuántas veces al día comes frutas y verduras?")
    frutas = input()
    print("¿Cuántas veces al día comes proteínas?")
    proteinas = input()
    print("¿Cuántas veces al día comes carbohidratos?")
    carbohidratos = input()
    print("¿Cuántas veces al día comes grasas?")
    grasas = input()
    print("¿Cuántas veces al día comes azúcares?")
    azucares = input()
    print("¿Cuántas veces al día comes lácteos?")
    lacteos = input()
    print("¿Cuántas veces al día comes alimentos procesados?")
    procesados = input()
    print("¿Cuántas veces al día comes alimentos fritos?")
    fritos = input()
    print("¿Cuántas veces al día comes alimentos congelados?")
    congelados = input()
    print("¿Cuántas veces al día comes alimentos enlatados?")
    enlatados = input()
    print("¿Cuántas veces al día comes alimentos integrales?")
    integrales = input()


def guardarinfousuario(
    nombre,
    edad,
    peso,
    estatura,
    objetivo,
    ejercicio,
    horas,
    agua,
    comidas,
    frutas,
    proteinas,
    carbohidratos,
    grasas,
    azucares,
    lacteos,
    procesados,
    fritos,
    congelados,
    enlatados,
    integrales,
):
    archivo = open("informacionusuario.txt", "w")
    archivo.write(nombre + "\n")
    archivo.write(edad + "\n")
    archivo.write(peso + "\n")
    archivo.write(estatura + "\n")
    archivo.write(objetivo + "\n")
    archivo.write(ejercicio + "\n")
    archivo.write(horas + "\n")
    archivo.write(agua + "\n")
    archivo.write(comidas + "\n")
    archivo.write(frutas + "\n")
    archivo.write(proteinas + "\n")
    archivo.write(carbohidratos + "\n")
    archivo.write(grasas + "\n")
    archivo.write(azucares + "\n")
    archivo.write(lacteos + "\n")
    archivo.write(procesados + "\n")
    archivo.write(fritos + "\n")
    archivo.write(congelados + "\n")
    archivo.write(enlatados + "\n")
    archivo.write(integrales + "\n")


# La idea es que cada usuario tenga su archivo con su información personal
(
    nombre,
    edad,
    peso,
    estatura,
    objetivo,
    ejercicio,
    horas,
    agua,
    comidas,
    frutas,
    proteinas,
    carbohidratos,
    grasas,
    azucares,
    lacteos,
    procesados,
    fritos,
    congelados,
    enlatados,
    integrales,
) = pedirinformacion()
guardarinfousuario(
    nombre,
    edad,
    peso,
    estatura,
    objetivo,
    ejercicio,
    horas,
    agua,
    comidas,
    frutas,
    proteinas,
    carbohidratos,
    grasas,
    azucares,
    lacteos,
    procesados,
    fritos,
    congelados,
    enlatados,
    integrales,
)

# La idea es que cada usuario tenga su archivo con su información personal
# A partir de cada archivo generar entrenamiento adecuado


def calcularentrenamiento(usuario):
    if usuario == "bajo peso":
        print("Tu objetivo es subir de peso")
        print("Tu entrenamiento será el siguiente")
        print(
            "Día 1: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 2: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 3: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 4: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 5: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 6: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print("Día 7: Descanso")
    elif usuario == "sobrepeso":
        print("Tu objetivo es bajar de peso")
        print("Tu entrenamiento será el siguiente")
        print(
            "Día 1: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 2: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 3: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 4: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 5: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 6: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print("Día 7: Descanso")
    elif usuario == "tonificar":
        print("Tu objetivo es tonificar")
        print("Tu entrenamiento será el siguiente")
        print(
            "Día 1: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 2: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 3: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 4: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 5: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print(
            "Día 6: 30 minutos de cardio, 3 series de 10 repeticiones de sentadillas, 3 series de 10 repeticiones de lagartijas, 3 series de 10 repeticiones de abdominales"
        )
        print("Día 7: Descanso")
    else:
        print("No se ha encontrado un entrenamiento adecuado")
