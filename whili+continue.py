contador = 0

while contador <= 100:
    contador += 1
    
    if contador >=10 and contador <=27:
        continue      # no caso ele excluiu o 6
    
    print(contador)
    
    if contador == 40:
        break