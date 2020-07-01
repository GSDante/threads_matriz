import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio

def gerar_tabela(dim, vetor):
	headerColor = 'grey'
	rowEvenColor = 'lightgrey'
	rowOddColor = 'white'

	fig = go.Figure(data=[go.Table(
	  header=dict(
	    values=['<b>Matriz ' + str(3) + 'x' + str(3) + '</b>','<b>Valor</b>'],
	    line_color='darkslategray',
	    fill_color=headerColor,
	    align=['left','center'],
	    font=dict(color='white', size=12)
	  ),
	  cells=dict(
	    values=[
	      ['Mínimo', 'Médio', 'Máximo'],
	      vetor],
	    line_color='darkslategray',
	    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
	    align = ['left', 'center'],
	    font = dict(color = 'darkslategray', size = 11),
	    height = 30
	    ))
	])

	fig.show()

def plot(tempo_seq, tempos_thr):
	fig, ax = plt.subplots(figsize=(15, 10))
	ax.plot(tempos_seq, c='blue', label='Sequencial')
	ax.plot(tempos_thr, c='red', label='Thread')
	ax.legend(loc='best')
	ax.set_title("Médias dos tempos de execução obtidos por dimensão")
	plt.show()

if(__name__ == '__main__'):
	tempos_seq = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
	tempos_thr = [1.5, 2.8, 6.6, 20.5, 40.6, 200.3, 534.5, 1002.3]
	#gerar_tabela(3, [2, 4, 6])
	plot(tempos_seq, tempos_thr)