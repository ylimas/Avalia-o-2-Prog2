from xmlrpc.client import ServerProxy

def menu():
	print('=====Cliente XML-RPC====')
	print('1 - Fazer Reserva')
	print('2 - Cadastrar Passageiro')
	print('3 - Cadastrar Voo')
	print('4 - Sair')

def main():

	srp = ServerProxy("http://localhost:8000/")

	on = True

	while on == True:

		menu()
		escolha = int(input('Escolha uma opção: '))

		if escolha not in [1, 2, 3, 4]:
			print('Escolha inválida! ')
		elif escolha == 1:
			idvoo = input('\nInforme o ID do voo: ')
			if srp.vooExiste(idvoo) == False:
				print('O voo não existe.\n\n\n')
			elif srp.vagasVoo(idvoo) <= 0:
				print('O voo está lotado.\n\n\n')
			else:
				assento = input('\nInforme o assento: ')
				if srp.assentoLivre(idvoo, assento) == False:
					print('\nO assento está ocupado. ')
				else:
					idpass = input('\nInforme o ID do passageiro: ')
					if srp.passExiste(idpass) == False:
						print('O passageiro não existe.\n\n\n')
					else:
						idres = input('\nInforme o ID da reserva: ')
						voo = srp.getVoo(idvoo)
						data = ''
						if voo and 'dataPda' in voo:
							data = voo['dataPda']
						status = 'confirmada'
						cod = srp.adReserva(idres, data, status, assento, idpass, idvoo)
						if cod == 0:
							print('Sua reserva foi confirmada!')
							bdpass = srp.getPassageiro(idpass)
							res = srp.getReserva(idres)

							print('-------------DADOS DO PASSAGEIRO-------------')
							print(f"ID do Passageiro:   {bdpass['id']}")
							print(f"Nome:   {bdpass['nome']}")
							print(f"Email:   {bdpass['email']}")
							print(f"Telefone:   {bdpass['tel']}")
							print('\n\n')

							print('------------DADOS DA RESERVA-------------')
							print(f"ID da Reserva:   {res['id']}")
							print(f"Data:   {res['data']}")
							print(f"Status:   {res['status']}")
							print(f"Assento:   {res['assento']}")
							print(f"ID do Passageiro:   {bdpass['id']}")
							print(f"ID do Voo:   {res['idvoo']}")
							print('\n\n')

							print('------------DADOS DO VOO------------')
							print(f"ID do VOO:   {voo['id']}")
							print(f"Número do Voo:   {voo['numVoo']}")
							print(f"Ponto de embarque:   {voo['origem']}")
							print(f"Data da Partida:   {voo['dataPda']}")
							print(f"Ponto de Desembarque:   {voo['destino']}")
							print(f"Data de Chegada:   {voo['dataChe']}")
							print('\n\n\n\n')
						else:
							if cod == 1:
								print('Erro: passageiro não existe.')
							elif cod == 2:
								print('Erro: voo não existe.')
							elif cod == 3:
								print('Erro: voo sem vagas.')
							elif cod == 4:
								print('Erro: assento ocupado.')
							else:
								print('Erro desconhecido na reserva.')

		elif escolha == 2:
			idpass = input('Informe o ID do passageiro: ')
			while srp.passExiste(idpass):
				idpass = input('O ID já está sendo utilizado. Insira outro: ')

			nome = input('Informe o nome do passageiro: ')
			email = input('Informe o Email do passageiro: ')
			tel = input('Informe o telefone do passageiro: ')

			srp.adPassageiro(idpass, nome, email, tel)
			print('Passageiro cadastrado com sucesso!\n\n')

		elif escolha == 3:
			idvoo = input('Informe o ID do voo:  ')
			while srp.vooExiste(idvoo):
				idvoo = input('O ID já está sendo utilizado. Insira outro: ')

			numVoo = input('Número do voo: ')
			origem = input('Origem: ')
			destino = input('Destino: ')
			dataPda = input('Data partida: ')
			dataChe = input('Data chegada: ')

			srp.adVoo(idvoo, numVoo, origem, destino, dataPda, dataChe)
			print('Voo cadastrado!\n\n')

		elif escolha == 4:
			on = False


main()
