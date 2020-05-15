from raspagem_corona import RaspagemCorona, TratamentoDados

if __name__ == '__main__':

	#Determinando limites
	primeira_linha = 4
	ultima_linha = 34
	linha_inexistente = [5, 6, 20]

	#Declarando o Dicionário Principal
	main_dictionary = dict()

	#Instanciando a classe e acessando o site
	raspador = RaspagemCorona()

	#Declarando lista de cabeçalhos
	heads = list()

	#Loop de coleta de cabeçalhos
	for cabecalho in range(1, 13):
		heads.append(raspador.Cabecalhos(cabecalho).replace('\n', ' '))

	#Loop de coleta de dados
	for linha in range(primeira_linha, ultima_linha):

		if linha not in linha_inexistente:

			#Cada linha começa com uma lista de dados em branco
			dados = list()

			for coluna in range(1, 13):

				#Adiciona o dado coletado à lista de dados da linha
				dado = raspador.RasparDados(linha, coluna).replace(' ', '')
				
				#Preparando os dados para a tabela
				dado = raspador.TratarString(dado)

				dados.append(dado)

			#Incorporando os dados ao Dicionário Principal
			raspador.ParaDicionario(heads, dados, main_dictionary)
		else:
			continue

	raspador.driver.quit()

	tratamento = TratamentoDados()

	df = tratamento.ParaDataFrame(main_dictionary)

	df['T.C.P.'] = tratamento.GerarPorcentagem(df, df['Total Cases'])
	df['T.C.P.'] = tratamento.GerarPorcentagem(df, df['Total Deaths'])
	df['T.T.P.'] = tratamento.GerarPorcentagem(df, df['Total Tests'])

	print(df)
	tratamento.ParaExcel(df)