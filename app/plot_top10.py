import matplotlib.pyplot as plt
import numpy as np


def plotTop10(modules,file_name,type):
  amount = []
  libs = []
  modules_dict = dict([])

  for i in range(len(modules)):
      modules_dict[str(modules[i]['name'])] = int(modules[i]['amount'])

  libs = sorted(modules_dict, key = modules_dict.get, reverse=True)
  libs = libs[0:10]

  for i in libs:
    amount.append(modules_dict[i])

  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  bars = ax.bar(libs,amount)

  for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        round(bar.get_height(), 1),
        horizontalalignment='center',
        color='black'
    )

  bars[0].set_color('darkred')
  bars[1].set_color('firebrick')
  bars[2].set_color('indianred')
  bars[3].set_color('tomato')
  bars[4].set_color('coral')
  bars[5].set_color('salmon')
  bars[6].set_color('darksalmon')
  bars[7].set_color('lightsalmon')
  bars[8].set_color('sandybrown')
  bars[9].set_color('peachpuff')

  x_pos = np.arange(len(libs))
  plt.xticks(x_pos, libs, rotation=90,fontsize=15)
  ax.set_ylabel('Number of projects', labelpad=15,
                color='#333333',fontsize=15)
  if type == "Std":
    ax.set_title('Most Used Python Libraries', pad=15, color='#333333',
                weight='bold', fontsize=30)
  else:
    ax.set_title('Most Used Python External Libraries', pad=15, color='#333333',
                weight='bold', fontsize=30)

  fig = plt.gcf()
  fig.set_size_inches(10, 5, forward=True)
  fig.savefig(f'./returns/{file_name}.png', bbox_inches='tight')
