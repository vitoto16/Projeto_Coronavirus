import pandas as pd
from .raspagem_corona import TratamentoDados


# Para rodar esse arquivo de teste, apenas é necessário executar
# quando setado o prompt/cmder na pasta com o arquivo o comando 'pytest'

# Testa os metodos relacionados a opção 'ler_excel' do programa principal


def test_deve_retornar_dataframe_quando_chamada_a_funcao_ler_excel():
    # Testa se o método ler excel retorna um dataframe
    tratamento = TratamentoDados()
    df = tratamento.ler_excel()
    assert type(df) == pd.DataFrame


def test_deve_substituir_nome_da_primeira_celula_da_primeira_coluna_quando_chamada_a_funcao_ler_excel():
    # Testa se a coluna 'Unnamed: 0' foi de fato apagada do df
    tratamento = TratamentoDados()
    df = tratamento.ler_excel()
    colunas_nome = list(df.columns)
    assert ('Unnamed: 0' not in colunas_nome) == True


def test_porcentagem():
    # Testa se a soma da coluna de porcentagens é igual a 100
    tratamento = TratamentoDados()
    df = tratamento.ler_excel()
    df = tratamento.gerar_porcentagem(df, 'Total Cases')
    soma = df['porcentagem_' + 'Total Cases'].sum()

    # Comparação de float feita com o módulo da subtração
    assert abs(soma - float(100)) <= 0.001
