from selenium import webdriver

class RaspagemCorona():

	def __init__(self):

		self.driver = webdriver.Chrome()

		self.driver.get('https://www.worldometers.info/coronavirus/')

	def RasparDados(self):

		for i in range(4, 45, 2):
			heads = []
			data = []

			for j in range(1, 13):
				head = self.driver.find_element_by_xpath('''
					//*[@id="main_table_countries_today"]/thead/tr/th[{}]'''.format(j)).text
				heads.append(head.replace('\n', ' '))

				data.append(self.driver.find_element_by_xpath('''
					//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'''.format(i, j)).text)

		return heads, data

	def ParaDicionario(self, heads, data, dicio):
		full_data = dict(zip(heads, data))
		
		#Incorporando país como chave e dados como valores
		for i in full_data.values():
			if i.isalpha():
				dicio[i] = full_data