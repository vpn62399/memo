# pip install numpy
# pip install pandas
# pip install pyplot
# pip install matplotlib
# pip list
# pip show selenium

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def t1():
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    url2 ='https://raw.githubusercontent.com/kankanla/memo/master/loto7c.csv'
    # lpd = pd.read_csv(url1, header=None)
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    lpd = pd.read_csv(url1, names=('t1', 'd1', 's1', 's2', 's3', 's4', 's5', 's6', 's7','b1', 'b2', 'n1', 'n2', 'n3', 'z1', 'z2'), usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])
    # lpd = pd.read_csv(url1, header=None, usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])

    lpd.set_index('d1')
    lpd.index
    lpd.plot()
    # lpd.plot('d1', ['s1', 's2', 's3', 's4', 's5', 's6', 's7'])
    plt.show()
    print('77')

def t2():
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    lpd = pd.read_csv(url1,header=None)
    lpd.plot()
    plt.show()

def t3():
    filename = 'alll7.csv'
    lpd=pd.read_csv(filename)
    tpd = lpd['n1']
    print(tpd.head())
    # tpd.plot()
    # lpd.plot()
    # plt.show()

t3()
