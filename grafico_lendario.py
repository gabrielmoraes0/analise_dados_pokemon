import poke
import matplotlib.pyplot as plt


#chamando as variaveis e utilizando len para saber a quantidade de cada variavel
lendarios = len(poke.lendarios(df=poke.csv()))
nao_lendarios = len(poke.nao_lendarios(df=poke.csv()))

dados = [lendarios, nao_lendarios]

#criando o grafico de pizza
categorias = ['Lendario','Normal']

cor = ['#e2509c', '#aa08bf']

#configuração do gráfico
plt.figure(figsize=(6, 6))  #ajusta o tamanho do gráfico
plt.pie(dados, labels=categorias, colors=cor, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(dados) / 100, p))

plt.title('Comparação de raridade de pokemons lendários e normais')
plt.show()