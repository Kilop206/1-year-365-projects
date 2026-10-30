def c_to_f(temperatura) :
	return temperatura * (9/5) + 32
	
def c_to_k(temperatura) :
	return temperatura + 273.15

def f_to_c(temperatura) :
	return (temperatura - 32) * (5/9)

def f_to_k(temperatura) :
	return (temperatura - 32) * (5/9) + 273.15

def k_to_c(temperatura) :
	return temperatura - 273.15

def k_to_f(temperatura) :
	return (temperatura - 273.15) * (9/5) + 32 
		

def main() :
	escalas = ["C", "F", "K"]

	escala_original = ""

	while True :
		escala_original = input("Insira a escala original da temperatura\nC - Celsius\nF - Fahrenheit\nK - Kelvin\n")

		if escala_original in escalas : break
		else :
			print("Escala inválida!")

	
	temperatura = float(input("Insira a temperatura a ser calculada: "))

	escala_destino = ""
	
	while True :
		escala_destino = input("Insira a escala destino da temperatura\nC - Celsius\nF - Fahrenheit\nK - Kelvin\n")

		if escala_destino in escalas : break
		else :
			print("Escala inválida!")

	resultado = 0.0

	if escala_original == escala_destino :
		resultado = temperatura
	else :
	
		match escala_original :
			case "C" :
				match escala_destino :
					case "F" :
						resultado = c_to_f(temperatura)
						
					case "K" :
						resultado = c_to_k(temperatura)
						
			case "F" :
				match escala_destino :
					case "C" :
						resultado = f_to_c(temperatura)
						
					case "K" :
						resultado = f_to_k(temperatura)
						
			case "K" :
				match escala_destino :
					case "C" :
						resultado = k_to_c(temperatura)
						
					case "F" :
						resultado = k_to_f(temperatura)
					
				

		print(f'A temperatura {temperatura} {escala_original} em {escala_destino} é {resultado}')

if __name__ == "__main__" :
	main()