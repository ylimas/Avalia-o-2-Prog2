from xmlrpc.server import SimpleXMLRPCServer
import tadbd_srp as tadbd

def adPassageiro(idpass, nome, email, fone):
	return tadbd.adPassageiro(bd, idpass, nome, email, fone)

def adReserva(idres, data, status, assento, idpass, idvoo):
	return tadbd.adReserva(bd, idres, data, status, assento, idpass, idvoo)

def adVoo(idvoo, numvoo, origem, destino, dtpartida, dtchegada):
	return tadbd.adVoo(bd, idvoo, numvoo, origem, destino, dtpartida, dtchegada)

def getPassageiro(id):
	if tadbd.passExiste(bd, id) == True:
		return bd['passageiros'][id]
	return None

def getVoo(id):
	if tadbd.vooExiste(bd, id) == True:
		return bd['voos'][id]
	return None

def getReserva(id):
	if id in bd['reservas']:
		return bd['reservas'][id]
	return None

def vooExiste(idvoo):
	return tadbd.vooExiste(bd, idvoo)

def passExiste(idpass):
	return tadbd.passExiste(bd, idpass)

def vagasVoo(idvoo):
	return tadbd.vagasVoo(bd, idvoo)

def assentoLivre(idvoo, assento):
	return tadbd.assentoLivre(bd, idvoo, assento)
	
def main():
	print("Servidor SRP rodando na porta Local 8000...")
	server = SimpleXMLRPCServer(("localhost", 8000))

	global bd
	bd = tadbd.open_bd('tabpassageiros.txt', 'tabreservas.txt', 'tabvoos.txt')

	server.register_function(adPassageiro, 'adPassageiro')
	server.register_function(adReserva, 'adReserva')
	server.register_function(adVoo, 'adVoo')
	server.register_function(getPassageiro, 'getPassageiro')
	server.register_function(getVoo, 'getVoo')
	server.register_function(getReserva, 'getReserva')
	server.register_function(vooExiste, 'vooExiste')
	server.register_function(passExiste, 'passExiste')
	server.register_function(vagasVoo, 'vagasVoo')
	server.register_function(assentoLivre, 'assentoLivre')

	server.serve_forever()

	tadbd.salva_bd(bd, 'tabpassageiros.txt', 'tabreservas.txt', 'tabvoos.txt')

main()
