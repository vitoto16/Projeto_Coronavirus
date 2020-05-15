from selenium import webdriver
import pandas as pd
import numpy as np

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
		4
		#Criando dicionario de valores
		full_data = dict(zip(heads, data))
		full_data.pop(heads[0])
		
		#Incorporando país como chave e dados como valores
		dicio[data[0]] = full_data

	#Preparando os numeros para DataFrame
	def TratarString(self, data):

		if '+' in data:
			data = data.replace('+', '')

		if ',' in data:
			data = data.replace(',', '')

		if 'N/A' in data:
			data = np.nan
			return data

		if data == '':
			data = 0
			return data

		if not data.isalpha():
			data = int(data)

		return data

class TratamentoDados():

	def ParaDataFrame(self, dicio):

		df = pd.DataFrame(dicio, dtype = np.int64).T

		return df

	def ParaExcel(self, df):

		writer = pd.ExcelWriter('out_corona.xlsx', engine = 'openpyxl')
		df.to_excel(writer, sheet_name = 'analise_corona')
		writer.save()

	def GerarPorcentagem(self, df, coluna_dataframe):

		soma = coluna_dataframe.sum()

		porcentagem = coluna_dataframe/soma

		return porcentagem