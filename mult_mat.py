import numpy as np 
from threading import Thread
import sys
import zipfile

#Classes de funções auxiliares para tratamento de exceção 
#Na linha de comando
class Error(Exception):
    pass

class LetraError(Error):
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


	#Exceção para dimensão dada errada por linha de comando
	except ValueError:
		print("Dimensão inválida")
		print()

	#Exceção para o tipo de aplicação dado errada por linha de comando		
	except LetraError:
		print("Tipo de aplicação errada. Por favor, digite S ou C para um tipo válido de aplicação")
		print()
		
	#Exceção para a quantidade de argumentos dada errada por linha de comando
	except QtdArgError:
		print("Quantidade de parâmentros inválidos")
		print()



