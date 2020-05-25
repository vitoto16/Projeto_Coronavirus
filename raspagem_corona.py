from selenium import webdriver
import plotly.express as px
import plotly.graph_objects as go
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

		soma = df[coluna_dataframe].sum()
		nova_coluna = 'porcentagem_' + coluna_dataframe

		df[nova_coluna] = (df[coluna_dataframe] / soma) * 100

	def LerExcel(self):

		df = pd.read_excel('out_corona.xlsx')
		df.rename(columns={'Unnamed: 0':'Paises'},
				inplace=True)

		return df

class TratamentoGraficos():

	def PlotarBarrasComposto(self, df):

		paises = df['Paises']

		fig = go.Figure()

		fig.add_trace(go.Bar(
		    x=paises,
		    y=df['Total Cases'],
		    name='Total de Casos',
		    marker_color='indianred'
		))
		fig.add_trace(go.Bar(
		    x=paises,
		    y=df['Total Deaths'],
		    name='Total de Mortes',
		    marker_color='lightsalmon'
		))

		fig.update_layout(
			barmode='group',
			xaxis_tickangle=-45,
			title='Incidencia mundial do virus',
			xaxis_title='Paises',
			yaxis_title='People(M)',
			font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="#7f7f7f"
    		)
		)
		fig.show()

	def PlotarPizzaMortes(self, df):

		paises = df['Paises']

		fig = px.pie(df, values='Total Deaths', names=paises, title='Relação de mortes por país')

		fig.update_traces(textinfo='label+percent', textposition='inside')

		fig.show()

	def PlotarPizzaTestes(self, df):

		paises = df['Paises']
		total_testes = df['Total Tests']

		fig = go.Figure(data=[go.Pie(labels=paises, values=total_testes)])

		fig.update_traces(textinfo='label+value', textfont_size=15, textposition='inside')

		fig.update_layout(title='Relação de testes por país')

		fig.show()