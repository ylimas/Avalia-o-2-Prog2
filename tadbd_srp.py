



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

		tabres[linha[0]['id']] = linha[0]
		tabres[linha[1]['data']] = linha[1]
		tabres[linha[2]['status']] = linha[2]
		tabres[linha[3]['assento']] = linha[3]
		tabres[linha[4]['idpass']] = linha[4]
		tabres[linha[5]['idvoo']] = linha[5]

		linha = arq.readline()



	tab['reservas'] = tabres
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

	#-----------------PASSAGEIROS------------------
	file = open(tabnamePass, 'w')

	for passageiro in bd['passageiros']:
		for dado in passageiro.values():
			file.write(dado + ', ')
		file.write('\n')


	file.close()



#-----------------RESERVAS---------------------
	file = open(tabnameRes, 'w')

	for reserva in bd['reservas']:
		for dado in reserva.values():
			file.write(dado + ', ')
		file.write('\n')

	file.close()



#-----------------VOOS------------------------
	file = open(tabnameVoos, 'w')

	for voo in bd['voos']:
		for dado in voo.values():
			file.write(dado + ', ')
		file.write('\n')

	file.close()

#FAZER A VERIFICAÇÃO DA ULTIMA LINHA


	
def adPassageiro(bd, idpass, nome, email, fone):

	bd['passageiros'][idpass] = {}
	bd['passageiros'][idpass]['id'] = str(idpass)
	bd['passageiros'][idpass]['nome'] = str(nome)
	bd['passageiros'][idpass]['email'] = str(email)
	bd['passageiros'][idpass]['tel'] = str(fone)

	return bd

def adReserva(bd, idres, data, status, assento, idpass, idvoo):
	
	bd['reservas'][idres] = {}
	bd['reservas'][idres]['id'] = str(idres)
	bd['reservas'][idres]['data'] = str(data)
	bd['reservas'][idres]['status'] = str(status)
	bd['reservas'][idres]['assento'] = str(assento)
	bd['reservas'][idres]['idpass'] = str(idpass)
	bd['reservas'][idres]['idvoo'] = str(idvoo)

	return bd

def adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada):


	bd['voos'][idvoo] = {}

	bd['voos'][idvoo]['id'] = str(idvoo)
	bd['voos'][idvoo]['numVoo'] = str(numvoo)
	bd['voos'][idvoo]['origem'] = str(origem)
	bd['voos'][idvoo]['destino'] = str(destino)
	bd['voos'][idvoo]['dataPda'] = str(dtpartida)
	bd['voos'][idvoo]['dataChe'] = str(dtchegada)
	#40 lugares sempre







def vooExiste(bd, idvoo):
	pass	

def passExiste(bd, idpass):
	pass

def vagasVoo(bd, idvoo):
	pass

def assentoLivre(bd, idvoo, assento):
	pass
