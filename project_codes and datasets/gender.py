import pandas as pd
import numpy as np
df = pd.read_csv("100datasetT.csv")
print(df.head())
genderDS = df['gender']
var = genderDS.groupby(genderDS).count()
print(var)
gender = var.keys
frequency = var.values
count = len(frequency)
ypos = np.arange(0,count)
import matplotlib.pyplot as plt
plt.bar(ypos,frequency,align='center',width=0.2,color=['yellow','red'])
names = ['FEMALE','MALE']
x = range(len(names))
plt.plot(x)
plt.xticks(x, names)
#plt.scatter(y)
plt.title("No of MALE & FEMALE students in sois 2005 to 2010")
plt.xlabel("GENDER")
plt.ylabel("NO OF STUDENT")
#plt.xticks(branch)
plt.show()
