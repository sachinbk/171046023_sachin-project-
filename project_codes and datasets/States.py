import pandas as pd
import numpy as np
df = pd.read_csv("100datasetT.csv")
print(df)
print(df.head())
stateDS = df['state']
var = stateDS.groupby(stateDS).count()
print(var)
states = var.keys
frequency = var.values
count = len(frequency)
ypos = np.arange(0,count)
import matplotlib.pyplot as plt
#plt.pie(shadow=True,startangle=140,autopct='%1.0f%%')
plt.bar(ypos,frequency,color=['red','blue','green','yellow','gray','orange','lightgreen'],align='center',width=0.7)
names = ['AP','DEL','KAR','KEL','MAH','TAM','UP']
x = range(len(names))
plt.xticks(x, names)
plt.title("Different states of student in sois 2005 to 2010")
plt.xlabel("states")
plt.ylabel("NO OF STUDENT")
#plt.xticks(states)
plt.show()
