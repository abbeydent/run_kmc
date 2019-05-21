from sklearn.datasets.samples_generator import make_moons
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.cluster import KMeans

X,Y = make_moons(n_samples=400, noise=0.05, random_state=0)

#print(X)

plt.scatter(X[:,0], X[:,1])
plt.savefig('scatterplot_moon.png')

