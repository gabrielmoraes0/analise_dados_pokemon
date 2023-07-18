import matplotlib.pyplot as plt
import poke

#import do dado que é preciso
elementos = poke.grafico_elemento(df=poke.csv())
print(elementos)
fig, ax = plt.subplots()
#passando a variavel para o elemento y para criar gráfico
y_valor = elementos

#eixo x do gráfico
x_elementos = ['Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug', 'Ground', 'Fire', 'Poison'
       ,'Rock', 'Fighting','Dark', 'Electric','Dragon','Steel','Ghost','Fairy','Ice']

#grossura da barra
width = 0.2

ax.bar(x_elementos,y_valor, width=width)
ax.set_title('Participação de pokemons por elementos')
plt.show()
