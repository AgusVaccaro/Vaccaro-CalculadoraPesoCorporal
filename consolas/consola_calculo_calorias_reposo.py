import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor correspondiente a su género (Hombres: 5, Mujeres: -161): "))
    
    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorias que quema estando en reposo es: ", calorias_reposo)

main()