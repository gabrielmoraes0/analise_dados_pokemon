import pandas as pd


#Leitura do arquivo de dados pokemon
def csv():
    df = pd.read_csv('Pokemon.csv')
    return df

#Retorna os valores de qual pokemon participa de qual clan
def tipos(df):
    type = pd.concat([df['Type 1'], df['Type 2']]).value_counts()
    return type

#Retorna os valores de cada poke participar de qual elemento.
def grafico_elemento(df):
    type = pd.concat([df['Type 1'], df['Type 2']]).value_counts()
    coluna = type
    valores = []
    for valor in coluna:
        valores.append(valor)
    return valores


#Dados retirados e passados para uma lista para a ser utilizada em um gráfico
def grafico_geracao(df):
    geracao = df['Generation'].value_counts()
    valores = []
    for valor in geracao:
        valores.append(valor)
    return valores


#Separando em niveis os ataques dos pokes para saber os niveis de ataque
def ataque_alto(df):
    maiores_ataques = df.loc[df['Attack'] >= 150]
    
    return len(maiores_ataques)

def ataque_medio(df):
    ataque_medio = df.query('100<= Attack <= 149')
    return len(ataque_medio)

def ataque_baixo(df):
    ataque_baixo = df.query('50<= Attack <= 99')
    return len(ataque_baixo)

def outros_ataques(df):
    outros_ataques = df.query('0<= Attack <=49')
    return len(outros_ataques)


#trabalhando com valores nulos que são pokes com apenas um tipo/elemento
def um_elemento(df):
    df_com_nulo = df[df.isnull().any(axis=1)]
    df_media = df_com_nulo[['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']].mean()
    medias = []
    for valor in df_media:
        medias.append(valor)
    return medias

#sem valores nulos, pokes com 2 elementos
def dois_elementos(df):
    df_sem_nulos = df.dropna()
    df_media = df_sem_nulos[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
    medias = []
    for valor in df_media:
        medias.append(valor)
    return medias

#separando por valores booleanos
def lendarios(df):
    df_lenda = df[df['Legendary'] == True]
    return df_lenda


def nao_lendarios(df):
    df_nao_lendario = df[df['Legendary'] == False]
    return df_nao_lendario


if __name__ == '__main__':
    df = csv()

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    print(df.info())







