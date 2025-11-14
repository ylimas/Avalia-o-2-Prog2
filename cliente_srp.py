from xmlrpc.client import ServerProxy
#CORRIGIR USANDO GET E SEM ACESSAR BD POR AQUI. 


def menu():
	print('=====Cliente XML-RPC====')
	print('1 - Fazer Reserva')
	print('2 - Cadastrar Passageiro')
	print('3 - Cadastrar Voo')
	print('4 - Sair')


def main():

	srp = ServerProxy("http://localhost:8000/")

	#Variável que mantém o loop
	on = True

	while on == True:

		#Exibe o menu e captura a escolha
		menu()
		escolha = input('Escolha uma opção: ')

		#Interpreta a escolha
		if escolha not in [1, 2, 3, 4]:
			print('Escolha inválida! ')
		elif escolha == 1:
			idvoo = input('\nInforme o ID do voo: ')
			if srp.vooExiste(bd, idvoo) == False:
				print('O voo não existe.\n\n\n')
			elif srp.vagasVoo(bd, idvoo) <= 0:
				print('O voo está lotado.\n\n\n')
			else:
				assento = input('\nInforme o assento: ')
				if srp.assentoLivre(bd, assento) == False:
					print('\nO assento está ocupado. ')
				else:
					idpass = input('\nInforme o ID do passageiro: ')
					if srp.passExiste(bd, idpass) == False:
						print('O passageiro não existe.\n\n\n')
					else:
						adReserva(bd, idres, 'confirmada', assento, idpass, idvoo)
						print('Sua reserva foi confirmada!')
						voo = srp.getVoo(idvoo)
						bdpass = srp.getPass(idpass)
						res = srp.getRes(idres)


						#idpass, nome, email, telefone
						print('-------------DADOS DO PASSAGEIRO-------------')
						print(f'ID do Passageiro:   {bdpass['id']}')
						print(f'Nome:   {bdpass['nome']}')
						print(f'Email:   {bdpass['email']}')
						print(f'Telefone:   {bdpas['tel']}')
						print('\n\n')
						

						#idres, status, assento, idpass, idvoo
						print('------------DADOS DA RESERVA-------------')
						print(f'ID da Reserva:   {res['id']}')
						print(f'Data:   {res['data']}')
						print(f'Status:   {res['status']}')
						print(f'Assento:   {res['assento']}')
						print(f'ID do Passageiro:   {bdpass['id']}')
						print(f'ID do Voo:   {voo['idvoo']}')
						print('\n\n')


						#idvoo, numvoo, origem, destino, dtpartida, dtchegada
						print('------------DADOS DO VOO------------')
						print(f'ID do VOO:   {voo['id']}')
						print(f'Número do Voo:   {voo['numVoo']}')
						print(f'Ponto de embarque:   {voo['origem']}')
						print(f'Data da Partida:   {voo['dataPda']}')
						print(f'Ponto de Desembarque:   {voo['destino']}')
						print(f'Data de Chegada:   {voo['dataChe']}')
						print('\n\n\n\n')





		elif escolha == 2:
			idpass = input('Informe o ID do passageiro: ')
			

			#VERIFICA SE O ID JÁ EXISTE
			val = srp.passExiste(idpass)
				while val == False:
					idpass = input('O ID já está sendo utilizado. Insira outro: ')
					val = srp.passExiste(idpass)

			nome = input('Informe o nome do passageiro: ')
			email = input('Informe o Email do passageiro: ')
			tel = input('Informe o telefone do passageiro: ')

			srp.adPass(idpass, nome, email, tel)
			print('Passageiro cadastrado com sucesso!\n\n')

		elif escolha == 3:
			#idvoo, numvoo, origem, destino, dtpartida, dtchegada
			idvoo = input('Informe o ID do voo:  ')

			#VERIFICANDO SE O ID JÁ EXISTE
			val = srp.vooExiste(idvoo)
			while val == False:
				idvoo = input('O ID já está sendo utilizado. Insira outro: ')
				val = srp.vooExiste(idvoo)



