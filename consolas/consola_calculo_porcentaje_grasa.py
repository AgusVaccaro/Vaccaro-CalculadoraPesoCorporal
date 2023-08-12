import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor correspondiente a su género (Hombres: 10.8, Mujeres: 0): "))
    
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("Su porcentaje de grasa corporal es:", porcentaje_grasa)


main()
