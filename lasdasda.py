# corrida.py
# Simulador de corrida no terminal (ASCII)
# Feito para ser simples de rodar e divertido de mexer :)

import os
import random
import time
from dataclasses import dataclass, field

# ---------- Utils ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def clamp(x, a, b):
    return max(a, min(b, x))

# ---------- Modelos ----------
@dataclass
class Carro:
    nome: str
    icone: str
    vmax: float          # velocidade máxima (m/s)
    aceleracao: float    # aceleração base (m/s²)
    aderencia: float     # 0.6 ~ 1.0 (quanto melhor segura na pista)
    inteligencia: float  # 0~1 (IA usa nitro melhor e freia melhor)
    nitros: int = 2
    pos: float = 0.0     # posição total em metros (contando todas as voltas)
    vel: float = 0.0     # velocidade atual
    volta_atual: int = 0
    concluiu: bool = False
    tempo_final: float | None = None
    historico: list = field(default_factory=list)

    def tick(self, dt, pista, clima, usar_nitro=False):
        if self.concluiu:
            return

        # efeitos de clima/pista
        grip = self.aderencia * clima["fator_grip"] * pista["grip_base"]

        # chance de micro-eventos (pequena perda de tempo)
        if random.random() < clima["prob_evento_pequeno"]:
            # um "tranco": reduz levemente a velocidade
            self.vel *= 0.9

        # estratégia de IA: decidir nitro
        if not usar_nitro and self.nitros > 0:
            # IA avalia diferença para o líder e reta (sem curvas)
            reta = pista["reta_proporcao"]
            quer = (self.inteligencia * 0.7 + reta * 0.4 + random.random()*0.2) > 0.9
            usar_nitro = quer

        boost = 1.0
        if usar_nitro and self.nitros > 0:
            boost = 1.35
            self.nitros -= 1

        # dinâmica simples
        ruído = random.uniform(-0.2, 0.2)
        acel_efetiva = max(0.0, self.aceleracao * grip * boost + ruído)
        self.vel += acel_efetiva * dt

        # “curva” reduz velocidade média fora da reta
        curva_penalty = (1 - pista["reta_proporcao"]) * (1 - grip) * 3.0
        self.vel -= curva_penalty * dt
        self.vel = clamp(self.vel, 0, self.vmax * grip * (1.0 + 0.05 * pista["qualidade"]))

        # avanço
        self.pos += self.vel * dt

        # salva histórico curto para HUD
        if len(self.historico) > 60:
            self.historico.pop(0)
        self.historico.append(self.vel)

    def kmh(self):
        return self.vel * 3.6


# ---------- Setup padrão ----------
def criar_pilotos(nome_jogador="Você", adversarios=4):
    icons = ["🚗","🏎️","🚙","🚕","🚓","🚘","🛻","🚐"]
    random.shuffle(icons)

    def rnd_car(nm, ic):
        return Carro(
            nome=nm, icone=ic,
            vmax=random.uniform(58, 70),       # m/s ≈ 210–252 km/h
            aceleracao=random.uniform(6, 10),  # m/s²
            aderencia=random.uniform(0.70, 0.98),
            inteligencia=random.uniform(0.4, 0.95),
            nitros=2
        )

    carros = [rnd_car(nome_jogador, icons[0])]
    for i in range(adversarios):
        carros.append(rnd_car(f"Bot{i+1}", icons[i+1]))
    return carros

def setup_pista(dist_volta_km=3.5, voltas=3):
    return {
        "dist_volta_m": dist_volta_km * 1000.0,
        "voltas": voltas,
        "reta_proporcao": random.uniform(0.35, 0.75),  # % da volta que é reta
        "grip_base": random.uniform(0.90, 1.05),
        "qualidade": random.uniform(0.0, 1.0)          # melhora leve do topo de velocidade
    }

def setup_clima():
    # três estados simples
    tipo = random.choices(
        ["seco","nublado","chuva"],
        weights=[0.55, 0.30, 0.15],
        k=1
    )[0]
    if tipo == "seco":
        return {"tipo": tipo, "fator_grip": 1.00, "prob_evento_pequeno": 0.02}
    if tipo == "nublado":
        return {"tipo": tipo, "fator_grip": 0.96, "prob_evento_pequeno": 0.03}
    # chuva
    return {"tipo": tipo, "fator_grip": 0.88, "prob_evento_pequeno": 0.05}

