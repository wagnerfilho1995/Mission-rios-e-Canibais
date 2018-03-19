
# Lista de tuplas, que representa os estados do problema
estados = []

# Array para marcacao de estados ja visitados, cada estado visitado 
# sera um indice nesse array na qual deve ser setado 1
visitados = [0] * 33101

# Array de representacao do estado atual
#	 M  C  B  M  C	
a = [3, 3, 1, 0, 0]

estados.append([3, 3, 1, 0, 0])

# Contador Global
i = 0

def solucao():
	
	if(estados[i][3] + estados[i][4] == 6):
		print("Fronteira:")
		j = i
		for j in range(j, len(estados)):
			if(j == i):
				print("-> {}".format(estados[j]) + " !! Solucao !!")
			else: print(estados[j])
		return False
	else: return True


def foiVisitado(a): #	Verificar se o estado ja foi visitado
	
	#	Converte os valores dentro do array para um numero inteiro
	indice = int(''.join(str(i) for i in a))

	if(visitados[indice] == 1):
		return True
	else:
		visitados[indice] = 1
		return False

def validar(aux):	#	Averiguar todas as condicoes que permitem um estado ser valido ou nao para adicionar na fronteira

	#	Verficiar se existe alguma posicao com valor negativo
	if(aux[0] < 0 or aux[1] < 0 or aux[3] < 0 or aux[4] < 0):
		return False

	#	Verificar se missionarios estao em minoria na esquerda
	if(aux[0] < aux[1] and aux[0] != 0):
		return False
	#	Verificar se missionarios estao em minoria na direita
	if(aux[3] < aux[4] and aux[3] != 0):
		return False

	return True

def fronteira(i):

	print("Fronteira:")

	j = i
	for j in range(j, len(estados)):
		if(j == i):
			print("-> {}".format(estados[j]))
		else: print(estados[j])

	f = estados[i][:]
	if(estados[i][2] == 1): #	Barco esta na margem esquerda

		#	Tentar passar 2 missionarios
		f[0] = f[0] - 2
		f[2] = 0	#	Setar barco no outro lado da margem
		f[3] = f[3] + 2
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]
		#	Tentar passar 1 missionario
		f[0] = f[0] - 1
		f[2] = 0	#	Setar barco no outro lado da margem
		f[3] = f[3] + 1
		if(validar(f)):
			estados.append(f[:])
		
		f = estados[i][:]	
		#	Tentar passar 1 de cada
		f[0] = f[0] - 1
		f[1] = f[1] - 1
		f[2] = 0	#	Setar barco no outro lado da margem
		f[3] = f[3] + 1
		f[4] = f[4] + 1
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]	
		#	Tentar passar 2 canibais
		f[1] = f[1] - 2
		f[2] = 0	#	Setar barco no outro lado da margem
		f[4] = f[4] + 2
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]	
		#	Tentar passar 1 canibal
		f[1] = f[1] - 1
		f[2] = 0	#	Setar barco no outro lado da margem
		f[4] = f[4] + 1
		if(validar(f)):
			estados.append(f[:])

	else: #	Barco esta na margem direita

		#	Tentar passar 2 missionarios
		f[3] = f[3] - 2
		f[2] = 1	#	Setar barco no outro lado da margem
		f[0] = f[0] + 2
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]
		#	Tentar passar 1 missionario
		f[3] = f[3] - 1
		f[2] = 1	#	Setar barco no outro lado da margem
		f[0] = f[0] + 1
		if(validar(f)):
			estados.append(f[:])
		
		f = estados[i][:]	
		#	Tentar passar 1 de cada
		f[3] = f[3] - 1
		f[4] = f[4] - 1
		f[2] = 1	#	Setar barco no outro lado da margem
		f[0] = f[0] + 1
		f[1] = f[1] + 1
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]	
		#	Tentar passar 2 canibais
		f[4] = f[4] - 2
		f[2] = 1	#	Setar barco no outro lado da margem
		f[1] = f[1] + 2
		if(validar(f)):
			estados.append(f[:])

		f = estados[i][:]	
		#	Tentar passar 1 canibal
		f[4] = f[4] - 1
		f[2] = 1	#	Setar barco no outro lado da margem
		f[1] = f[1] + 1
		if(validar(f)):
			estados.append(f[:])

# MAIN
print("========= Problema dos Missionários =========")
print("Pressione enter para Começar!")
start = input()
print("MODELO = [ Me, Ce, B, Md, Cd ]")
print("Me = número de missionários na margem esquerda")
print("Ce = número de canibais na margem esquerda")
print("B = barco, sendo 1 quando está na esquerda e 0 quando está na direita")
print("Md = número de missionários na margem direita")
print("Cd = número de missionários na margem direita")
while(solucao()):
	a = estados[i][:]
	if(foiVisitado(a) == 0):
		fronteira(i)
	i += 1
print("Muito bem! Todos atravessaram em segurança!")