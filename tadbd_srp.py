

#------------TESTADO!-------------
def open_bd(tabnamePass, tabnameRes, tabnameVoos): 

	file = open(tabnamePass, 'r', encoding='utf-8')
	linha = file.readline()

	tab = {}
	tabres = {}
	tabpass = {}
	tabvoos = {}

	while linha != '':

		linha = linha.strip()
		linha = linha.split(',')

		tabpass[linha[0]] = {}

		tabpass[linha[0]]['id'] = linha[0]
		tabpass[linha[0]]['nome'] = linha[1]
		tabpass[linha[0]]['email'] = linha[2]
		tabpass[linha[0]]['tel'] = linha[3]

		linha = file.readline()

	file.close()

	tab['passageiros'] = tabpass

	file = open(tabnameRes, 'r', encoding='utf-8')
	linha = file.readline()

	while linha != '':
		linha = linha.strip()
		linha = linha.split(',')

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
		tabvoos[linha[0]]['vagas'] = 40

		linha = file.readline()

	tab['voos'] = tabvoos

	return tab

#------------TESTADO!-------------
def salva_bd(bd, tabnamePass, tabnameRes, tabnameVoos):

	file = open(tabnamePass, 'w', encoding='utf-8')
	for passageiro in bd['passageiros'].values():
		if passageiro:
			linha = ''
			for dado in passageiro.values():
				linha += str(dado) + ','
			file.write(linha[:-2] + '\n')
	file.close()

	file = open(tabnameRes, 'w', encoding='utf-8')
	for reserva in bd['reservas'].values():
		if reserva:
			linha = ''
			for dado in reserva.values():
				linha += str(dado) + ','
			file.write(linha[:-2] + '\n')
	file.close()

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
				return 0
			else:
				return 4
		elif vooExiste(bd, idvoo) == False:
			return 2
		elif vagasVoo(bd, idvoo) <= 0:
			return 3
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
	if vooExiste(bd, idvoo) == False:
		return -1
	total = 40
	cont = 0
	for reserva in bd['reservas'].values():
		if reserva['idvoo'] == idvoo:
			cont += 1
	return total - cont

#------------TESTADO!-------------
def assentoLivre(bd, idvoo, assento):
	if vooExiste(bd, idvoo) == False:
		return False

	for reserva in bd['reservas'].values():
		if reserva['idvoo'] == idvoo and reserva['assento'] == assento:
			return False
	return True
