import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio

def gerar_tabela(vetor):
	headerColor = 'grey'
	rowEvenColor = 'lightgrey'
	rowOddColor = 'white'

	fig = go.Figure(data=[go.Table(
	  header=dict(
	    values=['<b>Matriz ' + '</b>','<b>Speed-up</b>'],
	    line_color='darkslategray',
	    fill_color=headerColor,
	    align=['left','center'],
	    font=dict(color='white', size=12)
	  ),
	  cells=dict(
	    values=[
	      ['4x4', '8x8', '16x16', '32x32', '64x64', '128x128', '256x256', '512x512', '1024x1024', '2048x2048'],
	      vetor],
	    line_color='darkslategray',
	    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor,
	    			 rowEvenColor, rowOddColor, rowEvenColor, rowOddColor, rowEvenColor]],
	    align = ['left', 'center'],
	    font = dict(color = 'darkslategray', size = 11),
	    height = 30
	    ))
	])

	fig.show()

def plot(tempos_seq, tempos_thr):
	fig, ax = plt.subplots(figsize=(15, 15))
	ax.plot(list(range(0, 10)), tempos_seq, c='blue', label='Sequencial')
	ax.plot(list(range(0, 10)), tempos_thr, c='red', label='Thread')
	ax.set_ylabel('Tempo (s)')
	ax.set_xlabel('Dimensão da matriz')
	ax.legend(loc='best')
	ax.set_xticks(np.arange(10))
	ax.set_xticklabels(['4x4', '8x8', '16x16', '32x32', '64x64', '128x128', '256x256', '512x512', '1024x1024', '2048x2048'],
						 rotation = 45)
	ax.set_title("Médias dos tempos de execução obtidos por dimensão")
	plt.show()

if(__name__ == '__main__'):
	medi = open('Dados/media.txt', 'r')
	medi_lista = medi.read().strip().split('\n')
	medi_lista = [round(float(i), 8) for i in medi_lista]

	medi_seq = []
	medi_thr = []
	[medi_seq.append(value) if index % 2 == 0 else medi_thr.append(value) for index, value in enumerate(medi_lista)]
	
	plot(medi_seq, medi_thr)


	'''
	mini = open('Dados/min.txt',  'r')
	maxi = open('Dados/max.txt', 'r')
	medi = open('Dados/media.txt', 'r')

	mini_lista = mini.read().strip().split('\n')
	mini_lista = [round(float(i), 8) for i in mini_lista]

	maxi_lista = maxi.read().strip().split('\n')
	maxi_lista = [round(float(i), 8) for i in maxi_lista]

	medi_lista = medi.read().strip().split('\n')
	medi_lista = [round(float(i), 8) for i in medi_lista]

	speedup = open('Dados/speedup.txt', 'r')
	speedup_lista = speedup.read().strip().split('\n')
	speedup_lista = [round(float(i), 4) for i in speedup_lista]
	

	gerar_tabela(speedup_lista)


	#4x4
	gerar_tabela(4, [mini_lista[0], medi_lista[0], maxi_lista[0]], [mini_lista[1], medi_lista[1], maxi_lista[1]])

	#8x8
	gerar_tabela(8, [mini_lista[2], medi_lista[2], maxi_lista[2]], [mini_lista[3], medi_lista[3], maxi_lista[3]])

	#16x16
	gerar_tabela(16, [mini_lista[4], medi_lista[4], maxi_lista[4]], [mini_lista[5], medi_lista[5], maxi_lista[5]])

	#32x32
	gerar_tabela(32, [mini_lista[6], medi_lista[6], maxi_lista[6]], [mini_lista[7], medi_lista[7], maxi_lista[7]])

	#64x64
	gerar_tabela(64, [mini_lista[8], medi_lista[8], maxi_lista[8]], [mini_lista[9], medi_lista[9], maxi_lista[9]])

	#128x128
	gerar_tabela(128, [mini_lista[10], medi_lista[10], maxi_lista[10]], [mini_lista[11], medi_lista[11], maxi_lista[11]])

	#256x256
	gerar_tabela(256, [mini_lista[12], medi_lista[12], maxi_lista[12]], [mini_lista[13], medi_lista[13], maxi_lista[13]])

	#512x512
	gerar_tabela(512, [mini_lista[14], medi_lista[14], maxi_lista[14]], [mini_lista[15], medi_lista[15], maxi_lista[15]])

	#1024x1024
	gerar_tabela(1024, [mini_lista[16], medi_lista[16], maxi_lista[16]], [mini_lista[17], medi_lista[17], maxi_lista[17]])

	#2048x2048
	gerar_tabela(2048, [mini_lista[18], medi_lista[18], maxi_lista[18]], [mini_lista[19], medi_lista[19], maxi_lista[19]])
'''
