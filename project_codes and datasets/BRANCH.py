import pandas as pd
import numpy as np
df = pd.read_csv("100datasetT.csv")
print(df.head())
branchDS = df['branch']
var = branchDS.groupby(branchDS).count()
print(var)
sbranch = var.keys
frequency = var.values
count = len(frequency)
ypos = np.arange(0,count)
import matplotlib.pyplot as plt
plt.bar(ypos,frequency,label= 'label',align='center',width=0.5,color = ['red','green','blue','yellow'])
#label = xticks(ypos)
names = ['EMBEDDED','MEDICAL SOFTWARE','VLSI-CAD','VLSI-SDV']
x = range(len(names))
plt.plot(x)
plt.xticks(x, names)
plt.title("No of students in sois")
plt.xlabel("Branch")
plt.ylabel("No of student")
#plt.xticks(['E-COMMERCE','MEDICAL SOFTWARE'])
labels = ['E-COMMERCE','MEDICAL SOFTWARE']

#plt.xticks(ypos, labels)
plt.show()
