import random
from time import sleep

pilotos = []
grids = []

menu = int(input("""
=========================================|
|        🏁  F1 MOTOR SPORT MENU  🏎️      |
|=========================================
|                                        |
|   [1] 🏆 Iniciar Corrida              
|   [2] ❌ Sair do Jogo
|                                        |
=========================================|
Escolha uma opção: """))


if menu == 1: 
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

    print("\nEsse então é o grid da corrida")
    print(grids)
    print("""
          🏁🏁🏁🏁🏁🏁
          """ * 2 )
    sleep(5)
    print("A corrida vai começar em: ")
    for valor in range(5, -1, -1):
        print(valor)
        sleep(1)
    print("🏁 Vai! 🏁\n")

    voltas = 10  
    for volta in range(1, voltas + 1):
        print(f"===== Volta {volta} =====")
        
        print()
        for i in range(len(grids)):
            eventos = [
                    f"{grids[i]} quase perdeu o controle!",
                    f"{grids[i]} manteve a posição.",
                    f"{grids[i]} encostou no adversário, mas seguiu na pista.",
                    f"{grids[i]} realizou uma manobra arisca "
                    ]
            if i == grid[0]:
                evento = random.choice(eventos)
                print(evento)
                print('')
            else:
                if random.random() < 0.4:
                    pos1 = random.randint(0, len(grids)-1)
                    pos2 = random.randint(0, len(grids)-1)
                    if pos1 != pos2:
                        grids[pos1], grids[pos2] = grids[pos2], grids[pos1]
                        print(f'{grids[i]} fez uma ultrapassagem!')
                        print(f">>> Ultrapassagem! Nova ordem: {grids}")
                else:
                    evento = random.choice(eventos)
                    print(evento)
                    print('')
                  
        sleep(5)

    print("🏁🏆 CORRIDA FINALIZADA 🏆🏁")
    print("Resultado final:")
    for i, piloto in enumerate(grids, start=1):
        print(f"{i}º lugar - {piloto}")
    print("Obrigado por Jogar")
else:
    print("Volte sempre")