import os
import numpy as np
import matplotlib.pyplot as plt

os.system("g++ caminata.cpp -o caminata.x")
os.system("./caminata.x > datos.dat")

data=np.loadtxt("datos.dat")

plt.figure()
plt.plot(data[:,0], data[:,1])
plt.savefig("caminata.png")

