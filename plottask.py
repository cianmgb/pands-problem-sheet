import numpy as np
import matplotlib.pyplot as plt
  
# Generating some random data
# for an example
data = np.random.normal(5, 2, 1000)
  
# Plotting the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b', label='Normal Distribution')
  
plt.show()