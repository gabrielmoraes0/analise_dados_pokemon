import matplotlib.pyplot as plt
import numpy as np
import poke

#chamando as funções e passando e transformando em tuplas e limitando 2 casas decimais
um_elemento = tuple(round(val, 2) for val in poke.um_elemento(df=poke.csv()))

dois_elementos = tuple(round(val, 2) for val in poke.dois_elementos(df=poke.csv()))


categorias = ('Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed')

#chamando as categoriais em tuplas em um dicionario para passar mais a frente para o gráfico
nomes_categorias = {
    'Um tipo': um_elemento,
    'Dois tipos': dois_elementos,
}

#transformando o texto em valores espaçados, ou seja ''considerando'' numero junto com o len e np
x = np.arange(len(categorias))

largura = 0.25
multiplicador = 0

fig, ax = plt.subplots(layout='constrained')

#criação do grafico
for atributo, medicao in nomes_categorias.items():
    desvio = largura * multiplicador
    cria = ax.bar(x + desvio, medicao, largura, label=atributo)
    ax.bar_label(cria, padding=2,)
    multiplicador += 1

#customizando o gráfico, como titulo, legenda, limitando o tamanho do mesmo
ax.set_title('Media de comparação de status de pokes por categorias')
ax.set_xticks(x + largura, categorias)
ax.legend(ncols=2)
ax.set_ylim(0, 500)

plt.show()
