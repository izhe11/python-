import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

data = [
    #year month predicted high   low
    (2007, 8,   113.2,    114.2, 112.2),
    (2007, 9,   112.8,    115.8, 109.8),
    (2007, 10,  111.0,    116.0, 106.0),
    (2007, 11,  109.8,    116.8, 102.8),
    (2007, 12,  107.3,    115.3, 99.3),
    (2008, 1,   105.2,    114.2, 96.2),
    (2008, 2,   104.1,    114.1, 94.1),
    (2008, 3,   99.9,     110.9, 88.9),
    (2008, 4,   94.8,     106.8, 82.8),
    (2008, 5,   91.2,     104.2, 78.2),
 ]

xpos = np.arange(0,4*np.pi,0.1)
ypos = np.sin(xpos)
zpos = np.cos(xpos)
z1 = np.array([0,4*np.pi])
z2 = np.array([0,0])

plt.plot(xpos,ypos,'b',xpos,zpos,'r')    #x y轴数据，绘制多条曲线时传入多组xy参数
plt.plot(z1,z2,'-.')
plt.xlabel('x')            #x轴标题
plt.ylabel('y')            #y轴标题
plt.show()
