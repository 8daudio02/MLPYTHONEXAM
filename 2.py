import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
plt.title("Monthwise Chair and product sales")
plt.bar(df['months'], df['chair'], label ='Chair')
plt.xlabel('Months')
plt.ylabel('Units Sold')
plt.legend(loc='best')
plt.show()
plt.title("All products sales data")
plt.stackplot(list(df.columns.values)[1:7],df.iloc[:,1:7],labels=list(df.columns.values)[1:7])
plt.show()
