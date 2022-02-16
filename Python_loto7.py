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


def tx1(num):
    import csv
    f = open('xStep-L7.csv', 'r')
    da = csv.reader(f)
    for x in da:
        if int(num) > int(x[0]) and int(num) < int(x[1]):
            if int(x[2]) > 1:
                return 2
            return 1
    return 0

# tx1(8149925)


def t5():
    # 番号指定
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
        if x > 5:
            break


def t6():
    # 番号指定 Loto7
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select * from alll7 where id=abs(random())%10295473'''

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >1458200 and id < 8041128 '''
    # loto7.loc[:,12].describe()
    # mean	5365861e+06
    # std	3031056e+06
    # min	1458200e+04
    # 25%	2820762e+06
    # 50%	5539011e+06
    # 75%	8041128e+06
    # max	1027423e+07

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >2940107 and id < 9016912 '''
    # loto7.loc[0:20,[12]].describe()
    # mean	4965708e+06
    # std	5729267e+06
    # min	9145050e+05
    # 25%	2940107e+06
    # 50%	4965708e+06
    # 75%	6991310e+06
    # max	9016912e+06

    # 番号指定 Loto7
    inar = [5, 9, 15, 17, 31, 33, 36]
    notinar = [3, 4, 6, 11, 12, 16, 20, 23]

    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            nocnt = 0
            cnt = 0
            for j in notinar:
                if j in xx:
                    nocnt = nocnt + 1

            if nocnt == 1:
                for j in inar:
                    if j in xx:
                        cnt = cnt + 1
                if cnt > 1:
                    tck = tx1(xx[0])
                    if tck == 0 or tck > 1:
                        print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                            xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], tck, xx[0]))
                        x = x+1
        if x > 10:
            cur.close()
            break


# t6()


def t7():
    # 平均値の前後+2-2 (vls + lv)
    # 当たる確率低い
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select * from alll7 where id=abs(random())%10295473'''
    vls = [4, 12, 16, 20, 25, 29, 33]
    x = 0
    lv = 4
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            if int(xx[1]) > (vls[0]-lv) and int(xx[1]) < (vls[0]+lv):
                if int(xx[2]) > (vls[1]-lv) and int(xx[2]) < (vls[1]+lv):
                    if int(xx[3]) > (vls[2]-lv) and int(xx[3]) < (vls[2]+lv):
                        if int(xx[4]) > (vls[3]-lv) and int(xx[4]) < (vls[3]+lv):
                            if int(xx[5]) > (vls[4]-lv) and int(xx[5]) < (vls[4]+lv):
                                if int(xx[6]) > (vls[5]-lv) and int(xx[6]) < (vls[5]+lv):
                                    if int(xx[7]) > (vls[6]-lv) and int(xx[7]) < (vls[6]+lv):
                                        print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                                            xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], '', xx[0]))
                                        x = x+1
        if x > 10:
            cur.close()
            break
# t7()


def t8():
    # 番号指定 Loto6
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = '''select * from alll6 where id=abs(random())% 6096455'''

    inar = [2, 4, 8]
    notinar = [1, 3, 6, 19, 21, 27, 39]

    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            nocnt = 0
            cnt = 0
            for j in notinar:
                if j in xx:
                    nocnt = nocnt + 1

            if nocnt == 0:
                for j in inar:
                    if j in xx:
                        cnt = cnt + 1
                if cnt == 2:
                    tck = tx1(xx[0])
                    if tck == 0 or tck > 1:
                        print("localStorage_additem([{},{},{},{},{},{},{}])".format(
                            xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], tck, xx[0]))
                        x = x+1
        if x > 10:
            cur.close()
            break


# t8()

def t9():
    # 組み合わせ確認
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = '''select t1,d1,s1,s2,s3,s4,s5,s6 from loto6'''
    list(range(1, 38))

    for i in range(1, 38):
        pass
        # print(i)

    cr = con.execute(sqlcmd)
    ct = 0
    ck = [2, 4, 18]
    for b in ck:
        print(b)

    for jj in cr:
        if ck[0] in jj and ck[1] in jj and ck[2] in jj:
            print(jj)
            ct += 1
    print(ck, ct)


t9()
