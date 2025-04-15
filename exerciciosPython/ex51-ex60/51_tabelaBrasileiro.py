times_brasileirao = (
    "Flamengo", "Palmeiras", "Juventude", "Vasco da Gama", "Fluminense",
    "Internacional", "Fortaleza", "Ceará", "Corinthians", "Botafogo",
    "Bragantino", "Cruzeiro", "Grêmio", "Bahia", "São Paulo",
    "Atlético-MG", "Mirassol", "Santos", "Vitória", "Sport"
)
timesAlfabetico = sorted(times_brasileirao)
print(f"Os 5 primeiros colocados do Brasileiro são {times_brasileirao[0:5]}\nOs 4 últimos são {times_brasileirao[-4:]}\n")
print("Os times em ordem alfabetica são")
for c in range(0,20,4):
    print(f"{timesAlfabetico[c]:<15}  {timesAlfabetico[c+1]:<15} {timesAlfabetico[c+2]:<15} {timesAlfabetico[c+3]:<15}")
posicaoSantos = times_brasileirao.index("Santos") + 1
print(f"E a posição do santos é {posicaoSantos}°")