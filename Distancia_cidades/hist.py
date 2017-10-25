import numpy as np
import matplotlib.pyplot as plt
import csv

# bins = range(0,3250, 250) 
# bin_centers = [0.5 * e - f for e, f in zip(bins[:-1],bins[1:])]
# col = [b - min(bin_centers) for b in bin_centers]

col = 12
threshold = 130

with open('dist.csv', 'r') as f:
    data=[tuple(line) for line in csv.reader(f)]

data_num = [[float(l[0]), int(l[1])] for l in data]

data_plt = sum( [[e[0]]*e[1] for e in data_num], [])

f, axarr = plt.subplots(3, sharex=False)

axarr[0].hist(np.asarray(data_plt),2*col, color='red')
axarr[0].set_title('Todos os dados')

axarr[1].hist(np.asarray([e for e in data_plt if e > threshold]), 3*col,  color='red')
axarr[1].set_title('Raio maior que %s Km (menor resolução)' % threshold)

axarr[2].hist(np.asarray([e for e in data_plt if e > threshold]), 5*col,  color='red')
axarr[2].set_title('Raio maior que %s Km (maior resolução)' % threshold)

f.subplots_adjust(hspace=0.5)
plt.show()

