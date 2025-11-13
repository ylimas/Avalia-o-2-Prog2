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


						#idpass, nome, email, telefone
						print('-------------DADOS DO PASSAGEIRO-------------')
						print(f'ID do Passageiro:   {bd['passageiro'][idpass]['id']}')
						print(f'Nome:   {bd['passageiro'][idpass]['nome']}')
						print(f'Email:   {bd['passageiro'][idpass]['email']}')
						print(f'Telefone:   {bd['passageiro'][idpass]['tel']}')
						print('\n\n')
						

						#idres, status, assento, idpass, idvoo
						print('------------DADOS DA RESERVA-------------')
						print(f'ID da Reserva:   {bd['reservas'][idres]['id']}')
						print(f'Data:   {bd['reservas'][idres]['data']}')
						print(f'Status:   {bd['reservas'][idres]['status']}')
						print(f'Assento:   {bd['reservas'][idres]['assento']}')
						print(f'ID do Passageiro:   {bd['passageiro'][idpass]['id']}')
						print(f'ID do Voo:   {bd['reservas'][idres]['idvoo']}')
						print('\n\n')


						#idvoo, numvoo, origem, destino, dtpartida, dtchegada
						print('------------DADOS DO VOO------------')
						print('')
