import random
from time import sleep
pilotos = []
grids = []
print("""🏁""" * 15)
menu = int(input("""
        F1 MOTOR SPORT
    [1] Jogar
    [2] Sair
    : """))
print("🏁" * 15)
if menu == 1 : 
    corredores = int(input("""  
        Quantos pilotos terá na corrida
    : """))
    
    for corredor in range(corredores):
        nome = str(input(f"""
        Qual o nome do {corredor + 1}
    : """))
        pilotos.append(nome)
             
    circuito = int(input("""
        [1] Interlagos
        [2] SPA
        [3] Mônaco 
        [4] Monza
        [5] Silverstone
        Qual será o circuito
    : """))

    for corredor in range(corredores):
        grid = str(input(f"""
        Qual a posição {corredor + 1 } do grid?
        (Escreva o nome do piloto)
    : """))
        pilotos.remove(grid)
        grids.append(grid)

    sleep(1)
    print("Esse então é o grid da corrida")
    sleep(1)
    print(grids)
    sleep(5)
    print("""
          🏁🏁🏁🏁🏁🏁
          """ )
   
    print("A corrida vai começar em: ")
    for valor in range(5, -1, -1):
        print(valor, end='\r')
        sleep(1)
    print("🏁Vai🏁")
    chances = ["largou bem", "largou mal" ]
    largada = random.choice(chances)
    corrida = 100 
    escolha = random.choice(grids)
    
    while True: 
        print(f"O piloto {escolha} {largada}")
        if largada == "largou mal ":
            sleep(1)
            print("E infelizmente perdeu posições")
        else:
            sleep(1)
            print("O piloto conseguiu algumas posições")
    
        sleep(1)
        print("")
        print(f"Já o piloto {grid} aproveitou o vácuo")
        sleep(1)
        print("Os demais pilotos seguem a liha")
        print(f"O Piloto {escolha} está fora da corrida infelizmente ")        
        break       
    
    