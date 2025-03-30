#Criando comando sobre a aula

# Solicita ao usuário que insira seu peso em kg
peso = float(input("Digite seu peso em kg: "))

# Solicita ao usuário que insira sua altura em metros
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado do IMC
print("Seu IMC é de aproximadamente: ",imc,"!") 
