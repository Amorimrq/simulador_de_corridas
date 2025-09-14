import random
from time import sleep

pilotos = []
grids = []

print("""
=========================================|
|        🏁  F1 MOTOR SPORT MENU  🏎️      |
|========================================= 
|                                        |
|   [1] 🏆 Iniciar Corrida              
|   [2] ❌ Sair do Jogo
|                                        |
=========================================|
""")

while True:
    try:
        menu = int(input("Escolha uma opção: "))
        if menu not in [1, 2]:
            print("⚠️ Opção inválida, digite 1 ou 2.")
            continue
        break
    except ValueError:
        print("⚠️ Digite apenas números! ")

if menu == 1: 
    while True:
        try:
            corredores = int(input("Quantos pilotos terá na corrida? (mínimo 2): "))
            if corredores < 2:
                print("⚠️ Precisa ter pelo menos 2 pilotos!")
                continue
            break
        except ValueError:
            print("⚠️ Digite apenas números!")

    for i in range(corredores):
        while True:
            nome = input(f"Digite o nome do piloto {i+1} 🏎️: ").strip()
            if nome == "":
                print("⚠️ O nome não pode ficar vazio!")
            elif nome in pilotos:
                print("⚠️ Esse nome já foi escolhido!")
            else:
                pilotos.append(nome)
                break

    
    while True:
        try:
            circuito = int(input("""
[1] 🇧🇷 Interlagos
[2] 🇧🇪 SPA
[3] 🇲🇨 Mônaco 
[4] 🇮🇹 Monza
[5] 🏴 Silverstone
Escolha o circuito: """))
            
            if circuito not in [1, 2, 3, 4, 5]:
                print("⚠️ Escolha apenas entre 1 e 5!")
                continue
            break
        except ValueError:
            print("⚠️ Digite apenas números!")
    
    while True:
        try:
            print('')
            voltas = int(input("Quantas voltas terá a corrida? (mínimo 5): "))
            if voltas < 5:
                print("⚠️ Precisa ter pelo menos 5 voltas!")
                continue
            break
        except ValueError:
            print("⚠️ Digite apenas números!")

    print("🚦 Definindo o grid de largada...")
    for pos in range(corredores):
        while True:
            print('================================')
            print(f"Pilotos disponíveis: {pilotos}")
            grid = input(f"Quem largará na posição {pos+1}️⃣ ? ").strip()
            if grid in pilotos:
                pilotos.remove(grid)
                grids.append(grid)
                break
            else:
                print("⚠️ Nome inválido ou já escolhido!")
    
    print("")
    print("✅ Grid de largada definido!")
    for pos, piloto in enumerate(grids, start=1):
        if pos == 1:
            print(f"{pos}º lugar: {piloto}")
        elif pos == 2:
            sleep(1)    
            print(f"{pos}º lugar: {piloto}")
        elif pos == 3:
            sleep(2)    
            print(f"{pos}º lugar: {piloto}")
        else:
            sleep(2)    
            print(f"{pos}º lugar: {piloto}")
    sleep(2)
    
    print("🏎️ Pilotos prontos na pista!")
    sleep(2)
    
    print("🏁 Corrida vai começar em...")
    for valor in range(5, -1, -1):
        print(f"⏱️ {valor}")
        sleep(1)
    print("🔥🏎️ Vai!!! 🏎️🔥")

    voltass = voltas 
    for volta in range(1, voltass + 1):
        print(f"========= 🌀 Volta {volta} 🌀 =========")

        ultrapassagem = False
        piloto_ultrapassou, piloto_perdeu = None, None

        if random.random() < 0.4 and len(grids) > 1:
            pos1 = random.randint(1, len(grids)-1)
            pos2 = pos1 - 1  
            grids[pos1], grids[pos2] = grids[pos2], grids[pos1]
            piloto_ultrapassou, piloto_perdeu = grids[pos2], grids[pos1]
            ultrapassagem = True
        
        sleep(3)
        
        for i in range(len(grids)):
            if ultrapassagem and grids[i] == piloto_ultrapassou:
                print(f"⚡ {grids[i]} ultrapassou {piloto_perdeu}! 🚀")
                sleep(2)
            else:
                evento = random.choice([
                    f"😱 {grids[i]} quase perdeu o controle!",
                    f"😞 {grids[i]} não teve boa sorte.",
                    f"💥 {grids[i]} encostou no adversário, mas seguiu na pista.",
                    f"🔥 {grids[i]} voa como um foguete!"
                ])
                print(evento)
            print()

        if ultrapassagem:
            print(f"📊 Nova ordem: {grids}")
            
            sleep(5)

    print("🏁🏁 Corrida finalizada! 🏁🏁")
    sleep(2)    
    print("🎉 Resultado final 🎉")
    sleep(2)    

    for pos, piloto in enumerate(grids, start=1):
        if pos == 1:
            print(f"🥇 {pos}º lugar: {piloto}")
        elif pos == 2:
            sleep(1)    
            print(f"🥈 {pos}º lugar: {piloto}")
        elif pos == 3:
            sleep(2)    
            print(f"🥉 {pos}º lugar: {piloto}")
        else:
            sleep(2)    
            print(f"{pos}º lugar: {piloto}")
