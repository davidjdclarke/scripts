from matplotlib import pyplot as plt
import numpy as np

def lut(offset, mean, e):
	max_val = 256
	hist = np.zeros((256), dtype=np.uint8)
	
	for i in range(max_val):
	    if offset >= 0:
	    	num = max_val - 1 - 2*offset
	    	den = 1 + ((mean / (i+1)) ** (10 * e))
	    	hist[i] = (num / den) + 2*offset
	    else:
	    	num = max_val - 1 + 2*offset
	    	den = 1 + ((mean / (i+1)) ** (10 * e))
	    	hist[i] = (num / den)
	return hist


# params        
h1 = lut(0, 128, 1)
h2 = lut(25, 128, 1)
h3 = lut(50, 128, 1)
h4 = lut(75, 128, 1)
h5 = lut(100, 128, 1)

plt.plot(h1, label='h1')
plt.plot(h2, label='h2')
plt.plot(h3, label='h3')
plt.plot(h4, label='h4')
plt.plot(h5, label='h5')

print('h1 (mean):' + str(np.mean(h1)))
print('h2 (mean):' + str(np.mean(h2)))
print('h3 (mean):' + str(np.mean(h3)))
print('h4 (mean):' + str(np.mean(h4)))
print('h5 (mean):' + str(np.mean(h5)))

plt.grid()
plt.legend()
plt.show()        
        