# ---------- Render ----------
def barra_progresso(pos, total, largura=42):
    frac = clamp(pos/total, 0, 1)
    cheio = int(frac * largura)
    return "[" + "#"*cheio + "-"*(largura-cheio) + "]"

def render_hud(carros, pista, clima, tempo, lider_pos):
    clear()
    print("SIMULADOR DE CORRIDA – Terminal Edition")
    print(f"Pista: {pista['dist_volta_m']/1000:.1f} km x {pista['voltas']} voltas | Clima: {clima['tipo']}")
    print(f"Tempo: {tempo:6.1f}s   Reta: {int(pista['reta_proporcao']*100)}%   GripBase: {pista['grip_base']:.2f}")
    print("-"*70)

    total_m = pista["dist_volta_m"] * pista["voltas"]
    for c in carros:
        barra = barra_progresso(c.pos, total_m)
        gap = (lider_pos - c.pos) / 3.6  # “gap” em s aproximado (m / (m/s))
        if c.concluiu:
            status = f"✓ FIN {c.tempo_final:5.1f}s"
        else:
            status = f"{c.kmh():6.1f} km/h | nitro:{c.nitros} | gap:+{max(0, gap):.1f}s"
        volta = int(c.pos // pista["dist_volta_m"]) + 1
        volta = min(volta, pista["voltas"])
        print(f"{c.icone} {c.nome:<8} V{volta}/{pista['voltas']} {barra}  {status}")

def render_podio(resultados):
    print("\n" + "="*70)
    print("🏁 CHEGADA! RESULTADO FINAL")
    for i, c in enumerate(resultados, start=1):
        tempo_txt = f"{c.tempo_final:.2f}s" if c.tempo_final is not None else "--.--"
        medalha = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}º"
        print(f"{medalha}  {c.nome:<10}  {tempo_txt}")
    print("="*70)

# ---------- Lógica da corrida ----------
def correr(nome_jogador="Você"):
    random.seed()  # semente aleatória

    carros = criar_pilotos(nome_jogador, adversarios=4)
    pista = setup_pista(dist_volta_km=3.6, voltas=3)
    clima = setup_clima()

    # Duração do "tick" de simulação
    dt = 0.15  # segundos entre frames
    tempo_total = 0.0
    total_m = pista["dist_volta_m"] * pista["voltas"]

    # Estratégia simples de nitro para o jogador: usa no começo da última volta e no meio da penúltima
    pontos_nitro = {
        2: pista["dist_volta_m"] * 1.5,  # metade da 2ª volta
        3: pista["dist_volta_m"] * 2.02  # começo da 3ª volta
    }

    concluidos = 0
    while True:
        tempo_total += dt

        lider_pos = max(c.pos for c in carros)

        # update de cada carro
        for c in carros:
            usar_nitro_jogador = False
            if c.nome == "Você" and c.nitros > 0:
                volta_atual = int(c.pos // pista["dist_volta_m"]) + 1
                alvo = pontos_nitro.get(volta_atual, None)
                if alvo is not None and c.pos >= alvo:
                    usar_nitro_jogador = True

            c.tick(dt, pista, clima, usar_nitro=usar_nitro_jogador)

            # checagem de volta/conclusão
            nova_volta = int(c.pos // pista["dist_volta_m"])
            if nova_volta != c.volta_atual:
                c.volta_atual = nova_volta

            if not c.concluiu and c.pos >= total_m:
                c.concluiu = True
                c.tempo_final = tempo_total
                concluidos += 1

        # render
        render_hud(sorted(carros, key=lambda x: -x.pos), pista, clima, tempo_total, lider_pos)

        # fim?
        if concluidos == len(carros):
            break

        time.sleep(dt * 0.7)  # levemente menor pra parecer mais "vivo"

    # resultado final
    resultados = sorted(carros, key=lambda c: c.tempo_final if c.tempo_final is not None else 1e9)
    render_podio(resultados)

if __name__ == "__main__":
    try:
        correr("Você")
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
