import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("100datasetT.csv")
print(df.head())
resultDS= df['RESULT']
print resultDS
first=dist=second=0
for i in resultDS:
	if i=='FIRST':
		first+=1
	elif i=='DIST':
		dist+=1
	elif i=='SECOND':
		second+=1
print(first,dist,second)
 
# Data to plot
labels = 'FIRST','DIST','SECOND'
sizes = [first,dist,second]
colors = ['gold', 'yellowgreen', 'lightcoral']
#explode = (0.1,0.1,0.1)  # explode 1st slice
#Plot
plt.pie(sizes,labels=labels, colors=colors,shadow=True,startangle=140,autopct='%1.0f%%')
plt.title("Result of student from 2005 to 2010")
 
plt.axis('equal')
plt.show()
