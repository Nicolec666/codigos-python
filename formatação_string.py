# usando o codigo como exemplo
nome = "Nicole"
peso = float(input("Digite seu peso:  "))
altura = float(input("Estamos quase lá, agora digite sua altura:  "))
resultado = peso/ (altura * altura)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso}  quilos e seu imc é'
linha_3 = f"{resultado:.4f}"
# f-strings
#colocando o f na frente e depois colocar{} na palavra que seria a variável assim o print vai mostrar a variavel linha_1 ediTADA com o f, o resto fica como str.
#DA para formatar casas decimais usabdo o:.2f(ele vai ter duas casas decimais)
print( nome , "O resultado do seu IMC é" ,resultado)
#ou de forma mais bonita
print(linha_1)
print(linha_2)
print(linha_3)