import threading

def func(lin_a, matriz_b, lin_res):
	for j in range(len(lin_a)):
		soma = 0
		for k in range(len(lin_a)):
			soma += lin_a[k]*matriz_b[k][j]
		lin_res[j] = soma

def multiplicar(matriz_a, matriz_b, resultado, metodo):
	dim = len(matriz_a)
	if(metodo == 'S'):
		soma = 0
		for i in range(dim):
			for j in range(dim):
				soma = 0
				for k in range(dim):
					soma += matriz_a[i][k]*matriz_b[k][j]
				resultado[i][j] = soma
	elif(metodo == 'C'):
		print('Em desenvolvimento...')
		threads = []
		for i in range(dim):
			t = threading.Thread(target=func, args=(matriz_a[i], matriz_b, resultado[i]))
			threads.append(t)
			t.start()
		for thread in threads:
			thread.join()
	else:
		print('Erro ao escolher o método para efetuar o cálculo.')

if(__name__ == '__main__'):
	ma = [[23, 65, 9,54], [12, 2, 7,32], [76, 84, 32,21], [21,32,34,53]]	  
	mb = [[35, 24, 8,43], [32,10, 36, 15], [21,17, 76, 43], [12,12,32,43]]
	res = [[None, None, None,None], [None, None, None,None], [None, None, None,None], [None,None,None,None]]
	multiplicar(ma, mb, res, 'C')
	print(res)