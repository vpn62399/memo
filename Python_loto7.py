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
    url2 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7c.csv'
    # lpd = pd.read_csv(url1, header=None)
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    lpd = pd.read_csv(url1, names=('t1', 'd1', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
                      'b1', 'b2', 'n1', 'n2', 'n3', 'z1', 'z2'), usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])
    # lpd = pd.read_csv(url1, header=None, usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])

    lpd.set_index('d1')
    lpd.index
    lpd.plot()
    # lpd.plot('d1', ['s1', 's2', 's3', 's4', 's5', 's6', 's7'])
    plt.show()
    print('77')


def t2():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    lpd = pd.read_csv(url1, header=None)
    lpd.plot()
    plt.show()


def t3():
    filename = 'alll7.csv'
    lpd = pd.read_csv(filename)
    tpd = lpd['n1']
    print(tpd.head())
    # tpd.plot()
    # lpd.plot()
    # plt.show()


def t4():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    url2 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7c.csv'

    lpd1 = pd.read_csv(url1, header=None, usecols=[0, 2, 15])
    lpd2 = pd.read_csv(url2, header=None)

    temp2 = lpd1.loc[lpd1[2] == 3]
    temp = lpd2.loc[lpd2[11].isnull()]
    lpd2 = temp.loc[:, [0, 12]]
    lpd3 = pd.merge(lpd2, temp2, left_on=0, right_on=0)
    print(lpd3.head(10))
    # plt.plot(lpd3[0:100])
    lpd3[0:900].plot()
    plt.show()


def t5():
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select * from alll7 where s1=5 and s2=17 and s3!=18 and id>6850000 and id<6880000 and id=abs(random())%10295473 limit 3'''
    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            # print(xx)
            # print("T_cpt2([{},{},{},{},{},{},{},{}])".format(xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],xx[7],xx[0]))
            print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], 0, xx[0]))
            x = x+1
        if x > 200:
            break
t5()
