''' 
Consider the following data. Draw a pie chart.
It should have the following:
a) Graph title should be “Forest cover of north eastern states”.
b) Explode the ‘Mizoram’
c) Show legend
d) Show percentage
e) Edge color should be black
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
State=['Arunachal Pradesh','Assam','Manipur','Meghalaya','Mizoram','Ngaland','Tripura']
ForestCover=[66964,28105,17346,17146,18186,12489,7726]
myexplode=[0,0,0,0,0.2,0,0]

plt.pie(ForestCover,labels=State,wedgeprops={"edgecolor":"black"},autopct="%1.1f%%",explode=myexplode)
plt.title("Forest cover of north eatsern states")
plt.legend(State)
plt.show()
