import random
print("="*60)
print("🎰 BIENVENIDO AL CASINO PYTHON 🎰")
print("="*60)
# randint() - Número de la suerte
numero_suerte = random.randint(1, 100)
print(f"\n🍀 Tu número de la suerte: {numero_suerte}")
####si la proballidad es mas 70% debe salir un menajer exceletmne suerte
#si mas de 40% de probabilidad debe salir un mensaje de buena suerte
#si es menor de 40% debe salir un mensaje de mala suerte

# random() - Probabilidad de ganar
probabilidad = random.random()
porcentaje = probabilidad * 100
print(f"\n📊 Tu probabilidad de ganar hoy: {porcentaje:.2f}%")
if porcentaje > 70:
    print("🌟 ¡Excelente suerte! Hoy es tu día para ganar a lo grande." )
elif porcentaje > 40:   
    print("🍀 ¡Buena suerte! Tienes una buena oportunidad de ganar hoy.")
else:
    print("⚠️ ¡Mala suerte! Hoy podría ser un día difícil en el casino. Juega con precaución.")
    
# choice() - Ruleta de colores
colores = ["rojo", "negro", "verde"]
color_ganador = random.choice(colores)
print(f"\n🎡 RULETA - Color ganador: {color_ganador.upper()}")

#---------------------------------------

# shuffle() - Mezclar cartas
mazo = ['A♠', '2♥', '3♦', '4♣', '5♠', 'K♥', 'Q♦', 'J♣']
print(f"\n🃏 Mazo original: {mazo}")
random.shuffle(mazo)
print(f"   Mazo mezclado: {mazo}")
print(f"   Tu carta: {mazo[0]}")

# sample() - Lotería
numeros_loteria = random.sample(range(1, 100), 5)
numeros_loteria.sort()
print(f"\n🎫 LOTERÍA - Números ganadores: {numeros_loteria}")

# uniform() - Premio en efectivo
premio = random.uniform(10.0, 1000.0)
print(f"\n💰 Premio ganado: S/ {premio:.4f}")

# randrange() - Apuestas en múltiplos de 5
apuesta = random.randrange(5, 105, 5)
print(f"\n💵 Apuesta sugerida: S/ {apuesta}")



# Generar ticket completo
print("\n" + "="*60)
print("🎟️  TICKET DE CASINO")
print("="*60)
print(f"Número de suerte: {numero_suerte}")
print(f"Probabilidad: {porcentaje:.2f}%")
print(f"Ruleta: {color_ganador}")
print(f"Carta: {mazo[0]}")
print(f"Lotería: {numeros_loteria}")
print(f"Premio: S/ {premio:.2f}")
print(f"Apuesta sugerida: S/ {apuesta}")
print("="*60)

# Juego extra: Lanzamiento de dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
total_dados = dado1 + dado2
print(f"\n🎲 Lanzamiento de dados: {dado1} + {dado2} = {total_dados}")

if total_dados == 7:
    print("   ¡JACKPOT! Sacaste 7 🎊")
elif total_dados >= 10:
    print("   ¡Excelente tirada! 🎉")
else:
    print