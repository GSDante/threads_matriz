import numpy as np 



#Arquivo com as médias de todos os teste sequenciais e concorrentes
medias = open("Dados/media.txt",'r')
#Vai pegar os valores de dois em dois
speed = np.zeros(10)

sequencial = []
concorrente = []
#Pegando os valores linha por linha
while True:
	sequencial_line = medias.readline()
	concorrente_line = medias.readline()

	sequencial.append(list(map(float,sequencial_line.split())))
	concorrente.append(list(map(float,concorrente_line.split())))

	if not sequencial_line:
		break

sequencial = [x for x in sequencial if x !=[]]
concorrente = [x for x in concorrente if x !=[]]

seq = np.array(sequencial)
con = np.array(concorrente)
speedup_registro = open("Dados/speedup.txt",'w')

for i in range(len(speed)):
	speed[i] = (seq[i])/(con[i])
	speedup_registro.write(str(speed[i]) + "\n")