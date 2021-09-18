example = {
  "lib_list": [
   {
      "name": "pymongo",
      "amount": 1
    },
    {
      "name": "matplotlib",
      "amount": 23
    },
    {
      "name": "numpy",
      "amount": 20
    },
    {
      "name": "sklearn",
      "amount": 5
    },
    {
      "name": "pytest",
      "amount": 17
    },
    {
      "name": "scipy",
      "amount": 15
    },
    {
      "name": "beautifulsoup",
      "amount": 12
    },
    {
      "name": "pandas",
      "amount": 10
    },
    {
      "name": "requests",
      "amount": 18
    },
     {
      "name": "seaborn",
      "amount": 3
    },
    {
      "name": "flask",
      "amount": 1
    },
    {
      "name": "pillow",
      "amount": 30
    }
  ]
}



import matplotlib.pyplot as plt
import numpy as np

def plotTop10(lib_list):  
    modules_dict = dict([])
    modules = lib_list['lib_list']
    amount = []
    
    for i in range(len(modules)):
        modules_dict[str(modules[i]['name'])] = modules[i]['amount']        

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
    ax.set_title('Most Used Python Libraries', pad=15, color='#333333',
                 weight='bold', fontsize=30)
    
    fig = plt.gcf()
    fig.set_size_inches(10, 5, forward=True)
    plt.show()
    fig.savefig('top10.png', bbox_inches='tight')
    
plotTop10(example)