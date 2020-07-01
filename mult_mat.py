import numpy as np 
import threading 
import sys
import zipfile
import time 

#Classes de funções auxiliares para tratamento de exceção 
#Na linha de comando
class Error(Exception):
    pass

class QtdArgError(Error):
	pass



#Função para verificar se o valor está na base 2
def base_2(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True

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
	#Operação em sequencial da mutiplicação de matrizes
	if(metodo == 'S'):
		soma = 0
		for i in range(dim):
			for j in range(dim):
				soma = 0
				for k in range(dim):
					soma += matriz_a[i][k]*matriz_b[k][j]
				resultado[i][j] = soma

	#Multiplição entre matrizes concorretemente utilizando threads por linhas
	elif(metodo == 'C'):
		threads = []
		#Criando as threads baseado na quantidade de linhas da matriz
		for i in range(dim):
			t = threading.Thread(target=func, args=(matriz_a[i], matriz_b, resultado[i]))
			
			#Nome da thread
			t.name = "thread_" + str(i)
			threads.append(t)
			t.start()

		#Coordenandos as threads
		for thread in threads:
			thread.join()
	else:
		print('Erro ao escolher o método para efetuar o cálculo.')

if __name__ == '__main__':


	try:

		#Verificando se o valor é na base 2
		if (base_2(int(sys.argv[1])) == False):
			raise ValueError
		
		#Verificando se o está pedindo o tipo sequencial ou concorrente
		elif sys.argv[2] != "S" and sys.argv[2] != "C":
			raise LetraError 

		#Verificando a quantidade argumentos na linha de comando	
		elif len(sys.argv) != 3:
			raise QtdArgError 

		col = int(sys.argv[1])
		lin = int(sys.argv[1])
		metodo = sys.argv[2]

		#Variaveis que registram o nome das matrizes A e B
		#O "Matrizes/" é por conta do .namelist
		name_A = "Matrizes/A" + sys.argv[1] + "x" + sys.argv[1] +".txt"
		name_B = "Matrizes/B" + sys.argv[1] + "x" + sys.argv[1] +".txt"

		matriz_A = []
		matriz_B = []
		#Procurando as matrizes no arquivo "Matrizes.zip"
		with zipfile.ZipFile("Matrizes.zip", "r") as file:
			for name in file.namelist():
				if name == name_A:
					f = open(name, "r")
					#Pegando as dimensões na primeira linha do arquivo
					dimension = f.readline()
					while True:
						values = f.readline()

						#Pegando os valores do arquivo e retirando só os inteiros
						matriz_A.append(list(map(int,values.split())))

						#Parando no fim da linha
						if not values:
							break

				elif name == name_B:
					f = open(name, "r")
					#Pegando as dimensões na primeira linha do arquivo
					dimension = f.readline()
					while True:
						values = f.readline()

						#Pegando os valores do arquivo e retirando só os inteiros
						matriz_B.append(list(map(int,values.split())))

						#Parando no fim da linha
						if not values:
							break

		#Filtrando os elemento vazios das matrizes
		matriz_A = [x for x in matriz_A if x != []]
		matriz_B = [x for x in matriz_B if x != []]

		resultado = np.zeros((len(matriz_A), len(matriz_B))).tolist()
		
		#Gravando o tempo nos 20 testes
		tempo = np.zeros(20)

		for i in range(20):
			start = time.time()
			multiplicar(matriz_A, matriz_B, resultado, metodo)
			end = time.time()

			tempo[i] = (end - start)
		
		#Dados estatísticos	
		tempo_media = np.mean(tempo)
		tempo_max = np.amax(tempo)
		tempo_min = np.amin(tempo)
		tempo_desvio_padrao = np.std(tempo)
				
		#Abrindo os .txt para armazenar os dados
		media_registro = open("Dados/media.txt",'a')
		max_registro = open("Dados/max.txt",'a')
		min_registro = open("Dados/min.txt",'a')
		desvio_padrao_registro = open("Dados/desvio_padrao.txt",'a')

		#Registrando os dados nem .txt
		media_registro.write(str(tempo_media) + "\n")
		max_registro.write(str(tempo_max) + "\n")
		min_registro.write(str(tempo_min) + "\n")
		desvio_padrao_registro.write(str(tempo_desvio_padrao) + "\n")

	#Exceção para dimensão dada errada por linha de comando
	except ValueError:
		print("Dimensão inválida")
		print()


		
	#Exceção para a quantidade de argumentos dada errada por linha de comando
	except QtdArgError:
		print("Quantidade de parâmentros inválidos")
		print()



