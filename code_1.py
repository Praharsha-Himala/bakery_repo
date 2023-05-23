import numpy as np
arr = np.linspace(-5,5,10)
import matplotlib.pyplot as plt
arr2 = np.arange(1,11)
plt.plot(arr,arr2,':')
plt.plot(arr2,arr,color= "red")
plt.show()
