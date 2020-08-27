from raspagem_corona import RaspagemCorona, TratamentoDados, TratamentoGraficos

if __name__ == '__main__':
	
	# Determinando limites
	primeira_linha = 4
	ultima_linha = 34
	linha_inexistente = [5, 7, 9]

	# Declarando o Dicionário Principal
	main_dictionary = dict()

	# Instanciando a classe e acessando o site
	raspador = RaspagemCorona()

	# Declarando lista de cabeçalhos
	heads = list()

	# Loop de coleta de cabeçalhos
	for cabecalho in range(3, 14):
		heads.append(raspador.cabecalhos(cabecalho).replace('\n', ' '))

	# Loop de coleta de dados
	for linha in range(primeira_linha, ultima_linha):

		if linha not in linha_inexistente:

			# Cada linha começa com uma lista de dados em branco
			dados = list()

			for coluna in range(2, 14):

				# Adiciona o dado coletado à lista de dados da linha
				dado = raspador.raspar_dados(linha, coluna).replace(' ', '')
				
				# Preparando os dados para a tabela
				dado = raspador.tratar_string(dado)

				dados.append(dado)

			# Incorporando os dados ao Dicionário Principal
			raspador.para_dicionario(heads, dados, main_dictionary)
			print(main_dictionary)
		else:
			continue

	# Fecha o driver quando acaba a raspagem
	raspador.driver.quit()

	# Trata os dados para o dataframe
	tratamento = TratamentoDados()

	# Monta o dataframe com os dados
	df = tratamento.para_data_frame(main_dictionary)
	df = tratamento.tratar_data_frame(df)
	print(df)

	# Gera porcentagem de casos e mortes totais
	tratamento.gerar_porcentagem(df, 'Total Cases')
	tratamento.gerar_porcentagem(df, 'Total Deaths')

	# Gera Excel a partir do dataframe
	tratamento.para_excel(df)

	tratamento_grafico = TratamentoGraficos()

	# Plotagem dos graficos a partir do dataframe
	tratamento_grafico.plotar_barras_composto(df)

	tratamento_grafico.plotar_graficos_pizza(df)

	tratamento_grafico.plotar_grafico_pontos(df)

	tratamento_grafico.plotar_mapa(df)
