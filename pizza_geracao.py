import matplotlib.pyplot as plt
import poke


valor = poke.grafico_geracao(df=poke.csv())

#dados para o gráfico de pizza
valores = valor
print(valor)

labels = ['Geração 1','Geração 2','Geração 3','Geração 4','Geração 5','Geração 6']

cores = ['#00BFFF','#A52A2A','#F0F8FF','#006400','#FF1493','#ADFF2F']

#configurações do gráfico de pizza
explode = (0.05,0,0,0,0,0)  # Explode o primeiro pedaço do gráfico
fig, ax = plt.subplots()

#criação do gráfico de pizza
ax.pie(valores, explode=explode, labels=labels, colors=cores, autopct='%1.1f%%',
       shadow=True, startangle=90)

#configurações adicionais
ax.axis('equal')  # Assegura que o gráfico seja desenhado como um círculo
plt.title('Gráfico de Poke por geração')

#exibição do gráfico
plt.show()