def calcular_IMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    porcentaje_grasa = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
    return porcentaje_grasa

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    tmb = (10 * peso) + (6.25 * altura * 100) - (5 * edad) + valor_genero
    return tmb

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividad = tmb * valor_actividad
    return tmb_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = int(tmb * 0.8)
    rango_superior = int(tmb * 0.85)
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior} y {rango_superior} calorías al día."

