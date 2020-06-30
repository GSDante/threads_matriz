import numpy as np
import threading
#Funcao executada pela thread
#A função recebe a linha da matriz A, toda a matriz B, e a linha da matriz de resultado
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
			t.name = "thread_" + str(i)
			threads.append(t)
			t.start()
		for thread in threads:
			print(thread.name)
			thread.join()
	else:
		print('Erro ao escolher o método para efetuar o cálculo.')

if(__name__ == '__main__'):
	ma = [[93, 34, 12, 6], [9, 37, 23, 47], [81, 69, 33, 10], [65, 23, 98, 56]]	  
	mb = [[84, 26, 23, 15], [73, 14, 66, 36], [81, 67, 26, 73], [35, 87, 32, 89]]
	res = np.zeros((len(ma), len(ma))).tolist()
	multiplicar(ma, mb, res, 'C')
	print(res)