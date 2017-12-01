import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("100datasetT.csv")
print(df.head())
statusDS = df['status']
print statusDS
completed=left=0
for i in statusDS:
	if i=='COMPLETED':
		completed+=1
	elif i=='LEFT':
		left+=1
print('completed 98.45%,left 1.54%')

# Data to plot
labels = 'completed','left'
sizes = [completed,left]
colors = ['gold', 'yellowgreen']
#explode = (0.1,0.1)  # explode 1st slice

# Plot
plt.pie(sizes,labels=labels,colors=colors,shadow=True, startangle=140,autopct='%1.0f%%')
plt.title("The student completed AND left the ME 2005 to 2010")
plt.axis('equal')
plt.show()
