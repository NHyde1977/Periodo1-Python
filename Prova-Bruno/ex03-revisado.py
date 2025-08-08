from itertools import permutations, combinations, combinations_with_replacement
import random

times = {'flamento':{"gols_feitos": 0, "gols_sofridos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "pontos": 0},
         'botafogo':{"gols_feitos": 0, "gols_sofridos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "pontos": 0},
         'vasco': {"gols_feitos": 0, "gols_sofridos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "pontos": 0},
         'fluminense': {"gols_feitos": 0, "gols_sofridos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "pontos": 0}}
combinacoes_jogos = list(combinations(times, 2)) # mandou usar lista aqui pq ela pode ser atualizada e a combinação só é atualizada quando é criada e nunca mais
print('combinacoes_jogos:')
for c in combinacoes_jogos:
    print(c)

for timeA, timeB in combinacoes_jogos:
    gols_timeA = random.randint(0, 4)
    gols_timeB = random.randint(0, 4)
    times[timeA]["gols_feitos"] += gols_timeA
    times[timeA]["gols_sofridos"] += gols_timeB
    times[timeB]["gols_feitos"] += gols_timeA
    times[timeB]["gols_sofridos"] += gols_timeB

    if gols_timeA > gols_timeB:
            times[timeA]["vitorias"] += 1
            times[timeA]["pontos"] += 3
            times[timeB]["derrotas"] += 1
    elif gols_timeA < gols_timeB:
            times[timeB]["vitorias"] += 1
            times[timeB]["pontos"] += 3
            times[timeA]["derrotas"] += 1
    else:
            times[timeA]["empates"] += 1
            times[timeB]["empates"] += 1
            times[timeA]["pontos"] += 1
            times[timeB]["pontos"] += 1
print (times)

campeao = None
maior_pont = 0
vitorias = 0
derrotas = 0
empates = 0
gols = 0

for time, stats in times.items():

    if stats["pontos"] > maior_pont:
        campeao = time
        maior_pont = stats["pontos"]
        gols = stats["gols_feitos"]
        vitorias = stats["vitorias"]
        derrotas = stats["derrotas"]
        empates = stats["empates"]

aproveitamento = (maior_pont / 9) * 100

print(f"Time campeão: {campeao}")
print(f"Pontos: {maior_pont}")
print (f"Vitórias: {vitorias}")
print (f"Derrotas: {derrotas}")
print (f"Empates: {empates}")
print (f"Gols realizados: {gols}")
print (f"Aproveitamente: {aproveitamento:.2f}%")