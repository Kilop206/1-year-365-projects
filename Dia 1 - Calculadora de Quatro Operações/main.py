# Funções para as operações

def add(a, b) :
    return a + b

def subtract(a, b) : 
    return a - b

def multiply(a, b) :
    return a * b

def divide(a, b) :
    if b == 0 :
        raise ValueError("B não pode ser igual a 0")
    return a / b

# Função principal
def main() :

    operadores = ["+", "-", "*", "/", "(", ")"]

    # Valores após a separação
    valores_parsed = []

    # Resultado final
    result = 0

    operacao = input("Digite uma operação: ")

    # Passa por todos os valores da expressão
    for index, value in enumerate(operacao) :

        if (index + 1) > len(operacao) :
            break
        # Verifica se os valores são válidos antes de adicionar aos valores separados
        elif value.isdigit() or value in operadores :
            valores_parsed.append(value)


    numeros_apos_operadores = []

    # Faz com que números consecutivos na array sejam tratados como um número só
    for index, value in enumerate(valores_parsed) :
        if (index - 1) > 0 :
            if value.isdigit() and valores_parsed[index - 1] in operadores and index + 1 < len(valores_parsed):
                value.join(valores_parsed[index + 1])

    # Coloca valores entre parênteses no começo
    for index, value in enumerate(valores_parsed) :
        if value == "(" :
            if "(" in valores_parsed[(index + 1):(len(valores_parsed) - 1)] :
                break
            else :
                numeros_apos_operadores += (valores_parsed[(index):(len(valores_parsed) - 1)])

    # Remove parênteses
    for index, value in enumerate(numeros_apos_operadores) :
        if numeros_apos_operadores[index] in ["(", ")"] :
            numeros_apos_operadores.remove("(")
            print(numeros_apos_operadores)

    # Faz as operações
    for index, value in enumerate(numeros_apos_operadores) :
        match numeros_apos_operadores[index + 1] :
            case "+" :
                result = sum(value, numeros_apos_operadores[index + 2])
                break
            case "-" :
                result = subtract(value, numeros_apos_operadores[index + 2])
                break
            case "*" :
                result = multiply(value, numeros_apos_operadores[index + 2])
                break
            case "/" :
                result = divide(value, numeros_apos_operadores[index + 2])
                break


    print(result)

    continuar = input("Deseja continuar? (S/N): ")
    if not continuar.lower().startswith("s") :
        SystemExit(0)
        

if __name__ == '__main__' :
    main()