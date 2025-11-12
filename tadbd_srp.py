


def open_bd(tabnamePass, tabnameRes, tabnameVoos):

	#abrindo arquivo e declarando variáveis
	file = open(tabnamePass, 'r')
	linha = file.readline()

	tab = {}
	tabres = {}
	tabpass = {}
	tabvoos = {}



	#lendo cada linha até ler uma linha vazia
	while linha != '':

		linha = linha.strip()
		linha = linha.split(', ')

		#tratando os dados da linha
		tabpass[linha[0]] = {}

		#preenchendo o id
		tabpass[linha[0]['id']] = linha[0]
		#preenchendo o nome
		tabpass[linha[0]['nome']] = linha[1]
		#preenchendo o email
		tabpass[linha[0]['email']] = linha[3]
		#preenchendo o telefone
		tabpass[linha[0]['tel']] = linha[4]

		linha = file.readline()


	file.close()

	#colocando os passageiros do dicionário principal
	tab['passageiros'] = tabpass



	#repetindo o processo agora com as reservas
	file = open(tabnameRes, 'r')
	linha = file.readline()

	while linha != '':
		linha = linha.strip()
		linha = linha.split(', ')


	#perguntar sobre id da reserva
		tabres[linha[0]] = {}

	#--------FAZER PROCESSAMENTO DOS DADOS DAS RESERVAS-----------------
	#
	#
	#
	#
	#
	#
	file.close()

	#--------------VOOS---------------
	file = open(tabnameVoos, 'r')


	linha = file.readline()
	while linha != '':
		linha = linha.strip()
		linha = linha.split(', ')

		tabres[linha[0]] = {}


		tabres[linha[0]['id']] = linha[0]

		tabres[linha[1]['numVoo']] = linha[1]
		
		tabres[linha[2]['origem']] = linha[2]
		
		tabres[linha[3]['destino']] = linha[3]
		
		tabres[linha[4]['dataPda']] = linha[4]
		
		tabres[linha[5]['dataChe']] = linha[5]
		
		tabres[linha[6]['vagas']] = linha[6]

		linha = file.readline()

	tab['voos'] = tabvoos

	return tab






def salva_bd(bd, tabnamePass, tabnameRes, tabnameVoo):

	pass

def adPassageiro(bd, idpass, nome, email, fone):

	pass

def adReserva(bd, idres, data, status, assento, idpass, idvoo):
	pass


def adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada):
	pass

def vooExiste(bd, idvoo):
	pass	

def passExiste(bd, idpass):
	pass

def vagasVoo(bd, idvoo):
	pass

def assentoLivre(bd, idvoo, assento):
	pass
