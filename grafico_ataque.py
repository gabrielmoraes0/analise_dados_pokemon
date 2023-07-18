import matplotlib.pyplot as plt
import poke

#importando os valores dos ataques para utilizar no gráfico
ataque_alto = poke.ataque_alto(df=poke.csv())
ataque_medio = poke.ataque_medio(df=poke.csv())
ataque_baixo = poke.ataque_baixo(df=poke.csv())
outros = poke.outros_ataques(df=poke.csv())


#passando para uma lista para utilizar no grafico e testando os valores
valores = [ataque_alto, ataque_medio, ataque_baixo, outros]
print(valores)

#Transformando o valor em porcentagem para utilizar no grafico
percentual_alto = (ataque_alto / 800) * 100
percentual_alto = round(percentual_alto, 2)

percentual_medio = (ataque_medio / 800) * 100
percentual_medio = round(percentual_medio, 2)

percentual_baixo = (ataque_baixo / 800) * 100
percentual_baixo = round(percentual_baixo, 2)

percentual_outros = (outros / 800) * 100
percentual_outros = round(percentual_outros, 2)

percentual = [percentual_alto, percentual_medio, percentual_baixo, percentual_outros]
print(percentual)

fig, ax = plt.subplots()
#dados do gráfico de barras
valores = [ataque_alto, ataque_medio, ataque_baixo, outros]
barras = ['Acima de 150', 'Entre 149 e 100', 'Entre 99 e 50', 'Abaixo de 50']
barras_cor = ['blue', 'red', 'orange', 'purple']
barras_textos = ['3.62%', '22.62%', '57.12%', '16.62%']

#criar o gráfico de barras
ax.bar(barras, valores, color=barras_cor, label=barras_textos)

#adicionar o valor em cima de cada barra
for i in range(len(barras)):
    ax.text(i, valores[i], str(valores[i]), ha='center', va='bottom')

ax.legend(title='Percentual')
plt.title('Classificação de ataque entre os pokemons')
#exibir o gráfico
plt.show()

