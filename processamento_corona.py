from raspagem_corona import RaspagemCorona

if __name__ == '__main__':

	#Declarando o Dicionário Principal
	main_dictionary = {}

	#Instanciando a classe e acessando o site
	raspador = RaspagemCorona()

	#Loop de coleta de dados
	for i in range(4, 45):
		heads = []
		dados = []
		for j in range(1, 13):
			heads.append(raspador.Cabecalhos(j).replace('\n', ' '))
				
			data = raspador.RasparDados(i, j)
			if data:
				dados.append(data)

		#Incorporando os dados ao Dicionário Principal
		raspador.ParaDicionario(heads, dados, main_dictionary)

	print(main_dictionary)

	raspador.driver.quit()