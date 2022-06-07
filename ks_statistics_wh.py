import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


data = pd.read_csv('weight-height.csv')


plt.bar(list(range(len(data.Weight))), data.Weight)
plt.title('Weight data')
plt.show()

plt.bar(list(range(len(data.Height))), data.Height)
plt.title('Height data')
plt.show()


print(stats.kstest(data.Weight, 'norm',(data.Weight.mean(), data.Weight.std()), N=5000))
print(stats.kstest(data.Height, 'norm',(data.Height.mean(), data.Height.std()), N=5000))
