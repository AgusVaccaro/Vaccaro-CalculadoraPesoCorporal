import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = calc.calcular_IMC(peso, altura)
    print("Su índice de masa corporal (IMC) es:", imc)
    
    if imc < 16:
        categoria = "Delgadez severa"
    elif imc < 17:
        categoria = "Delgadez moderada"
    elif imc < 18.5:
        categoria = "Delgadez aceptable"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidad tipo I"
    elif imc < 40:
        categoria = "Obesidad tipo II"
    elif imc < 50:
        categoria = "Obesidad tipo III o mórbida"
    else:
        categoria = "Obesidad tipo IV o extrema"
    
    print("Categoría: ", categoria)


main()
