import calculadora_indices as calc

def main():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    valor_genero = float(input("Ingrese el valor correspondiente a su género (Hombres: 5, Mujeres: -161): "))
    valor_actividad = float(input("Ingrese el valor correspondiente a su nivel de actividad fisica semanal. (1.2: poco o ningún ejercicio - 1.375: ejercicio ligero (1 a 3 días a la semana) - 1.55: ejercicio moderado (3 a 5 días a la semana) - 1.72: deportista (6 -7 días a la semana) - 1.9: atleta (entrenamientos mañana y tarde.)): "))
     
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print("La cantidad de calorias que quema estando en actividad es: ", calorias_actividad)
main()
