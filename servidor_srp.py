from xmlrpc.server import SimpleXMLRPCServer
import tadbd_srp.py as tadbd

#definindo as funções



def adPassageiro(idpass, nome, email, fone):
	tadbd.adPassageiro(bd, idpass, nome, email, fone)

def adReserva(idres, data, status, assento, idpass, idvoo):
	tadbd.adReserva(bd, idres, data, status, assento, idpass, idvoo)

def adVoo(idvoo, numvoo, origem, destino, dtpartida, dtchegada):
	tadbd.adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada)

def getPassageiro(id):
	if tadbd.passExiste(bd, id) == True:
		return bd['passageiros'][id]

def getVoo(id):
	if tadbd.vooExiste(bd, id) == True:
		return bd['voos'][id]

def getReserva(id):
	return bd['reservas'][id]

def vooExiste(idvoo):
	return tadbd.vooExiste(bd, idvoo)

def passExiste(idpass):
	return tadbd.passExiste(bd, idpass)

def vagasVoo(idvoo):
	return tadbd.vagasVoo(bd, idvoo)

def assentoLivre(idvoo, assento):
	return tadbd.assentoLivre(bd, idvoo, assento)
	
#--------------------MAIN---------------------


def main():
	print("Servidor SRP rodando na porta 8000...")
	server = SimpleXMLRPCServer(("localhost", 8000))


	global bd
	bd = tadbd.open_bd('tabpassageiros.txt', 'tabreservas.txt', 'tabvoos.txt')


#-------------REGISTRANDO---AS---FUNÇÕES-------------

	server.register_function(adPassageiro, 'adPass')
	server.register_function(adReserva, 'adRes')
	server.register_function(adVoo, 'adVoo')
	server.register_function(getPassageiro, 'getPass')
	server.register_function(getVoo, 'getVoo')
	server.register_function(getReserva, 'getRes')
	server.register_function(vooExiste, 'vooExiste')
	server.register_function(passExiste, 'passExiste')
	server.register_function(vagasVoo, 'vagas')
	server.register_function(assentoLivre, 'assentoLivre')

#---------RODANDO----SERVIDOR-------------------
	server.serve_forever()


#-------SALVA ANTES DE ENCERRAR----------------
	tadbd.salva_bd(bd, 'tabpassageiros.txt', 'tabreservas.txt', 'tabvoos.txt')

main()
