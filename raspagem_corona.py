from selenium import webdriver

class RaspagemCorona():

	def __init__(self):

		#Designando o driver
		self.driver = webdriver.Chrome()

		#Acessando o site
		self.driver.get('https://www.worldometers.info/coronavirus/')


	def Cabecalhos(self, coluna):
		
		#Coletando cabeçalhos
		heads = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/thead/tr/th[{}]'.format(coluna)).text

		return heads

	def RasparDados(self, linha, coluna):

		#Coletando dados
		data = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'.format(linha, coluna)).text

		return data

	def ParaDicionario(self, heads, data, dicio):
		full_data = dict(zip(heads, data))
		
		#Incorporando país como chave e dados como valores
		for i in full_data.values():
			if i.isalpha():
				dicio[i] = full_data