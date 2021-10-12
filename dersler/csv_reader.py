from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ax = plt.axes(projection='3d')

namafile = 'bodyData3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"

index = count()

def animate(i):
    data = pd.read_csv('bodyData3D.csv')

    x = data[header1]
    y = data[header2]
    z = data[header3]

    plt.cla()

    ax.plot3D(x, y, z, 'red')

    ax.scatter(x, y, z, c='b', marker='o')

    ax.set_xlabel('X mm')
    ax.set_ylabel('Y mm')
    ax.set_zlabel('Z mm')


    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=500)


plt.tight_layout()
plt.show()
