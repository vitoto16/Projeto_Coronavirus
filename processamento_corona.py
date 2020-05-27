from raspagem_corona import RaspagemCorona, TratamentoDados, TratamentoGraficos

if __name__ == '__main__':
	
	#Determinando limites
	primeira_linha = 4
	ultima_linha = 34
	linha_inexistente = [5, 6, 18]

	#Declarando o Dicionário Principal
	main_dictionary = dict()

	#Instanciando a classe e acessando o site
	raspador = RaspagemCorona()

	#Declarando lista de cabeçalhos
	heads = list()

	#Loop de coleta de cabeçalhos
	for cabecalho in range(2, 14):
		heads.append(raspador.Cabecalhos(cabecalho).replace('\n', ' '))

	#Loop de coleta de dados
	for linha in range(primeira_linha, ultima_linha):

		if linha not in linha_inexistente:

			#Cada linha começa com uma lista de dados em branco
			dados = list()

			for coluna in range(2, 14):

				#Adiciona o dado coletado à lista de dados da linha
				dado = raspador.RasparDados(linha, coluna).replace(' ', '')
				
				#Preparando os dados para a tabela
				dado = raspador.TratarString(dado)

				dados.append(dado)

			#Incorporando os dados ao Dicionário Principal
			raspador.ParaDicionario(heads, dados, main_dictionary)
		else:
			continue

	#Fecha o driver quando acaba a raspagem
	raspador.driver.quit()

	#Trata os dados para o dataframe
	tratamento = TratamentoDados()

	#Monta o dataframe com os dados
	df = tratamento.ParaDataFrame(main_dictionary)
	df = tratamento.TratarDataFrame(df)

	#Gera porcentagem de casos e mortes totais
	tratamento.GerarPorcentagem(df, 'Total Cases')
	tratamento.GerarPorcentagem(df, 'Total Deaths')

	#Gera Excel a partir do dataframe
	tratamento.ParaExcel(df)

	tratamento_grafico = TratamentoGraficos()

	#Plotagem dos graficos a partir do dataframe
	tratamento_grafico.PlotarBarrasComposto(df)

	tratamento_grafico.PlotarGraficosPizza(df)

	tratamento_grafico.PlotarGraficoPontos(df)

	tratamento_grafico.PlotarMapa(df)