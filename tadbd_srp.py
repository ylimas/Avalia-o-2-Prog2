#------------TESTADO!-------------
def open_bd(tabnamePass, tabnameRes, tabnameVoos): 

	#abrindo arquivo e declarando variáveis
	file = open(tabnamePass, 'r', encoding='utf-8')
	linha = file.readline()

	tab = {}
	tabres = {}
	tabpass = {}
	tabvoos = {}



	#lendo cada linha até ler uma linha vazia
	while linha != '':

		linha = linha.strip()
		linha = linha.split(',')

		#tratando os dados da linha
		tabpass[linha[0]] = {}

		#preenchendo o id
		tabpass[linha[0]]['id'] = linha[0]
		#preenchendo o nome
		tabpass[linha[0]]['nome'] = linha[1]
		#preenchendo o email
		tabpass[linha[0]]['email'] = linha[2]
		#preenchendo o telefone
		tabpass[linha[0]]['tel'] = linha[3]

		linha = file.readline()


	file.close()

	#colocando os passageiros do dicionário principal
	tab['passageiros'] = tabpass



	#repetindo o processo agora com as reservas
	file = open(tabnameRes, 'r', encoding='utf-8')
	linha = file.readline()

	while linha != '':
		linha = linha.strip()
		linha = linha.split(',')


	#perguntar sobre id da reserva
		tabres[linha[0]] = {}

		tabres[linha[0]]['id'] = linha[0]
		tabres[linha[0]]['data'] = linha[1]
		tabres[linha[0]]['status'] = linha[2]
		tabres[linha[0]]['assento'] = linha[3]
		tabres[linha[0]]['idpass'] = linha[4]
		tabres[linha[0]]['idvoo'] = linha[5]

		linha = file.readline()



	tab['reservas'] = tabres
	file.close()

	#--------------VOOS---------------
	file = open(tabnameVoos, 'r', encoding='utf-8')


	linha = file.readline()
	while linha != '':
		linha = linha.strip()
		linha = linha.split(',')

		tabvoos[linha[0]] = {}


		tabvoos[linha[0]]['id'] = linha[0]
		tabvoos[linha[0]]['numVoo'] = linha[1]
		tabvoos[linha[0]]['origem'] = linha[2]
		tabvoos[linha[0]]['destino'] = linha[3]
		tabvoos[linha[0]]['dataPda'] = linha[4]
		tabvoos[linha[0]]['dataChe'] = linha[5]
		tabvoos[linha[0]]['vagas'] = linha[6]

		linha = file.readline()

	tab['voos'] = tabvoos

	return tab





#------------TESTADO!-------------
def salva_bd(bd, tabnamePass, tabnameRes, tabnameVoos):


	#-----------------PASSAGEIROS------------------
	file = open(tabnamePass, 'w', encoding='utf-8')
	for passageiro in bd['passageiros'].values():
		if passageiro:
			linha = ''
			for dado in passageiro.values():
				linha += str(dado) + ','
			file.write(linha[:-2] + '\n')  # remove ", "
	file.close()

	#-----------------RESERVAS---------------------
	file = open(tabnameRes, 'w', encoding='utf-8')
	for reserva in bd['reservas'].values():
		if reserva:
			linha = ''
			for dado in reserva.values():
				linha += str(dado) + ','
			file.write(linha[:-2] + '\n')
	file.close()

	#-----------------VOOS------------------------
	file = open(tabnameVoos, 'w', encoding='utf-8')
	for voo in bd['voos'].values():
		if voo:
			linha = ''
			for dado in voo.values():
				linha += str(dado) + ','
			file.write(linha[:-2] + '\n')
	file.close()
#------------TESTADO!-------------
def adPassageiro(bd, idpass, nome, email, fone):

	bd['passageiros'][idpass] = {}
	bd['passageiros'][idpass]['id'] = str(idpass)
	bd['passageiros'][idpass]['nome'] = str(nome)
	bd['passageiros'][idpass]['email'] = str(email)
	bd['passageiros'][idpass]['tel'] = str(fone)

	return bd
#------------TESTADO!-------------
def adReserva(bd, idres, data, status, assento, idpass, idvoo):
	
	
	
	if passExiste(bd, idpass) == True:
		if vooExiste(bd, idvoo) == True and vagasVoo(bd, idvoo) > 0:
			if assentoLivre(bd, idvoo, assento):
				bd['reservas'][idres] = {}
				bd['reservas'][idres]['id'] = str(idres)
				bd['reservas'][idres]['data'] = str(data)
				bd['reservas'][idres]['status'] = str(status)
				bd['reservas'][idres]['assento'] = str(assento)
				bd['reservas'][idres]['idpass'] = str(idpass)
				bd['reservas'][idres]['idvoo'] = str(idvoo)
				bd['voos'][idvoo]['vagas'] -= 1

				return 0
			else:
				return 4
		elif vagasVoo(bd, idvoo) <= 0:
			return 3
		elif vooExiste(bd, idvoo) == False:
			return 2
	else:
		return 1
#------------TESTADO!-------------
def adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada):


	bd['voos'][idvoo] = {}

	bd['voos'][idvoo]['id'] = str(idvoo)
	bd['voos'][idvoo]['numVoo'] = str(numvoo)
	bd['voos'][idvoo]['origem'] = str(origem)
	bd['voos'][idvoo]['destino'] = str(destino)
	bd['voos'][idvoo]['dataPda'] = str(dtpartida)
	bd['voos'][idvoo]['dataChe'] = str(dtchegada)
	#40 lugares fixo
	bd['voos'][idvoo]['vagas'] = 40

	return bd
#------------TESTADO!-------------
def vooExiste(bd, idvoo):
	for voo in bd['voos'].values():
		if idvoo == voo['id']:
			return True
	return False
#------------TESTADO!-------------
def passExiste(bd, idpass):
	for passageiro in bd['passageiros'].values():
		if idpass == passageiro['id']:
			return True
	return False
#------------TESTADO!-------------
def vagasVoo(bd, idvoo):
	#retorna a quantidade de vagas;
	#caso o voo não exista, retorna o código -1

	#verificando se o voo existe

	if vooExiste(bd, idvoo) == False:
		return -1

	return int(bd['voos'][idvoo]['vagas'])
#------------TESTADO!-------------
def assentoLivre(bd, idvoo, assento):
	if vooExiste(bd, idvoo) == False:
		return False

	for reserva in bd['reservas'].values():
		if reserva['idvoo'] == idvoo and reserva['assento'] == assento:
			return False
	return True

