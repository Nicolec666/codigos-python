# if /    elif        /else
# se / se não se / se não
# O if> pode ser sozinho; o elif e else não.
entrada = input('Você quer "entrar" ou "sair"? ')
# usa a mesma ideia de true ou false (se isso for == a aquilo execute)
if entrada == "entrar":
  print("Você entrou no sistema")
elif entrada == "sair":
  print("Você saiu do sistema")
else:
    print("Você não digitou nem entrar e nem sair.")

#else é sempre a ultima opição
#PARTE 2 DO VÍDEO
condição = True
if condição:
  print("Esse é o código do if")
print("Fora do if")
  