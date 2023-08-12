import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = int(input("Ingrese el valor correspondiente a su género (hombres: 5, mujeres: -161): "))
    
    rango_calorias = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print (rango_calorias)

main()
