from x_raspagem_corona import RaspagemCorona

if __name__ == '__main__':

	main_dictionary = {}

	raspador = RaspagemCorona()

	main_dictionary = raspador.RasparDados()

	#raspador.ParaDicionario(raspador.RasparDados(), main_dictionary)

	print(main_dictionary)

	raspador.driver.quit()