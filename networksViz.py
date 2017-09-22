import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np

data = np.array([['Carrier','Size'],
                ['Anthem BCBS',15689],
                ['Bright',7507],
                ['Cigna',13550],
                ['Kaiser',13391],
                ['CO Choice',5711],
                ['Denver Health',858],
                ['RMHP',11672]])
# 
df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])
# 
df.Size = df.Size.str.replace(',', '').astype(int).fillna(0)
style.use('fivethirtyeight')
col = ['darkblue','r','g','c','royalblue','m','goldenrod']
#
df.plot(kind='bar', color=col, legend=None)
plt.ylabel('Unique Providers and\nFacilities/Pharmacies')
plt.title('2017 Network Size Measured In Unique "IndividualProviders"\nand "Facilities&Pharmacies" According to SERFF')
plt.grid(True)
plt.show()